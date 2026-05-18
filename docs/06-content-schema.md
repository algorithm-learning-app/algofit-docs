# 콘텐츠 스키마

문항은 JSON으로 관리한다. 필드명은 **영문**, 지문·해설은 **한국어** 문자열.

## 공통 필드 (`QuestionBase`)

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | yes | 전역 고유 ID, e.g. `pick_arr_001` |
| `type` | `"pick"` \| `"blank"` \| `"scenario_map"` | yes | 문항 유형 |
| `version` | integer | yes | 스키마/문항 버전, start at 1 |
| `language` | string | yes | 코드 예시 언어: `python` \| `java` \| `javascript` \| `typescript` \| `c` \| `go` \| `kotlin` (Pick은 MVP에서 `python`, Blank는 사용자 설정에 따라 필터) |
| `stem` | string | yes | 문제 지문 (KO) |
| `tags` | string[] | yes | 패턴 태그, e.g. `["array"]` |
| `difficulty` | 1 \| 2 \| 3 | yes | 1=easy, 3=hard |
| `explanation` | string | yes | 정답 해설 (KO), 3문장 이내 권장 |
| `metadata` | object | no | `author`, `source`, `createdAt` |

---

## Pick (`type: "pick"`)

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `choices` | `Choice[]` | yes | 3~4개 |
| `correctChoiceId` | string | yes | 정답 choice의 `id` |

### `Choice`

| Field | Type | Required |
|-------|------|----------|
| `id` | string | yes, e.g. `c1` |
| `label` | string | yes | 선택지 텍스트 (KO) |

### Example

```json
{
  "id": "pick_arr_001",
  "type": "pick",
  "version": 1,
  "language": "python",
  "stem": "정렬된 배열에서 특정 값의 존재 여부만 빠르게 확인하려 합니다. 시간 복잡도를 줄이려면 어떤 방법이 적절할까요?",
  "tags": ["binary_search"],
  "difficulty": 1,
  "choices": [
    { "id": "c1", "label": "이분 탐색" },
    { "id": "c2", "label": "투 포인터" },
    { "id": "c3", "label": "해시 테이블" },
    { "id": "c4", "label": "BFS" }
  ],
  "correctChoiceId": "c1",
  "explanation": "이미 정렬된 배열에서 값 하나를 찾을 때는 이분 탐색이 O(log n)으로 가장 적합합니다. 투 포인터는 보통 두 인덱스를 조절하는 부분 배열 문제에 씁니다."
}
```

---

## Blank (`type: "blank"`)

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `codeTemplate` | string | yes | 빈칸은 `{{blank_id}}` 플레이스홀더 |
| `blanks` | `BlankSlot[]` | yes | 1~3개 |
| `distractors` | string[] | no | 공통 오답 풀 (드래그 MVP) |

### `BlankSlot`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | yes | `b1`, matches placeholder |
| `correctAnswers` | string[] | yes | 허용 정답 (공백 trim 후 비교) |
| `choices` | string[] | yes | MVP 키워드 픽: 정답+오답 3~6개 |

### Example

```json
{
  "id": "blank_bs_001",
  "type": "blank",
  "version": 1,
  "language": "python",
  "stem": "정렬된 배열 nums에서 target의 인덱스를 반환하는 이분 탐색입니다. 빈칸을 채우세요.",
  "tags": ["binary_search"],
  "difficulty": 2,
  "codeTemplate": "def search(nums, target):\n    left, right = 0, len(nums) - 1\n    while {{b1}}:\n        mid = (left + right) // 2\n        if nums[mid] == target:\n            return mid\n        elif nums[mid] < target:\n            {{b2}}\n        else:\n            right = mid - 1\n    return -1",
  "blanks": [
    {
      "id": "b1",
      "correctAnswers": ["left <= right"],
      "choices": ["left <= right", "left < right", "left != right", "mid <= right"]
    },
    {
      "id": "b2",
      "correctAnswers": ["left = mid + 1"],
      "choices": ["left = mid + 1", "left = mid", "right = mid - 1", "left = mid - 1"]
    }
  ],
  "explanation": "while 조건은 left <= right로 구간을 유지합니다. target이 더 크면 left를 mid+1로 올려 왼쪽 절반을 버립니다."
}
```

---

## Scenario map (`type: "scenario_map"`)

