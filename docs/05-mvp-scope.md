# MVP 범위

## MVP Complete

| 항목 | 값 |
|------|-----|
| **완료일** | 2026-05-19 (KST) |
| **Must 표** | 아래 구현 상태 표 — 전 항목 ✅ |
| **검증** | `algofit-mobile`: `flutter analyze` · `flutter test` · `algofit-web`: `npm run build` · `npm test` · `algofit-docs`: `scripts/pr-review-check.sh` |
| **정책** | Daily 챌린지는 하트 미소모 ([04-gamification](04-gamification.md), [14-learning-flow](14-learning-flow.md)) — 2026-05-19 수정 반영 |

---

## Must (출시 차단 기준)

| 영역 | 내용 |
|------|------|
| 콘텐츠 | Pick ~50, Blank ~30 (6패턴) |
| 모드 | Pick, Blank, Level(World1~2), Algorithm(6), Daily |
| 실전 시나리오 | **Must 제외** — Should v1.0~1.1 (아래) |
| 게임화 | XP, 스트릭, 하트(기본), 뱃지 5~8개 |
| 계정 | 게스트 + 진행 **로컬** 저장 (서버 sync는 Phase 2) |
| 언어 | Python만 (Blank 코드) |
| 플랫폼 | 모바일 Flutter + PC 웹 React ([18-stack-decision](18-stack-decision.md)) |

## Should (출시 후 2~4주)

| 항목 | 설명 |
|------|------|
| **실전 시나리오 (`scenario_map`)** | 10~15문항, Learn Hub 또는 전용 탭. [12-real-world-scenarios](12-real-world-scenarios.md) |
| 게스트 진행 서버 sync | Supabase/Firebase 등 Phase 2 |
| World 2 스테이지 15+ | MVP는 10스테이지 |
| 푸시 (Daily 리마인드) | opt-in |
| 콘텐츠 CMS 최소 | JSON 업로드·버전 |

## 콘텐츠 수량 (Must)

| 패턴 태그 | Pick | Blank |
|-----------|------|-------|
| array | 8 | 5 |
| two_pointer | 8 | 5 |
| hash | 8 | 5 |
| binary_search | 8 | 5 |
| stack | 9 | 5 |
| bfs | 9 | 5 |
| **합계** | **50** | **30** |

## 월드·알고리즘 (Must)

- **World 1**: 20 스테이지 ([07-curriculum-world-1](07-curriculum-world-1.md))
- **World 2**: 스택·BFS 10 스테이지, World 1 7클리어 시 해금
- **Algorithm 모드**: 6종, `clearedQuestionIds` 기반 진행 %

## 완료 정의 (MVP Done)

1. 신규 사용자가 게스트로 **일일 챌린지 1회** 완료하고 스트릭이 기록된다.
2. World 1 스테이지 1→20 맵·언락 체인으로 진행이 가능하다.
3. Pick·Blank 각 1문항이 스키마대로 로드·채점된다.
4. 앱 재실행 후 XP·진행이 유지된다.

## 구현 상태 (2026-05-19)

| # | Must 항목 | 상태 | PR / 비고 |
|---|-----------|------|-----------|
| — | Daily 5문항·홈·pick/blank 풀·서울 날짜 시드 | ✅ | [algofit-mobile#2](https://github.com/algorithm-learning-app/algofit-mobile/pull/2), [#3](https://github.com/algorithm-learning-app/algofit-mobile/pull/3) |
| 1 | World 1 스테이지 4–20 (콘텐츠 매핑) | ✅ | [algofit-mobile#4](https://github.com/algorithm-learning-app/algofit-mobile/pull/4) |
| 2 | World 2 (10 스테이지, stack/BFS) | ✅ | 10스테이지·문항 매핑, W1 7클리어 해금 |
| 3 | Algorithm 6패턴·목록·상세·진행 % | ✅ | #4 |
| 4 | Review 탭 (세션 오답) | ✅ | #4 |
| 5 | pick 50 / blank 30 번들 | ✅ | mobile·web·`content/questions` 동기 ([algofit-web#5](https://github.com/algorithm-learning-app/algofit-web/pull/5) 등) |
| 6 | 게스트 world·algorithm 진행 로컬 저장 | ✅ | schema v4, SharedPreferences / localStorage |
| 7 | Web Daily 동일 풀·서울 시드 | ✅ | [algofit-web#1](https://github.com/algorithm-learning-app/algofit-web/pull/1) |
| 8 | Web `/continue?token=` + 홈 핸드오프 | ✅ | algofit-web#1 |
| 9 | 뱃지 8종 + 프로필(내 정보) 탭 | ✅ | `kBadges` 8개, guestId·스트릭·XP·PC 링크 복사 |
| 10 | Web `/profile` (guestId·진행) | ✅ | PC 프로필 스텁 → 실구현 |
| 11 | `content/questions` + 본 문서 | ✅ | pick 50 / blank 30, MVP Complete 표 |

**Must 미포함 (의도적)**: `scenario_map`, OAuth, 앱스토어 출시, 서버 sync.
