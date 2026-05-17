# 샘플 문항

콘텐츠 제작·QA용 **전체 필드** 예시. 스키마는 [06-content-schema.md](06-content-schema.md)를 따른다. `scenario_map` 상세·작가 가이드는 [12-real-world-scenarios.md](12-real-world-scenarios.md).

---

## Pick (5)

### pick_arr_001

| Field | Value |
|-------|-------|
| id | `pick_arr_001` |
| type | pick |
| version | 1 |
| language | python |
| tags | `["array"]` |
| difficulty | 1 |

**stem**  
길이 n인 배열에서 모든 원소를 한 번씩만 보며 최댓값을 구하려 합니다. 추가 메모리를 거의 쓰지 않으려면 어떤 접근이 가장 자연스러울까요?

**choices**

| id | label |
|----|-------|
| c1 | 배열을 한 번 순회하며 현재까지의 최댓값 갱신 |
| c2 | 배열을 정렬한 뒤 맨 앞 원소 선택 |
| c3 | 해시 테이블에 빈도를 저장 |
| c4 | BFS로 탐색 |

**correctChoiceId**: `c1`

**explanation**  
최댓값은 전 원소를 한 번 훑으며 `max`를 갱신하면 O(n)으로 구할 수 있습니다. 정렬은 O(n log n)으로 더 무겁고, 해시·BFS는 이 문제의 요구와 맞지 않습니다.

---

### pick_tp_001

| Field | Value |
|-------|-------|
| id | `pick_tp_001` |
| type | pick |
| version | 1 |
| language | python |
| tags | `["two_pointer"]` |
| difficulty | 2 |

**stem**  
**오름차순으로 정렬된** 배열에서 두 수의 합이 `target`이 되는 **서로 다른 두 인덱스**를 찾습니다. 시간을 줄이려면 보통 어떤 방법을 먼저 떠올리나요?

**choices**

| id | label |
|----|-------|
| c1 | 투 포인터 (왼쪽·오른쪽 끝에서 좁히기) |
| c2 | 이분 탐색만 단독으로 |
| c3 | 스택으로 중위 표현식 |
| c4 | BFS 레벨 순회 |

**correctChoiceId**: `c1`

**explanation**  
정렬된 배열의 두 수 합은 양끝 포인터를 움직이며 합을 비교하는 투 포인터가 전형적입니다. 이분 탐색은 “한 수 고정 후 나머지”에 쓸 수는 있지만, 이 지문의 첫 패턴은 투 포인터입니다.

---

### pick_hash_001

| Field | Value |
|-------|-------|
| id | `pick_hash_001` |
| type | pick |
| version | 1 |
| language | python |
| tags | `["hash"]` |
| difficulty | 2 |

**stem**  
정렬되지 않은 배열에서 `target = a[i] + a[j]`인 **인덱스 한 쌍**을 O(n)에 가깝게 찾고 싶습니다. 보조 자료구조로 무엇이 적절할까요?

**choices**

| id | label |
|----|-------|
| c1 | 해시 테이블 (값 → 인덱스) |
| c2 | 스택 |
| c3 | 큐만 사용한 BFS |
| c4 | 세그먼트 트리 |

**correctChoiceId**: `c1`

**explanation**  
순회하며 `target - nums[i]`가 이미 해시에 있는지 보면 평균 O(n)입니다. 정렬되지 않았으므로 투 포인터 전제가 없고, 스택·BFS는 부적합합니다.

---

### pick_bs_001

| Field | Value |
|-------|-------|
| id | `pick_bs_001` |
| type | pick |
| version | 1 |
| language | python |
| tags | `["binary_search"]` |
| difficulty | 1 |

**stem**  
이미 **오름차순 정렬된** 배열 `nums`에서 값 `x`가 있는지 **존재 여부만** 빠르게 확인하려 합니다. 가장 적절한 알고리즘은?

**choices**

