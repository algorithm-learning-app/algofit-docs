# 용어집

앱 UI·해설에서 쓰는 알고리즘·패턴 용어. 정의는 **한 줄** 학습자용.

| 용어 (KO) | English | 정의 |
|-----------|---------|------|
| 배열 | array | 같은 타입 원소가 연속된 인덱스 자료구조 |
| 인덱스 | index | 배열에서 원소 위치 (0부터) |
| 투 포인터 | two-pointer | 배열 양끝 또는 두 인덱스를 조절하며 조건을 만족시키는 기법 |
| 슬라이딩 윈도우 | sliding window | 고정·가변 길이 구간을 이동하며 합/조건을 갱신 |
| 해시 테이블 | hash table | 키→값 O(1) 평균 조회, 보수(complement) 찾기에 사용 |
| 빈도수 | frequency | 원소가 나온 횟수; 해시로 집계 |
| 이분 탐색 | binary search | **정렬된** 배열에서 중간을 보며 범위를 반으로 줄임 |
| lower bound | lower bound | 정렬 배열에서 `target` 이상인 첫 위치 |
| 스택 | stack | LIFO; push/pop은 맨 위만 |
| 큐 | queue | FIFO; 들어온 순서대로 처리 |
| BFS | breadth-first search | 그래프/트리를 **너비** 우선, 큐로 층별 탐색 |
| DFS | depth-first search | 깊이 우선; 스택 또는 재귀 (MVP 해설용) |
| 방문 처리 | visited | 이미 본 노드/칸을 표시해 중복 방문 방지 |
| 인접 리스트 | adjacency list | 노드별 이웃 목록; 그래프 표현 |
| 시간 복잡도 | time complexity | 입력 크기 n에 따른 연산 증가율 (Big-O) |
| O(n) | linear | n에 비례 |
| O(log n) | logarithmic | 이분 탐색 등 |
| 완전 탐색 | brute force | 모든 경우를 다 시도 |
| 누적합 | prefix sum | `prefix[i]` = 앞 i개의 합 |
| 정렬 | sorting | 순서대로 재배열; 이분 탐색 전제 |
| 패턴 | pattern | 반복되는 문제 유형·풀이 골격 |
| 스켈레톤 코드 | skeleton code | 빈칸이 있는 전형 코드 틀 |
| 스트릭 | streak | 연속으로 일일 챌린지를 완료한 일수 |
| 스테이지 | stage | 월드 맵上的 한 단위 학습 묶음 |
| 시나리오 | scenario | 서비스·업무 맥락이 담긴 짧은 상황 지문 (`scenario_map`) |
| 실전 시나리오 | scenario map mode | 현실 문제 매핑 모드 UI명; 지문 → 패턴 선택 |
| 현실 문제 | real-world (problem) | 코테에서 도메인 말이 섞인 지문 유형 (기출 암기 아님) |
| 도메인 모델링 | domain modeling | 상황을 배열·그래프·해시 등 **자료구조/관점**으로 바꾸는 1차 단계 |
| 패턴 매핑 | pattern mapping | 시나리오 제약을 읽고 알고리즘 태그에 연결하는 행위 |
| 시나리오 카테고리 | scenario category | `logistics`, `matching` 등 분류 ([12-real-world-scenarios](12-real-world-scenarios.md)) |
| primary 패턴 | primary pattern | 시나리오 문항에서 반드시 맞혀야 하는 대표 정답 choice |

### UI에서 영문 표기

- Algorithm 모드 카드: **한글 제목 + 영문 부제** (예: `이분 탐색 · Binary Search`)
- 코드·태그: 영문 snake_case (`binary_search`)

### World 1에서 다루지 않는 용어 (Later)

세그먼트 트리, 펜윅, 최소 비용 흐름, 강한 연결 요소 등 — 용어집 v2에서 추가.
