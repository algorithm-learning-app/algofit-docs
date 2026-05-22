# 콘텐츠 제작 가이드

Pick·Blank·실전 시나리오(`scenario_map`) 문항을 JSON으로 작성·검수하는 절차입니다. 필드 스키마는 [06-content-schema.md](06-content-schema.md), 샘플 전문은 [08-sample-questions.md](08-sample-questions.md)를 따릅니다.

---

## 1. 파일 배치

```
content/
  questions/
    pick.json          # type: pick 일괄 (또는 pick/ 아래 패턴별 분리)
    blank.json         # type: blank 일괄
    scenario.json      # type: scenario_map (Should, v1.0~)
  worlds/
    world_1.json       # questionIds 참조만
  daily/
    manifest.json      # 날짜별 questionIds
```

| 파일 | 권장 형식 | 비고 |
|------|-----------|------|
| `pick.json` / `blank.json` | 최상위 `{ "schemaVersion", "type", "updatedAt", "questions": [...] }` | MVP: 패턴당 1파일보다 유형별 1파일이 diff·리뷰에 유리 |
| 패턴별 분리 | `questions/pick/array.json` 등 | 문항 30개 이상이면 분리 후 manifest에서 병합 |
| 단일 문항 | `questions/pick/pick_arr_001.json` | 스테이지 단위 lazy load 시 ([13-tech-architecture](13-tech-architecture.md) §5) |

**ID 규칙**: `^(pick|blank|scenario)_[a-z0-9_]+$` — 예: `pick_hash_002`, `blank_tp_003`

### Blank `language` (다언어)

| 값 | 용도 |
|----|------|
| `python` | 기본·fallback 풀 (최소 30문항 권장) |
| `java`, `javascript` | 각 8문항 이상 권장 |
| `c`, `go` | 각 2문항 이상 (MVP 최소) |
| `typescript`, `kotlin` | UI 선택 가능; 풀 부족 시 Python으로 fallback |

- `codeTemplate`·`blanks[].choices`는 **해당 언어 문법**으로 작성한다.
- 앱/웹 Daily·스테이지는 `GuestProgress.preferredCodeLanguage`(또는 웹 `algofit:preferredCodeLanguage`)로 Blank만 필터한다.
- 확장 스크립트: `content/scripts/expand_questions.py` 실행 후 `apps/mobile/assets/data`, `apps/web/src/content`에 동기된다.

---

## 2. Pick 문항 작성

### 지문 (`stem`)

- 한국어 1~3문장. **상황 + 제약**(정렬 여부, 시간·메모리 목표)만 명시.
- “어떤 알고리즘/패턴이 적절한가?” 형태로 끝낸다.
- 코드 블록·수식은 넣지 않는다 (Blank와 역할 분리).

### 선택지 (`choices`) — **함정 설계 규칙**

- **3~4개**. `id`는 `c1`~`c4` 고정 권장.
- 정답 1개 + **그럴듯한 함정** 2~3개.

**좋은 함정은 "비슷한 다른 패턴"**입니다. 다음 중 하나여야 합니다:

| 유형 | 예 (정답: 슬라이딩 윈도우) |
|------|--------------------------|
| 정답이지만 더 무거움 | "누적합 + 이분 탐색" (O(n log n)) |
| 같은 도메인 다른 알고리즘 | "분할 정복으로 최대 부분합" (다른 문제) |
| 살짝 다른 전제일 때만 맞음 | "정렬 후 양끝 투 포인터" (연속 구간 정보 파괴) |

**나쁜 함정** (피해야 할 패턴):
- ❌ "BFS로 격자 최단 경로" (문제와 완전 무관 — 키워드만 보고 거르게 됨)
- ❌ "스택으로 괄호 짝 검사" (도메인이 달라 학습자가 진지하게 고려하지 않음)
- ❌ "해시로 빈도만" (현재 문제와 연결고리 없음)

함정이 무관할수록 문제는 **용어 매칭 퀴즈**가 되고 진짜 패턴 인식 훈련이 안 됩니다. 함정마다 "왜 이게 안 되는가/덜 좋은가"를 학습자가 30초 안에 떠올릴 수 있어야 합니다.

### 해설 (`explanation`)

3문장 권장 — `02-core-learning-loop.md`의 피드백 작성 규칙 4번과 정렬:

1. **패턴 이름과 한 줄 근거**: "X는 ...이기 때문에 맞습니다."
2. **가장 헷갈리는 오답 1개를 짚기**: "Y도 정답을 주지만 ...라서 더 무겁습니다." (또는 "...라서 틀립니다.")
3. (옵션) 복잡도·전제·일반화 한 줄.

예시 (`pick_tp_001`):
> 정렬된 배열의 두 수 합은 양끝 투 포인터로 O(n) 시간 + O(1) 공간이 가장 깔끔합니다. **해시 맵도 정답을 주지만 정렬 정보를 버리고 O(n) 공간을 추가로 씁니다.** 이분 탐색은 O(n log n)이라 투 포인터보다 느립니다.

### 메타

| 필드 | 가이드 |
|------|--------|
| `tags` | MVP 6종: `array`, `two_pointer`, `hash`, `binary_search`, `stack`, `bfs` |
| `difficulty` | 1=신호 명확, 2=두 패턴 경쟁, 3=제약 해석 필요 |
| `language` | MVP `"python"` 고정 |