| id | label |
|----|-------|
| c1 | 이분 탐색 |
| c2 | 해시로 빈도만 세기 |
| c3 | 스택으로 괄호 검사 |
| c4 | 완전 탐색만 가능 (이분 불가) |

**correctChoiceId**: `c1`

**explanation**  
정렬된 배열에서 값 하나를 찾는 기본 도구는 이분 탐색 O(log n)입니다. 존재 여부만 필요해도 동일합니다.

---

### pick_bfs_001

| Field | Value |
|-------|-------|
| id | `pick_bfs_001` |
| type | pick |
| version | 1 |
| language | python |
| tags | `["bfs"]` |
| difficulty | 2 |

**stem**  
2차원 격자에서 **시작 칸에서 목표 칸까지의 최소 칸 수**(4방향, 벽 `#`)를 구합니다. 가장 먼저 시도할 탐색 방법은?

**choices**

| id | label |
|----|-------|
| c1 | BFS (너비 우선) |
| c2 | 배열 이분 탐색 |
| c3 | 투 포인터만 |
| c4 | 스택으로만 DFS 없이 해결 |

**correctChoiceId**: `c1`

**explanation**  
가중치 없는 그래프/격자에서 **최단 거리(칸 수)** 는 BFS가 표준입니다. 이분·투 포인터는 격자 최단거리와 무관합니다.

---

## Blank (5)

### blank_tp_001

| Field | Value |
|-------|-------|
| id | `blank_tp_001` |
| type | blank |
| version | 1 |
| language | python |
| tags | `["two_pointer"]` |
| difficulty | 2 |

**stem**  
정렬된 배열 `nums`에서 두 수의 합이 `target`이 되는 두 인덱스를 반환합니다 (정확히 하나 존재). 빈칸을 채우세요.

**codeTemplate**

```python
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while {{b1}}:
        s = nums[left] + nums[right]
        if s == target:
            return [left, right]
        elif s < target:
            {{b2}}
        else:
            right -= 1
    return []
```

**blanks**

| id | correctAnswers | choices |
|----|----------------|---------|
| b1 | `left < right` | `left < right`, `left <= right`, `left != right`, `left > right` |
| b2 | `left += 1` | `left += 1`, `left -= 1`, `right += 1`, `left = right` |

**explanation**  
합이 작으면 더 큰 값이 필요하므로 `left`를 오른쪽으로 옮깁니다. `while left < right`로 같은 인덱스를 쓰지 않습니다.

---

### blank_hash_001

| Field | Value |
|-------|-------|
| id | `blank_hash_001` |
| type | blank |
| version | 1 |
| language | python |
| tags | `["hash"]` |
| difficulty | 2 |

**stem**  
정렬되지 않은 배열에서 두 수의 합이 `target`인 인덱스를 찾습니다. 빈칸을 채우세요.

**codeTemplate**

```python
def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        need = {{b1}}
        if need in seen:
            return [seen[need], i]
        {{b2}}
    return []
```

**blanks**

| id | correctAnswers | choices |
|----|----------------|---------|
| b1 | `target - x` | `target - x`, `target + x`, `x - target`, `x + target` |
| b2 | `seen[x] = i` | `seen[x] = i`, `seen[i] = x`, `seen.append(x)`, `seen.add(i)` |

**explanation**  
현재 값 `x`에 필요한 보수는 `target - x`입니다. 나중에 찾기 위해 현재 값과 인덱스를 해시에 저장합니다.

---

### blank_bs_001

| Field | Value |
|-------|-------|
| id | `blank_bs_001` |
| type | blank |
| version | 1 |
| language | python |
| tags | `["binary_search"]` |
| difficulty | 2 |

**stem**  
정렬된 `nums`에서 `target`의 인덱스를 반환하고, 없으면 -1을 반환합니다.

**codeTemplate**

