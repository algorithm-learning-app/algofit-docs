# MVP 범위

## 구현 현황 (2026-05-19)

| # | Must 항목 | 상태 | 비고 |
|---|-----------|------|------|
| 1 | World 1 스테이지 4–7+ 실문항·언락 | **완료** | 맵 20스테이지, 스테이지당 pick/blank 매핑 ([algofit-mobile#4](https://github.com/algorithm-learning-app/algofit-mobile/pull/4)) |
| 2 | World 2 셸 (3–5+ 스테이지) | **부분** | 5스테이지(stack/BFS), W1 7클리어 시 언락 |
| 3 | Algorithm 6종 + 진행 % | **완료** | 카탈로그·상세, `clearedQuestionIds` 기반 |
| 4 | 복습 탭 (오답 큐) | **완료** | Daily/World 오답 → `wrongQuestionIds` |
| 5 | bundled pick≥15, blank≥10 | **완료** | pick 50 / blank 30 (algofit-docs·mobile·web 동기) |
| 6 | 게스트 world·algorithm 진행 저장 | **완료** | schema v3, SharedPreferences |
| 7 | PC Daily 풀 동기·시드 | **완료** | [algofit-web#1](https://github.com/algorithm-learning-app/algofit-web/pull/1) |
| 8 | PC `/continue?token=` | **완료** | guestId ↔ localStorage 브릿지 (MVP) |
| 9 | PC 홈 모바일 핸드오프 | **완료** | guestId + continue 링크 |
| 10 | 문서·content 동기 | **완료** | `content/questions` pick 50 / blank 30 |

**미완 Must (v1.0 전)**: 뱃지 5–8, World2 10–15스테이지, 서버 동기화, `scenario_map`.

---

## Must (출시 차단 기준)

| 영역 | 내용 |
|------|------|
| 콘텐츠 | Pick ~50, Blank ~30 (6패턴) |
| 모드 | Pick, Blank, Level(World1~2), Algorithm(6), Daily |
| 실전 시나리오 | **Must 제외** — Should v1.0~1.1 (아래) |
| 게임화 | XP, 스트릭, 하트(기본), 뱃지 5~8개 |
| 계정 | 게스트 로그인 + 진행 로컬/서버 저장 |
| 언어 | Python만 (Blank 코드) |
| 플랫폼 | 모바일 우선 또는 PWA 1개 선택 (구현 문서에서 확정) |

## Should (출시 후 2~4주)

| 항목 | 설명 |
|------|------|
| **실전 시나리오 (`scenario_map`)** | 10~15문항, Learn Hub 또는 전용 탭, primary 패턴 1개 채점. World 1 말미 1~2스테이지 맛보기. 상세 [12-real-world-scenarios](12-real-world-scenarios.md) |
| 오답 복습 큐 | Algorithm 모드에서 틀린 문항만 |
| 푸시 (Daily 리마인드) | opt-in |
| World 2 스테이지 확장 | 15+ 스테이지 |
| 콘텐츠 CMS 최소 | JSON 업로드·버전 |

## v1.1 Should (시나리오 확장)

| 항목 | 설명 |
|------|------|
| 시나리오 +15문항 | 카테고리 8종, `modelingQuestion` 채점, Daily 주 2회 시나리오 1문항 |
| Algorithm 하단 “실전에 이렇게” | 알고리즘당 2~3문항 |

## Later

| 항목 | 설명 |
|------|------|
| 백준/프로그래머스 브릿지 | 외부 링크·문제 ID |
| 다국어·Java/C++ Blank | 2언어 이상 |
| 리그·랭킹 | 비목표 유지 검토 |
| 소셜·친구 | |
| 구독 (무한 하트) | [10-risks-and-metrics](10-risks-and-metrics.md) |

## 콘텐츠 수량 (Must)

| 패턴 태그 | Pick | Blank |
|-----------|------|-------|
| array | 8 | 5 |
| two_pointer | 8 | 5 |
| hash | 8 | 5 |
| binary_search | 8 | 5 |
| stack | 9 | 5 |
| bfs | 9 | 5 |
| **합계** | **~50** | **~30** |

## 월드·알고리즘 (Must)

- **World 1**: ~20 스테이지 ([07-curriculum-world-1](07-curriculum-world-1.md))
- **World 2**: 스택·큐·BFS 중심 10~15 스테이지 (개요만, 상세는 구현 후)
- **Algorithm 모드**: 6종, 종류당 문항 8~12개 혼합

## 일정 가정 (문서용, 검증 필요)

| 단계 | 기간 (가정) | 산출물 |
|------|-------------|--------|
| 문서·스키마 | 1~2주 | docs/, 샘플 JSON 80문항 설계 |
| 프로토타입 UI | 2~3주 | 핵심 루프 1플로우 |
| 콘텐츠 제작 | 3~4주 | Must 분량 JSON |
| MVP 통합 | 2~3주 | 게스트·Daily·저장 |
| **합계** | **~10~12주** (1인 파트타임이면 ×1.5~2) |

## 명시적 제외 (Out of scope)

- 온라인 IDE·코드 실행·채점
- 사용자 제출 문제·UGC
- 실시간 멀티플레이
- 강사·라이브 클래스
- ACM 수준 고난도 (세그트리, 펜윅 등)

## 완료 정의 (MVP Done)

1. 신규 사용자가 게스트로 **일일 챌린지 1회** 완료하고 스트릭이 기록된다.
2. World 1 스테이지 1→20 맵·언락 체인으로 진행이 가능하다.
3. Pick·Blank 각 1문항이 스키마대로 로드·채점된다. (`scenario_map`은 Should 완료 시 4번 항목으로 승격 가능)
4. 앱 재실행 후 XP·진행이 유지된다.

## 구현 상태 (2026-05-19)

| # | Must 항목 | 상태 | PR / 비고 |
|---|-----------|------|-----------|
| — | Daily 5문항·홈·pick/blank 풀·서울 날짜 시드 | ✅ | [algofit-mobile#2](https://github.com/algorithm-learning-app/algofit-mobile/pull/2), [#3](https://github.com/algorithm-learning-app/algofit-mobile/pull/3) |
| 1 | World 1 스테이지 4–20 (콘텐츠 매핑) | ✅ | [algofit-mobile#4](https://github.com/algorithm-learning-app/algofit-mobile/pull/4) — 맵 20스테이지, placeholder 없음 |
| 2 | World 2 최소 (3–5 스테이지) | ✅ | #4 — 5스테이지, 7클리어 시 해금 |
| 3 | Algorithm 6패턴·목록·상세·진행 % | ✅ | #4 |
| 4 | Review 탭 (세션 오답) | ✅ | #4 |
| 5 | pick.json 15+ / blank.json 10+ | 🟡 | #4 — 번들 15 pick / 11 blank (`content/questions` 동기화). Must 목표 50/30은 미달 |
| 6 | Web Daily 동일 풀·서울 시드 | ✅ | [algofit-web#1](https://github.com/algorithm-learning-app/algofit-web/pull/1) |
| 7 | Web `/continue` 토큰 handoff | ✅ | algofit-web#1 |
| 8 | `content/questions` 문항 확장 | 🟡 | [algofit-docs](https://github.com/algorithm-learning-app/algofit-docs) — 모바일 번들과 동기화(15/11), Must 50/30 전량은 후속 |
| 9 | 본 문서 구현 상태 표 | ✅ | 이 표 |

**미완 Must 후속**: 콘텐츠 50/30 전량, 게스트 서버 동기화, 뱃지 5–8개, World 2 10–15스테이지 확장(Should와 겹침).