실전 시나리오 · 현실 문제 매핑. 스펙·작가 가이드: [12-real-world-scenarios.md](12-real-world-scenarios.md).

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `scenarioCategory` | string | yes | `logistics` \| `matching` \| `scheduling` \| `search_filter` \| `aggregation` \| `limits_security` \| `inventory` \| `navigation` |
| `patternChoices` | `PatternChoice[]` | yes | 4~6개, `id` + `label` (KO) + `patternTag` (snake_case) |
| `primaryPatternIds` | string[] | yes | 정답으로 인정할 choice `id` (MVP: 길이 1) |
| `acceptablePatternIds` | string[] | no | 부분 점수용 추가 정답 (v1.1) |
| `modelingQuestion` | object | no | “먼저 무엇으로 모델링?” 보조 문항 |
| `tone` | `"playful"` \| `"neutral"` | no | UI 톤 힌트, default `playful` |

### `PatternChoice`

| Field | Type | Required |
|-------|------|----------|
| `id` | string | yes, e.g. `p1` |
| `label` | string | yes | 선택지 (KO), 패턴 이름 또는 짧은 설명 |
| `patternTag` | string | yes | `tags`와 동일 체계, e.g. `bfs` |

### `modelingQuestion` (optional)

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `stem` | string | yes | 보조 질문 (KO) |
| `choices` | `Choice[]` | yes | 4개 권장 |
| `correctChoiceId` | string | yes | e.g. `graph`, `array` — 해설용 태그 |

### Example

```json
{
  "id": "scenario_logistics_001",
  "type": "scenario_map",
  "version": 1,
  "language": "python",
  "stem": "배달 앱이 라이더 민수에게 여러 픽업 지점을 한 번에 돌게 합니다. 도로는 격자이고, 벽은 지날 수 없습니다. 모든 픽업을 거친 뒤 다시 허브로 돌아오는 **총 이동 칸 수**를 최소로 잡고 싶습니다. (지점 수는 작고, 이동은 상하좌우만 가능)",
  "scenarioCategory": "logistics",
  "tags": ["bfs"],
  "difficulty": 2,
  "tone": "playful",
  "patternChoices": [
    { "id": "p1", "label": "BFS로 최소 칸 수/홉 수 탐색", "patternTag": "bfs" },
    { "id": "p2", "label": "이분 탐색으로 정렬된 목록만 조회", "patternTag": "binary_search" },
    { "id": "p3", "label": "해시로 방문 메뉴만 기록", "patternTag": "hash" },
    { "id": "p4", "label": "스택으로 괄호 짝 맞추기", "patternTag": "stack" }
  ],
  "primaryPatternIds": ["p1"],
  "modelingQuestion": {
    "stem": "구현에 들어가기 전, 이 상황을 가장 먼저 무엇으로 놓는 게 자연스러울까요?",
    "choices": [
      { "id": "m1", "label": "격자/지점 그래프 (칸·간선)" },
      { "id": "m2", "label": "정렬된 1차원 배열만" },
      { "id": "m3", "label": "문자열 괄호 스택" },
      { "id": "m4", "label": "단일 정수 변수만" }
    ],
    "correctChoiceId": "m1"
  },
  "explanation": "격자에서 칸 수·홉 수를 최소로 하는 전형 신호는 BFS입니다. 이분 탐색은 정렬된 값 조회, 해시는 빠른 lookup에 쓰입니다. 먼저 지점을 그래프/격자로 모델링한 뒤 탐색 패턴을 고르세요."
}
```

---

## 번들·커리큘럼 (참고)

스테이지/일일 세트는 문항 ID 참조만 한다.

```json
{
  "id": "stage_w1_05",
  "worldId": "world_1",
  "questionIds": ["pick_arr_003", "blank_arr_002", "pick_tp_001"],
  "passAccuracy": 0.7
}
```

```json
{
  "id": "daily_2026_05_17",
  "date": "2026-05-17",
  "questionIds": ["pick_hash_002", "pick_bs_001", "blank_tp_001", "pick_stack_001", "blank_bfs_001"]
}
```

---

## 검증 규칙 (구현 시)

1. `correctChoiceId` ∈ `choices[].id`
2. Blank: every `{{bx}}` in `codeTemplate` has matching `blanks[].id`
3. `choices` per blank must include all `correctAnswers`
4. `scenario_map`: every `primaryPatternIds[]` ∈ `patternChoices[].id`; `patternTag` on correct choices should match `tags`
5. `id` regex: `^(pick|blank|scenario)_[a-z0-9_]+$`

## 파일 배치 (권장)

```
content/
  questions/
    pick.json          # 또는 pick/ 패턴별 분리
    blank.json
    scenario.json      # Should
  worlds/
    world_1.json
  daily/
    manifest.json
```

제작 절차·QA: [19-content-authoring.md](19-content-authoring.md). 모바일·PC 앱은 빌드 시 이 경로의 JSON을 번들로 가져온다 ([13-tech-architecture.md](13-tech-architecture.md) §5).
