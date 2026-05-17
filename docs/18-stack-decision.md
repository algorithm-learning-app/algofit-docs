# ADR-009: 클라이언트 스택 — Flutter(모바일) + React(PC 웹)

| 항목 | 내용 |
|------|------|
| **상태** | 확정 |
| **결정일** | 2026-05-17 |
| **관련** | [13-tech-architecture.md](13-tech-architecture.md) · [14-learning-flow.md](14-learning-flow.md) · [17-dev-setup.md](17-dev-setup.md) |

---

## 맥락

MVP는 모바일 우선(3~5분 Daily·Pick·Blank)이면서, **긴 Blank·코딩·PC 보너스**는 데스크톱 경험이 적합합니다. 초기에는 PWA 단일 코드베이스를 검토했으나, 사용자 의도는 다음과 같이 정리되었습니다.

- **일상 학습(홈·Daily·스트릭·게임 UI)** → 네이티브에 가까운 모바일 앱
- **PC 전용·참고 UI·긴 세션** → 기존 React(Vite) 웹

## 결정

| 플랫폼 | 스택 | 레포 경로 | 역할 |
|--------|------|-----------|------|
| **iOS / Android** | Flutter (Material 3) | `apps/mobile/` | 홈, Daily, Pick/Blank 짧은 세션, 스트릭, World 맵, 하단 탭 |
| **PC 웹** | React 18 + Vite + TypeScript | `apps/web/` | 긴 Blank, 코딩 UI, PC 보너스, 프로토타입·레퍼런스 UI |

- **콘텐츠·스키마**는 루트 `content/`(또는 향후 공유 패키지)를 단일 소스로 유지
- **게스트 진행**은 MVP에 각 클라이언트 로컬 저장(모바일: 플랫폼 저장소, 웹: `localStorage`)
- 폴더명 `apps/web`은 **이름 변경 없음**(경로·CI 유지). 역할은 문서·README에서 **PC 웹**으로 명시

## 근거

1. **사용자 의도**: 모바일은 앱스토어·푸시·제스처 UX; PC는 넓은 화면·키보드·긴 코드 블록
2. **이미 투자된 자산**: `apps/web` 홈·Daily vertical slice는 PC 경로·UI 레퍼런스로 재사용
3. **MVP 속도**: Flutter 홈·Daily 우선 구현; 웹은 PC 기능·디자인 시안 유지, 모바일 기능 확장은 하지 않음
4. **PWA 단일 스택 한계**: 모바일 Daily·게임 톤을 PWA만으로 맞추기보다 Flutter가 제품 방향과 일치

## 결과

### 해야 할 일

- `apps/mobile`: Flutter 앱, 패키지 `com.algofit` / 앱명 algofit
- `apps/web`: PC 웹·참고 UI; Daily 플로우는 **PC 경로**로 유지 가능(삭제하지 않음)
- 문서·README에 모노레포 구조와 실행 방법 분리 기술

### 하지 않을 일 (MVP)

- React로 모바일 Daily·홈 기능 확장
- Capacitor/TWA로 웹을 앱스토어에 싸기 (Later 검토)
- 단일 코드베이스(RN 등)로 즉시 통합

## 대안 (기각·보류)

| 대안 | 보류 이유 |
|------|-----------|
| PWA only | 모바일 제품 품질·앱스토어 요구와 불일치 |
| React Native only | PC 긴 Blank·기존 Vite 자산 활용 어려움 |
| Flutter only | PC 보너스·코딩 UX에 웹 스택이 이미 적합 |

---

*다음 구현 우선순위: Flutter Daily 5문항 플로우 → 콘텐츠 JSON 공유*