```python
def search(nums, target):
    left, right = 0, len(nums) - 1
    while {{b1}}:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            {{b2}}
        else:
            right = mid - 1
    return -1
```

**blanks**

| id | correctAnswers | choices |
|----|----------------|---------|
| b1 | `left <= right` | `left <= right`, `left < right`, `left != right`, `mid <= right` |
| b2 | `left = mid + 1` | `left = mid + 1`, `left = mid`, `right = mid + 1`, `left = mid - 1` |

**explanation**  
구간을 유지하려면 `left <= right`입니다. `target`이 더 크면 왼쪽 절반을 버리고 `left = mid + 1`입니다.

---

### blank_stack_001

| Field | Value |
|-------|-------|
| id | `blank_stack_001` |
| type | blank |
| version | 1 |
| language | python |
| tags | `["stack"]` |
| difficulty | 2 |

**stem**  
괄호 문자열 `s`가 올바른지 검사합니다. `()` `[]` `{}` 만 허용.

**codeTemplate**

```python
def is_valid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in '([{':
            {{b1}}
        elif ch in ')]}':
            if not stack or {{b2}}:
                return False
            stack.pop()
    return not stack
```

**blanks**

| id | correctAnswers | choices |
|----|----------------|---------|
| b1 | `stack.append(ch)` | `stack.append(ch)`, `stack.pop()`, `stack[0] = ch`, `return False` |
| b2 | `stack[-1] != pairs[ch]` | `stack[-1] != pairs[ch]`, `stack[0] != pairs[ch]`, `ch not in pairs`, `len(stack) == 0` |

**explanation**  
여는 괄호는 스택에 push하고, 닫는 괄호는 top이 짝이 맞는지 확인한 뒤 pop합니다.

---

### blank_bfs_001

| Field | Value |
|-------|-------|
| id | `blank_bfs_001` |
| type | blank |
| version | 1 |
| language | python |
| tags | `["bfs"]` |
| difficulty | 3 |

**stem**  
`grid`에서 `0`은 빈 칸, `1`은 벽입니다. `(sr, sc)`에서 `(tr, tc)`까지의 **최소 이동 칸 수**를 구합니다 (도달 불가 시 -1).

**codeTemplate**

```python
from collections import deque

def shortest_path(grid, sr, sc, tr, tc):
    rows, cols = len(grid), len(grid[0])
    q = deque([(sr, sc, 0)])
    visited = {(sr, sc)}
    while q:
        r, c, dist = q.popleft()
        if (r, c) == (tr, tc):
            return dist
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                {{b1}}
                {{b2}}
    return -1
```

**blanks**

| id | correctAnswers | choices |
|----|----------------|---------|
| b1 | `visited.add((nr, nc))` | `visited.add((nr, nc))`, `visited.add((r, c))`, `grid[nr][nc] = 1`, `q.clear()` |
| b2 | `q.append((nr, nc, dist + 1))` | `q.append((nr, nc, dist + 1))`, `q.appendleft((nr, nc, dist))`, `q.pop()`, `return dist + 1` |

**explanation**  
BFS는 큐에서 꺼내며 거리를 1씩 늘립니다. 방문 표시 후 같은 거리 레벨이 큐에 들어가도록 append합니다.

---

## Scenario map (3)

### scenario_logistics_001

| Field | Value |
|-------|-------|
| id | `scenario_logistics_001` |
| type | scenario_map |
| version | 1 |
| language | python |
| scenarioCategory | `logistics` |
| tags | `["bfs"]` |
| difficulty | 2 |
| tone | playful |

**stem**  
배달 플랫폼이 라이더 민수에게 픽업 지점 여러 곳을 한 번에 돌게 합니다. 도시는 **격자**이고, 벽 칸은 지날 수 없습니다. 모든 픽업을 거친 뒤 허브로 돌아올 때 **총 이동 칸 수**를 최소로 잡고 싶습니다. (지점 수는 작고, 이동은 상하좌우만 가능)