---

## 3. Blank 문항 작성

### 지문 (`stem`)

- Pick과 동일하게 한국어로 **무엇을 채우는 코드인지** 한 줄로 안내.

### 코드 (`codeTemplate`)

- **Python**만. 5~15줄, 함수 1개 권장.
- 빈칸은 `{{b1}}`, `{{b2}}` — `blanks[].id`와 일치.
- 들여쓰기 4칸, `\n` 이스케이프로 JSON에 저장.

### 빈칸 (`blanks`)

- 1~3개. 각 슬롯:
  - `correctAnswers`: 허용 표현 배열 (공백 trim 후 비교)
  - `choices`: 정답 + 오답 **3~6개**, 반드시 모든 `correctAnswers` 포함

### 흔한 실수

- `while {{b1}}`에 넣을 조건과 `blanks`의 선택지 문법 불일치
- `left = mid` vs `left = mid + 1` — 해설에 off-by-one 이유 명시

---

## 4. 실전 시나리오 (`scenario_map`)

상세 철학·카테고리·톤은 [12-real-world-scenarios.md](12-real-world-scenarios.md) § 콘텐츠 제작 가이드.

| 항목 | 요약 |
|------|------|
| 지문 | 3~6문장, 역할·목표·제약, 가벼운 상황극 |
| `patternChoices` | 4~6개, `patternTag`는 `tags`와 동일 체계 |
| `primaryPatternIds` | MVP 정답 1개 (`id` 배열 길이 1) |
| `scenarioCategory` | `logistics`, `matching`, `search_filter` 등 8종 중 택1 |
| 금지 | 실제 회사명·기출 문구 복제 |

`scenario.json`은 Pick/Blank 풀이 20문항 이상 쌓인 뒤 추가해도 된다.

---

## 5. QA 체크리스트 (제출 전)

### 공통

- [ ] `id` 전역 유일, regex 통과
- [ ] `version` ≥ 1, 필수 필드 누락 없음 ([06-content-schema](06-content-schema.md))
- [ ] 지문·선택지·해설 **한국어**, 필드명 **영문**
- [ ] `tags`가 World/Algorithm 커리큘럼과 맞음 ([07-curriculum-world-1](07-curriculum-world-1.md))
- [ ] 60~90초 안에 읽고 답할 수 있음

### Pick

- [ ] `correctChoiceId` ∈ `choices[].id`
- [ ] 선택지 3~4개, 정답이 하나로만 해석됨
- [ ] 해설에 “왜 다른 선택지는 애매한지” 1문장 이상

### Blank

- [ ] `codeTemplate`의 모든 `{{bx}}`에 대응 `blanks[].id` 존재
- [ ] 각 blank의 `choices`에 `correctAnswers` 전부 포함
- [ ] 코드가 15줄 이하, 실행 없이 읽기만으로도 풀 수 있음

### scenario_map

- [ ] `primaryPatternIds` ⊆ `patternChoices[].id`
- [ ] 정답 choice의 `patternTag`가 문항 `tags`와 일치
- [ ] 특정 서비스·코테 문구 미사용

### 번들·스테이지 연결

- [ ] `worlds/*.json`의 `questionIds`가 실제 `id`를 가리킴
- [ ] Daily manifest에 같은 날 중복 `id` 없음

---

## 6. 클라이언트 연동 (예정)

이 저장소의 `content/questions/`는 **단일 소스**입니다. 구현 시 각 앱에서 아래 경로로 가져옵니다.

| 클라이언트 | 예상 경로 | 방식 |
|------------|-----------|------|
| PC 웹 (`algofit-web`) | `import` / `import.meta.glob` from `content/questions/*.json` | Vite 빌드 시 번들 ([13-tech-architecture](13-tech-architecture.md) §5) |
| 모바일 (`algofit-mobile`) | `assets/data/questions/` 또는 git submodule 동기화 | Flutter `rootBundle` / 빌드 스크립트 복사 |

모노레포 `algorithm-training`을 쓰는 경우 `content/`를 루트에 두고 `apps/web`·`apps/mobile` 빌드 단계에서 동일 JSON을 복사하면 됩니다. **지금은 docs 저장소에만 두어도 되며**, 앱 저장소는 릴리스 시점에 sync합니다.

---

## 7. 작업 흐름 (권장)

1. 스프레드시트 또는 [08-sample-questions](08-sample-questions.md) 형식으로 초안
2. `pick.json` / `blank.json`에 JSON 반영
3. 로컬에서 `jq` 또는 스키마 검증 스크립트 실행 (CI 추가 예정)
4. PR에서 QA 체크리스트 코멘트로 자체 검수
5. `worlds`·`daily` manifest에 `questionIds` 연결

---

## 관련 문서

| 문서 | 용도 |
|------|------|
| [06-content-schema.md](06-content-schema.md) | 필드 정의·검증 규칙 |
| [08-sample-questions.md](08-sample-questions.md) | 전체 필드 예시 |
| [12-real-world-scenarios.md](12-real-world-scenarios.md) | scenario_map 전용 |
| [03-content-types.md](03-content-types.md) | 모드별 UX·문항 수 목표 |
