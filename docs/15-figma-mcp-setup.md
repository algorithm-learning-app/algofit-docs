# Figma MCP 설정 (Cursor)

알고핏(Algofit) UI를 Figma에서 만들고, Cursor 에이전트가 프레임·변수·코드 생성에 접근하려면 **Figma MCP** 연결이 필요합니다.

> **중요:** 이 문서는 설정 가이드만 제공합니다. `~/.cursor/mcp.json`은 **사용자가 직접** 수정·승인해야 합니다(OAuth, 토큰). 에이전트가 사용자 파일을 대신 편집하지 않습니다.

**공식 참고 (2025):**

- [Cursor and Figma: Set up the MCP server](https://help.figma.com/hc/en-us/articles/39889260656407-Cursor-and-Figma-Set-up-the-MCP-server)
- [Set up the remote server (recommended) | Figma Developer Docs](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/)
- [Set up the desktop server | Figma Developer Docs](https://developers.figma.com/docs/figma-mcp-server/local-server-installation/)
- [Figma MCP server guide (GitHub)](https://github.com/figma/mcp-server-guide)

---

## 권장: Remote Figma MCP (Cursor 플러그인)

Figma는 **원격(Remote) MCP**를 기본 권장합니다. 데스크톱 앱 없이도 동작하며, 캔버스 쓰기·변수·코드 생성 등 기능 범위가 가장 넓습니다.

### 1) Figma 플러그인 설치

**방법 A — 에이전트 채팅 (권장)**

Cursor **Agent** 채팅에 아래를 입력합니다:

```text
/add-plugin figma
```

플러그인에 포함되는 것:

- Figma MCP 서버 설정
- 디자인 구현·Code Connect·디자인 시스템 규칙용 **Agent Skills**
- Figma MCP 에셋 처리 **Rules**

**방법 B — 명령 팔레트**

1. `Cmd + Shift + P` (Windows: `Ctrl + Shift + P`)
2. `plugin` 또는 `Figma`로 검색해 **Figma 플러그인** 설치·설정 화면으로 이동  
   (마켓플레이스: [Figma | Cursor Plugins](https://cursor.com/marketplace/figma))

**방법 C — 수동 MCP 추가 (플러그인 없이)**

1. [Figma MCP 서버 딥링크](cursor://anysphere.cursor-deeplink/mcp/install?name=Figma&config=eyJ1cmwiOiJodHRwczovL21jcC5maWdtYS5jb20vbWNwIn0%3D)를 열어 Cursor MCP 설정으로 이동
2. **Install MCP Server?** → Install
3. Figma 옆 **Connect**로 인증 시작

또는 **Cursor → Settings → Cursor Settings → MCP → + Add new global MCP server** 후 URL:

`https://mcp.figma.com/mcp`

### 2) OAuth 인증 (사용자 직접)

Remote 서버는 **Figma OAuth**가 필요합니다. 에이전트가 대신 로그인할 수 없습니다.

1. MCP 탭 또는 플러그인 설치 흐름에서 **Connect** 선택
2. 브라우저에서 Figma **Allow access** 승인
3. Cursor로 돌아와 연결 상태 확인

### 3) 연결 후 할 수 있는 것 (요약)

| 영역 | 설명 |
|------|------|
| 디자인 읽기 | 프레임·컴포넌트·레이아웃·FigJam·변수(색·간격·타이포) |
| 코드 생성 | 선택 프레임 → 코드 (`get_design_context` 등) |
| Code Connect | Figma 노드 ↔ 코드베이스 컴포넌트 매핑 |
| 캔버스 쓰기 (Remote, 베타) | 프레임·컴포넌트·변수 생성·수정 (`use_figma` 등) |
| UI 캡처 (일부 클라이언트) | 로컬 웹 UI → Figma 레이어로 전송 |

**링크 기반 컨텍스트:** Figma에서 레이어/프레임 **Copy link to selection** → Cursor 채팅에 URL 붙여넣기. 클라이언트는 URL을 “열지” 않고 `node-id`를 추출해 MCP가 해당 노드를 읽습니다.

**요금·한도:** Starter/View·Collab 시트 등은 읽기 도구 호출 월 6회 등 제한이 있을 수 있습니다. Dev/Full 시트는 REST API Tier 1과 유사한 분당 한도. 상세는 [Figma MCP 가이드](https://github.com/figma/mcp-server-guide/blob/main/README.md).

---

## 대안: Desktop MCP (로컬)

조직·엔터프라이즈 등 **특수 케이스**용입니다. Figma도 **Remote 사용을 강력 권장**합니다.

### Figma 데스크톱에서 서버 켜기

1. [Figma desktop app](https://www.figma.com/downloads/) 최신 버전 설치
2. Design 파일 열기
3. 하단 툴바에서 **Dev Mode** (`Shift + D`)
4. Inspect 패널 **MCP server** → **Enable desktop MCP server**
5. 확인 메시지 후 주소 복사: `http://127.0.0.1:3845/mcp`

### `~/.cursor/mcp.json` 예시 (playwright와 병행)

기존에 `playwright`만 있다면, **아래 전체를 참고해 사용자가 직접 병합**합니다. 키 이름은 `figma-desktop`을 사용합니다.

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    },
    "figma-desktop": {
      "url": "http://127.0.0.1:3845/mcp"
    }
  }
}
```

> 실제 `playwright` 블록은 환경마다 다를 수 있습니다. **기존 항목은 유지**하고 `figma-desktop`만 추가하세요.

**주의**

- Figma 데스크톱 앱이 켜져 있고 해당 파일에서 MCP가 **Enabled** 상태여야 합니다.
- `127.0.0.1`은 로컬 전용입니다. **API 토큰·OAuth 시크릿을 Git에 커밋하지 마세요.**
- Remote 대비 기능·안정성 면에서 일반 프로젝트(알고핏)에는 **Remote 권장**.

---

## 대안: `npx figma-developer-mcp` (레거시·커뮤니티)

Figma 공식 Remote/Desktop 이전에 쓰이던 **서드파티** MCP입니다. 새 프로젝트에는 **공식 Remote 플러그인을 우선**하세요.

- 패키지: [figma-developer-mcp](https://www.npmjs.com/package/figma-developer-mcp) (커뮤니티)
- Figma **Personal access token** → 환경 변수 `FIGMA_API_KEY` (또는 문서/버전에 따라 `FIGMA_ACCESS_TOKEN`)
- `mcp.json`에 `command` + `args` + `env` 형태로 추가하는 방식이 일반적

**주의:** 토큰은 `mcp.json`에 넣지 말고 OS 환경 변수·시크릿 관리 도구를 사용하고, **저장소에 커밋하지 마세요.**

---

## 연결 확인 체크리스트

| # | 확인 항목 | 기대 결과 |
|---|-----------|-----------|
| 1 | Cursor **Settings → MCP** | Figma(또는 `figma-desktop`) 서버가 **Connected** / 도구 목록 표시 |
| 2 | Agent 모드 채팅 | MCP 도구가 활성(플러그인 설치 시 Figma 관련 Skills/Rules 존재) |
| 3 | 테스트 프롬프트 | 아래 예시 실행 |
| 4 | Figma 측 | Design 파일에 **편집 또는 보기** 권한, Dev/Full 시트면 한도 여유 |

**테스트 프롬프트 예시 (Remote):**

```text
이 Figma 프레임 링크의 레이아웃·색 변수를 요약해줘: [프레임 URL 붙여넣기]
```

```text
Figma MCP whoami로 내 계정·시트 정보를 확인해줘.
```

**테스트 프롬프트 예시 (Desktop):**

1. Figma 데스크톱에서 프레임 **선택**
2. Cursor: `현재 Figma 선택 영역의 디자인 컨텍스트를 가져와줘`

실패 시: Figma 앱·Cursor 재시작, MCP 서버 Enable 여부, `mcp.json` JSON 문법, 방화벽(로컬 3845) 확인.

---

## 알고핏(Algofit) 워크플로

MCP 연결이 끝난 뒤:

1. Figma에 Design 파일 생성 — 이름 예: **`Algofit`**
2. [16-algofit-figma-brief.md](16-algofit-figma-brief.md)의 프레임·토큰·컴포넌트 명명 규칙으로 화면 제작
3. 무료 캐릭터 에셋(A) + 커스텀 마스코트(B) 배치 — 마스코트 PNG는 `design/assets/mascot/`
4. **Home** 등 핵심 프레임 URL을 Cursor 채팅에 공유

**에이전트에게 줄 메시지 예시:**

```text
Algofit Figma 파일입니다. 01_Home 프레임 링크: https://www.figma.com/design/...
docs/16-algofit-figma-brief.md 토큰·컴포넌트 이름에 맞춰 구현 계획을 잡아줘.
```

이후 구현 단계에서 프레임별 링크를 붙이면 `get_design_context`, 변수 추출, (Remote) 캔버스 업데이트 등을 이어갈 수 있습니다.

---

## 관련 문서

| 문서 | 내용 |
|------|------|
| [14-learning-flow.md](14-learning-flow.md) | 제품·플랫폼·스트릭 협의 확정 |
| [16-algofit-figma-brief.md](16-algofit-figma-brief.md) | Figma 화면·디자인 토큰 브리프 |
| [09-ia-screens.md](09-ia-screens.md) | 화면 ID·IA |