**patternChoices**

| id | label | patternTag |
|----|-------|------------|
| p1 | BFS로 격자에서 최소 칸 수 탐색 | bfs |
| p2 | 정렬된 배열에서 이분 탐색만 | binary_search |
| p3 | 해시로 “본 메뉴”만 기록 | hash |
| p4 | 스택으로 괄호 짝 검사 | stack |

**primaryPatternIds**: `["p1"]`

**modelingQuestion.stem**  
구현 전, 이 상황을 가장 먼저 무엇으로 놓는 게 자연스러울까요?

| id | label (modeling choices) |
|----|--------------------------|
| m1 | 격자/지점 그래프 (칸·이동) |
| m2 | 정렬된 1차원 배열만 |
| m3 | 문자열 괄호 스택 |
| m4 | 단일 정수 변수만 |

**modelingQuestion.correctChoiceId**: `m1`

**explanation**  
“칸 수 최소·격자·상하좌우”는 가중치 없는 그래프에서의 **최단 거리** 신호이므로 BFS가 먼저 떠올려집니다. 이분·해시·스택은 다른 제약에서 쓰입니다. 먼저 지점을 그래프/격자로 모델링하세요.

---

### scenario_matching_001

| Field | Value |
|-------|-------|
| id | `scenario_matching_001` |
| type | scenario_map |
| version | 1 |
| language | python |
| scenarioCategory | `matching` |
| tags | `["hash"]` |
| difficulty | 2 |
| tone | playful |

**stem**  
점심 메뉴 앱이 사용자에게 **아직 안 본 메뉴**만 추천하려 합니다. 메뉴 id는 수십만 개이고, “최근 7일에 본 id” 목록이 실시간으로 들어옵니다. 매 요청마다 **이미 본 메뉴인지** 빠르게 판별해야 합니다. (정렬된 전체 목록을 매번 훑는 것은 느리다고 가정)

**patternChoices**

| id | label | patternTag |
|----|-------|------------|
| p1 | 해시 집합/맵으로 id 존재 여부 O(1) 조회 | hash |
| p2 | 정렬된 배열 + 투 포인터로만 처리 | two_pointer |
| p3 | BFS로 메뉴 그래프 탐색 | bfs |
| p4 | 스택으로 최근 호출 취소 | stack |

**primaryPatternIds**: `["p1"]`

**modelingQuestion** — (MVP 생략 가능)

**explanation**  
“id 존재 여부를 빠르게”는 **해시** 전형입니다. 정렬+투 포인터는 정렬된 배열의 쌍·구간 문제에 가깝고, BFS·스택은 이 제약과 맞지 않습니다.

---

### scenario_limits_001

| Field | Value |
|-------|-------|
| id | `scenario_limits_001` |
| type | scenario_map |
| version | 1 |
| language | python |
| scenarioCategory | `limits_security` |
| tags | `["hash"]` |
| difficulty | 3 |
| tone | playful |

**stem**  
공개 API 게이트웨이는 **사용자 id마다 1분에 최대 100번**만 호출을 허용합니다. 요청이 들어올 때마다 “지금 이 분 창에서 몇 번 썼는지”를 보고, 초과면 429를 돌려줍니다. (사용자 수는 많고, 창은 1분 단위로 슬라이드)

**patternChoices**

| id | label | patternTag |
|----|-------|------------|
| p1 | 사용자 id → (분 단위 타임스탬프, 카운트) 해시 + 창 갱신 | hash |
| p2 | 전체 로그를 정렬한 뒤 이분 탐색만 | binary_search |
| p3 | 격자 최단 경로 BFS | bfs |
| p4 | 배열 한 번 순회로 최댓값만 | array |

**primaryPatternIds**: `["p1"]`

**modelingQuestion.stem**  
“1분 창” 제약을 코드로 옮길 때, 가장 먼저 떠올릴 **자료 구조 묶음**은?

