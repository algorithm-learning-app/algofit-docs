# 개발 환경 · 코드 우선

## 디자인 소스

- **Source of truth**: 이 레포의 `apps/web/` (및 향후 `content/`).
- **Figma**: 참고용. 수동 복붙 없이 코드에서 UI를 맞춥니다.
- **Figma URL**: [Algofit](https://www.figma.com/design/f5zi1IUfrnYnydZCzOiovu/Algofit) · file key `f5zi1IUfrnYnydZCzOiovu`

토큰·카피는 [16-algofit-figma-brief.md](16-algofit-figma-brief.md), 홈 구성은 [14-learning-flow.md](14-learning-flow.md)를 따릅니다.

## 모바일 앱 (Flutter)

```bash
cd apps/mobile
flutter pub get
flutter run
```

| 항목 | 설명 |
|------|------|
| 시뮬레이터 | `flutter devices` → `flutter run -d <id>` |
| iOS | Xcode 설치 후 시뮬레이터 또는 실기기 |
| Android | Android Studio / 에뮬레이터 또는 USB 디버깅 |
| 분석 | `flutter analyze` |

패키지: `com.algofit.algofit` · 상세: [apps/mobile/README.md](../apps/mobile/README.md)

## PC 웹 (React + Vite)

```bash
cd apps/web
npm install
npm run dev
```

개발 서버: http://localhost:5174 (Vite 기본 5173이 다른 앱과 겹치면 5174 사용)

빌드 확인: `cd apps/web && npm run build`

아키텍처·스택 ADR: [13-tech-architecture.md](13-tech-architecture.md) · [18-stack-decision.md](18-stack-decision.md)

## 현재 범위

### `apps/mobile` (Flutter)

| 포함 | 미포함 |
|------|--------|
| 홈 UI (스트릭, XP, Daily 카드, PC 보너스 안내, World 1, 하단 탭) | Daily 5문항 플로우 |
| 마스코트 에셋 | 로컬 진행 저장 |

### `apps/web` (PC)

| 포함 | 미포함 |
|------|--------|
| 홈 UI (레퍼런스) | 모바일 제품 기능 확장 |
| Daily 5문항 플로우 — **PC 경로** (`/daily`, `/daily/:step`) | 50문항·scenario_map |
| 게스트 `localStorage` (스트릭·XP·진행) | 서버 동기화 |
| 플레이스홀더 (`/learn`, `/profile` 등) | World·시나리오 (모바일 우선) |

### Daily 라우트

| 경로 | 설명 |
|------|------|
| `/daily` | 오늘 챌린지 시작 (진행 중이면 이어하기) |
| `/daily/1` … `/daily/5` | 문항 |
| `/daily/:step/feedback` | 문항별 피드백 |
| `/daily/complete` | 5문항 종료·스트릭 결과 |

홈 **이어하기** → `/daily`. 5/5 전부 정답 시 `localStorage` 스트릭 +1 (Asia/Seoul 날짜 기준, 같은 날 중복 갱신 없음).
