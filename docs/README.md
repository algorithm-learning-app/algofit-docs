# 문서 인덱스

알고리즘 패턴 학습 앱의 기획·콘텐츠·UX 스펙입니다. 구현 전 이 폴더를 기준으로 작업합니다.

## 제품·학습

| 문서 | 한 줄 설명 |
|------|------------|
| [01-product-vision.md](01-product-vision.md) | 비전, 타깃, 백준/프로그래머스와의 차별, 성공 지표 |
| [02-core-learning-loop.md](02-core-learning-loop.md) | 3~5분 세션 흐름, 재미 원칙, 즉시 피드백 규칙 |
| [03-content-types.md](03-content-types.md) | Pick·Blank·Level·Algorithm·Daily·**실전 시나리오** 모드 스펙 |
| [12-real-world-scenarios.md](12-real-world-scenarios.md) | 현실 문제 매핑 철학, 카테고리, 작가 가이드, 패턴 치트시트 |
| [04-gamification.md](04-gamification.md) | XP·스트릭·하트·뱃지 — MVP vs 이후 |
| [05-mvp-scope.md](05-mvp-scope.md) | Must/Should/Later, 일정 가정, 제외 범위 |

## 콘텐츠·데이터

| 문서 | 한 줄 설명 |
|------|------------|
| [06-content-schema.md](06-content-schema.md) | Pick/Blank/**scenario_map** JSON 스키마 및 예시 (필드명 영문) |
| [07-curriculum-world-1.md](07-curriculum-world-1.md) | World 1 스테이지 ~20개, 패턴 태그 |
| [08-sample-questions.md](08-sample-questions.md) | 샘플 Pick 5 + Blank 5 + Scenario 3 (전체 필드) |

## UX·운영

| 문서 | 한 줄 설명 |
|------|------------|
| [09-ia-screens.md](09-ia-screens.md) | 화면 목록, 내비게이션, 온보딩 |
| [10-risks-and-metrics.md](10-risks-and-metrics.md) | 리스크, 북극성 지표, 수익 방향 |
| [11-glossary.md](11-glossary.md) | 앱에서 쓰는 알고리즘·패턴 용어집 |

## 구현

| 문서 | 한 줄 설명 |
|------|------------|
| [13-tech-architecture.md](13-tech-architecture.md) | Flutter+React PC, 모노레포, 콘텐츠·백엔드, Daily·스트릭 |
| [17-dev-setup.md](17-dev-setup.md) | 로컬 실행 (Flutter / Vite), Figma 참고 |
| [18-stack-decision.md](18-stack-decision.md) | ADR: 모바일 Flutter vs PC React 분리 (2026-05-17) |

## 제품 확정 · 디자인

| 문서 | 한 줄 설명 |
|------|------------|
| [14-learning-flow.md](14-learning-flow.md) | 알고핏·플랫폼 B·5/5 스트릭·PC 보너스·게임 톤 (협의 확정) |
| [15-figma-mcp-setup.md](15-figma-mcp-setup.md) | Cursor ↔ Figma MCP (Remote 권장, Desktop·레거시 대안) |
| [16-algofit-figma-brief.md](16-algofit-figma-brief.md) | Figma 토큰·프레임·컴포넌트·마스코트 배치 브리프 |

## 읽는 순서 (신규 개발자)

1. [01-product-vision](01-product-vision.md) → [02-core-learning-loop](02-core-learning-loop.md)
2. [05-mvp-scope](05-mvp-scope.md) → [03-content-types](03-content-types.md) → [12-real-world-scenarios](12-real-world-scenarios.md)
3. [06-content-schema](06-content-schema.md) → [08-sample-questions](08-sample-questions.md)
4. [09-ia-screens](09-ia-screens.md) → [07-curriculum-world-1](07-curriculum-world-1.md)
5. [14-learning-flow](14-learning-flow.md) → [16-algofit-figma-brief](16-algofit-figma-brief.md) (UI)
6. [13-tech-architecture](13-tech-architecture.md) → [18-stack-decision](18-stack-decision.md) → [17-dev-setup](17-dev-setup.md)
7. API 스펙 (다음, 번호 TBD)

## 다음 문서 권장

| 제안 문서 | 목적 | 상태 |
|-----------|------|------|
| [13-tech-architecture.md](13-tech-architecture.md) | 클라이언트/백엔드, 게스트·동기화, 오프라인 | ✅ |
| [14-learning-flow.md](14-learning-flow.md) | 플랫폼·스트릭·Algofit 협의 확정 | ✅ |
| [15-figma-mcp-setup.md](15-figma-mcp-setup.md) | Figma MCP (Cursor) | ✅ |
| [16-algofit-figma-brief.md](16-algofit-figma-brief.md) | Figma 디자인 브리프 | ✅ |
| `17-api-spec.md` (가칭) | 진행 저장, 일일 챌린지, sync API (Phase 2) | **다음** |
| `18-content-authoring.md` | CSV/스프레드시트 → JSON 변환, QA 체크리스트 | |
| `19-analytics-events.md` | 학습·리텐션 이벤트 명세 | |