| id | label |
|----|-------|
| m1 | id별 해시 + 시간(분) 키 |
| m2 | 정렬된 2차원 격자만 |
| m3 | 스택 하나 |
| m4 | 연결 리스트만 (탐색 없음) |

**modelingQuestion.correctChoiceId**: `m1`

**explanation**  
사용자별 **빈도·시간 창**은 id를 키로 하는 해시에 분 단위 카운트를 두는 패턴이 일반적입니다 (슬라이딩 윈도우는 hash+시간으로 확장). 이분·BFS·단순 배열 스캔은 “분당 N회” 제한과 잘 맞지 않습니다.

---

## JSON 일괄 (pick_arr_001)

```json
{
  "id": "pick_arr_001",
  "type": "pick",
  "version": 1,
  "language": "python",
  "stem": "길이 n인 배열에서 모든 원소를 한 번씩만 보며 최댓값을 구하려 합니다. 추가 메모리를 거의 쓰지 않으려면 어떤 접근이 가장 자연스러울까요?",
  "tags": ["array"],
  "difficulty": 1,
  "choices": [
    { "id": "c1", "label": "배열을 한 번 순회하며 현재까지의 최댓값 갱신" },
    { "id": "c2", "label": "배열을 정렬한 뒤 맨 앞 원소 선택" },
    { "id": "c3", "label": "해시 테이블에 빈도를 저장" },
    { "id": "c4", "label": "BFS로 탐색" }
  ],
  "correctChoiceId": "c1",
  "explanation": "최댓값은 전 원소를 한 번 훑으며 max를 갱신하면 O(n)으로 구할 수 있습니다. 정렬은 O(n log n)으로 더 무겁고, 해시·BFS는 이 문제의 요구와 맞지 않습니다."
}
```

나머지 Pick/Blank 9문항과 Scenario 3문항도 동일 스키마로 `content/questions/`에 JSON 파일로 내면 된다.

### JSON 일괄 (scenario_logistics_001)

```json
{
  "id": "scenario_logistics_001",
  "type": "scenario_map",
  "version": 1,
  "language": "python",
  "stem": "배달 플랫폼이 라이더 민수에게 픽업 지점 여러 곳을 한 번에 돌게 합니다. 도시는 격자이고, 벽 칸은 지날 수 없습니다. 모든 픽업을 거친 뒤 허브로 돌아올 때 총 이동 칸 수를 최소로 잡고 싶습니다. (지점 수는 작고, 이동은 상하좌우만 가능)",
  "scenarioCategory": "logistics",
  "tags": ["bfs"],
  "difficulty": 2,
  "tone": "playful",
  "patternChoices": [
    { "id": "p1", "label": "BFS로 격자에서 최소 칸 수 탐색", "patternTag": "bfs" },
    { "id": "p2", "label": "정렬된 배열에서 이분 탐색만", "patternTag": "binary_search" },
    { "id": "p3", "label": "해시로 본 메뉴만 기록", "patternTag": "hash" },
    { "id": "p4", "label": "스택으로 괄호 짝 검사", "patternTag": "stack" }
  ],
  "primaryPatternIds": ["p1"],
  "modelingQuestion": {
    "stem": "구현 전, 이 상황을 가장 먼저 무엇으로 놓는 게 자연스러울까요?",
    "choices": [
      { "id": "m1", "label": "격자/지점 그래프 (칸·이동)" },
      { "id": "m2", "label": "정렬된 1차원 배열만" },
      { "id": "m3", "label": "문자열 괄호 스택" },
      { "id": "m4", "label": "단일 정수 변수만" }
    ],
    "correctChoiceId": "m1"
  },
  "explanation": "칸 수 최소·격자·상하좌우는 BFS 신호입니다. 먼저 지점을 그래프/격자로 모델링한 뒤 탐색 패턴을 고르세요."
}
```
