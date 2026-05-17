# Algofit Figma 디자인 브리프

앱명: **알고핏 (Algofit)** · 톤: 가벼운 게임 (XP, 스트릭 불꽃, 월드 맵)  
캐릭터: **A** 무료 일러스트 + **B** 커스텀 마스코트(로봇 캡슐)

> 협의 확정 반영 — 플랫폼·스트릭·PC 보너스는 [14-learning-flow.md](14-learning-flow.md) 참고.

---

## 디자인 토큰 (다크 게임 팔레트)

MVP는 **다크 모드 1종**으로 통일합니다. Figma **Variables** 컬렉션 `Algofit / Core` 권장.

| 토큰 | 용도 | Hex |
|------|------|-----|
| `color/primary` | CTA, 진행, 브랜드 민트 | `#2DD4BF` |
| `color/streak` | 스트릭 불꽃·배지 | `#F97316` |
| `color/xp` | XP·레벨·보상 | `#FBBF24` |
| `color/bg` | 앱 배경 | `#0F172A` |
| `color/surface` | 카드·시트 | `#1E293B` |
| `color/text` | 본문 | `#F1F5F9` |
| `color/text-muted` | 보조 | `#94A3B8` |
| `color/success` | 정답 | `#34D399` |
| `color/error` | 오답 (과하지 않게) | `#F87171` |

**간격:** 4pt 그리드 — `space/8`, `16`, `24`, `32`  
**라운드:** 카드 `16`, 버튼 `12`, 칩 `999`  
**타이포 (예):** Display 28/Bold, Title 20/Semibold, Body 16/Regular, Caption 13/Regular

---

## 프레임 규격

| 항목 | 값 |
|------|-----|
| 모바일 기준 | **390 × 844** (iPhone 14 논리 해상도) |
| PC 보너스 | 별도 프레임 `PC_Bonus` (웹 1280×800 또는 1440×900 중 택1) |

---

## 프레임 명명 규칙

Figma 페이지 예: `Mobile` / `PC`

| 프레임 이름 | 내용 |
|-------------|------|
| `01_Home` | Daily 카드, 스트릭·하트·XP, 월드 요약, 이어하기 |
| `02_Daily_Pick` | 오늘 5문항 중 Pick UI, ProgressDots |
| `03_Feedback_Correct` | 정답 오버레이 + 마스코트 happy |
| `04_Daily_Complete` | 5/5 완료, 스트릭 갱신, 세션 요약 CTA |
| `05_World_Map` | World 노드 맵, 잠금/클리어 상태 |
| `PC_Bonus` | PC 전용 보너스 미션 (모바일 핵심 루프 아님) |

추가 화면은 `06_…` 접두사로 확장. [09-ia-screens.md](09-ia-screens.md)의 S02~S09와 매핑.

---

## 컴포넌트 목록 (Figma Components)

네이밍: `Category/Name` (슬래시 계층)

| 컴포넌트 | 설명 |
|----------|------|
| `Button/Primary` | 메인 CTA — 민트 fill, 라벨 흰색/다크 대비 WCAG 확인 |
| `Card/Daily` | 일일 챌린지 진입 카드 (제목, 5문항, 스트릭 힌트) |
| `Heart` | 하트 0~5 (filled / empty variant) |
| `StreakBadge` | 불꽃 + 일수 (`color/streak`) |
| `ProgressDots` | 5칸 진행 (완료·현재·미완료 variant) |

**권장 variant 속성:** `state=default|pressed|disabled`, `size=md`

---

## 캐릭터 에셋

### A — 무료 일러스트 (Figma에 Import)

| 소스 | URL | 용도 |
|------|-----|------|
| Open Peeps | https://www.openpeeps.com/ | 사람형 아바타·온보딩 |
| Humaaans | https://www.humaaans.com/ | 조합형 일러스트 |
| Kenney | https://kenney.nl/assets | UI 아이콘·간단 스프라이트·게임 UI 키트 |

- 라이선스 페이지에서 **상업적 사용·수정** 조항 확인 후 사용
- Figma: **Place image** 또는 SVG import → `Assets/Characters/A_*` 프레임에 정리

### B — 커스텀 마스코트 (Algofit 로봇 캡슐)

레포 내 PNG (이미 생성됨):

| 파일 | 상태 |
|------|------|
| `design/assets/mascot/algofit-mascot-neutral.png` | 기본 |
| `design/assets/mascot/algofit-mascot-happy.png` | 정답 |
| `design/assets/mascot/algofit-mascot-sad.png` | 오답 |

**Figma 배치**

1. 페이지 `Assets` 또는 `Mobile` 하위에 프레임 **`Mascot / Algofit`**
2. PNG 3장 import → Component **`Mascot/Algofit`** 생성, variant `expression=neutral|happy|sad`
3. `03_Feedback_Correct` → `happy`, 오답 피드백 프레임(추가 시) → `sad`, `01_Home` 하단 또는 카드 옆 → `neutral`
4. 크기: 모바일에서 높이 **80~120pt** 권장, Auto Layout으로 텍스트와 정렬

> Duolingo 녹색 올빼미와 구분: **민트·캡슐 실루엣** 유지.

---

## 화면별 배치 힌트

### `01_Home`

- 상단: `StreakBadge` + `Heart` + XP 바(골드 `#FBBF24`)
- 중앙: `Card/Daily` (오늘 5문항, 5/5 스트릭 조건 안내 한 줄)
- 하단: World 맵 썸네일 → `05_World_Map` 링크
- 마스코트 `neutral` — Daily 카드 옆 또는 빈 상태일 때

### `02_Daily_Pick`

- `ProgressDots` (5)
- Pick 지문 + 선택지
- 제출 `Button/Primary`

### `03_Feedback_Correct` / 오답

- 반투명 오버레이 + 해설 2~3줄
- 마스코트 happy / sad

### `04_Daily_Complete`

- “오늘 5/5 완료!” + 스트릭 +1 애니메이션(프로토타입 optional)
- XP 합산, `Button/Primary` → 홈

### `05_World_Map`

- 노드·경로 — `color/primary` 클리어, muted 잠금

### `PC_Bonus`

- “보너스” 배지 — 모바일 Daily와 시각적으로 구분 (예: 보라 악센트 `#A78BFA` 보조)
- 문구: PC에서만 추가 XP, 스트릭 필수 조건 아님

---

## Cursor MCP 연동 후

1. [15-figma-mcp-setup.md](15-figma-mcp-setup.md)대로 MCP 연결
2. 파일명 **Algofit**으로 Figma Design 파일 생성
3. 위 프레임·컴포넌트·Variables 반영
4. `01_Home` 등 **Copy link to selection** URL을 Cursor에 전달

**등록된 Figma 파일:** [Algofit](https://www.figma.com/design/f5zi1IUfrnYnydZCzOiovu/Algofit) · file key `f5zi1IUfrnYnydZCzOiovu`

---

## 관련 문서

| 문서 | 내용 |
|------|------|
| [14-learning-flow.md](14-learning-flow.md) | 학습·플랫폼·스트릭 규칙 |
| [15-figma-mcp-setup.md](15-figma-mcp-setup.md) | MCP 설치 |
| [09-ia-screens.md](09-ia-screens.md) | 화면 ID |
| [04-gamification.md](04-gamification.md) | XP·하트 (스트릭 상세는 14에서 5/5 정답 기준) |
