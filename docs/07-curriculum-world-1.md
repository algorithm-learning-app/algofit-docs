# World 1 커리큘럼

**테마**: 배열 기초 → 투 포인터 → 해시 → 이분 탐색 입문  
**스테이지 수**: 20  
**스테이지당**: Pick 1~2 + Blank 0~1 (세션 3~4문항)

## 패턴 태그

`array`, `two_pointer`, `hash`, `binary_search` (World 1), `stack`·`bfs`는 World 2

---

## 스테이지 목록

| Stage | 제목 | 문항 구성 (타입) | pattern tags | 학습 포인트 |
|-------|------|------------------|--------------|-------------|
| 1-1 | 배열이 뭐죠? | pick×2 | array | 인덱스, 순회 |
| 1-2 | 합구하기 입문 | pick + blank | array | 누적합 개념 |
| 1-3 | 최댓값 찾기 | pick×2 | array | 선형 스캔 |
| 1-4 | 두 수의 합 (브루트 소개) | pick | array | 완탐 vs 개선 필요 |
| 1-5 | 정렬된 배열과 투 포인터 | pick | two_pointer | 양끝 포인터 |
| 1-6 | 투 포인터 코드 | blank | two_pointer | `while left < right` |
| 1-7 | 부분 배열 합 | pick | two_pointer | 윈도우 맛보기 |
| 1-8 | 투 포인터 복습 | pick×2 | two_pointer | 중복 제거 패턴 |
| 1-9 | 해시가 필요해요 | pick | hash | O(1) lookup |
| 1-10 | 두 수의 합 (해시) | blank | hash | `dict`, complement |
| 1-11 | 빈도 세기 | pick | hash | Counter 개념 |
| 1-12 | 해시 복습 | pick + blank | hash | |
| 1-13 | 이분 탐색이란 | pick | binary_search | 정렬 전제 |
| 1-14 | 이분 탐색 코드 | blank | binary_search | left/right/mid |
| 1-15 | lower bound 맛보기 | pick | binary_search | 경계 |
| 1-16 | 배열 + 이분 조합 | pick×2 | binary_search, array | |
| 1-17 | World 1 중간 보스 | pick×2 + blank | mixed w1 | 정확도 80% 권장 |
| 1-17b | **실전 맛보기: 메뉴·주문** (Should) | scenario_map×1 | hash | 서비스 지문 → 해시 신호 ([12-real-world-scenarios](12-real-world-scenarios.md)) |
| 1-18 | 약한 패턴 보충 | pick (오답 태그) | adaptive | Should: 오답 기반 |
| 1-19 | 속도 훈련 | pick×3 | mixed w1 | 시간 표시만 |
| 1-19b | **실전 맛보기: 검색·필터** (Should) | scenario_map×1 | binary_search, array | 정렬·경계 신호 |
| 1-20 | World 1 클리어 | pick×2 + blank (+ scenario_map×1 Should) | mixed w1 | 뱃지 `world1_clear` |

---

## 난이도 곡선

- 1-1 ~ 1-4: difficulty 1 only  
- 1-5 ~ 1-12: difficulty 1~2  
- 1-13 ~ 1-20: difficulty 2, 1-17·1-20에 3 일부  

## World 1 클리어 조건 (MVP)

- 1-20 클리어 **또는** 1-1~1-19 별 합계 18개 이상 (정책 택1, 구현 시 하나로 고정)

## World 2 개요 (Must 요약만)

| 구간 | 태그 | 스테이지 수 |
|------|------|-------------|
| 2-1 ~ 2-8 | stack | 8 |
| 2-9 ~ 2-15 | bfs | 7 |

**실전 시나리오 비중**은 World 2에서 확대한다 (스택·BFS·경로·큐 맥락). World 1은 Should 시 1-17b·1-19b·1-20에 총 2~3문항 맛보기만.

상세 스테이지 표는 World 1 안정화 후 동일 형식으로 추가.

## questionId 매핑

실제 `questionIds`는 콘텐츠 제작 시 [08-sample-questions](08-sample-questions.md) 및 Must 50/30 풀에서 할당한다. 스테이지 JSON 예:

```json
{
  "id": "stage_w1_06",
  "order": 6,
  "title": "투 포인터 코드",
  "questionIds": ["blank_tp_001", "pick_tp_002"],
  "tags": ["two_pointer"]
}
```
