# PR 리뷰 (로컬 봇) 설정

GitHub Actions 대신 **로컬에서 검증한 뒤** Codex 스킬이 PR에 코멘트를 남기는 방식입니다. 저장소마다 `PR_REVIEW_CHECK_COMMAND`로 빌드·테스트·콘텐츠 검증을 지정합니다.

## 저장소별 PR / main 현황 (2026-05-18 기준)

| 저장소 | GitHub | PR | 비고 |
|--------|--------|-----|------|
| [algofit-mobile](https://github.com/algorithm-learning-app/algofit-mobile) | `apps/mobile` 동기화 | **가능** — `feat/world-1-map` 브랜치에 World 1 맵 작업 | 유일하게 feature PR이 열릴 수 있는 앱 |
| [algofit-web](https://github.com/algorithm-learning-app/algofit-web) | `apps/web` 동기화 | **없음** — `main`에 직접 푸시 | PC 웹·Daily·PC 보너스 |
| [algofit-docs](https://github.com/algorithm-learning-app/algofit-docs) | 루트 `docs/` + `content/` | **없음** — `main`에 직접 푸시 | 기획·스펙·JSON 콘텐츠 |

모노레포(`algorithm-training`)는 통합 작업 공간이며, 원격 푸시는 위 세 저장소로 나뉩니다.

## 로컬 봇 스크립트

리뷰 본문·검증 결과를 GitHub PR에 올리는 진입점:

```text
~/.codex/skills/gh-review-pr/scripts/review_pr.py
```

스킬 문서: `~/.codex/skills/gh-review-pr/SKILL.md`

PR 생성 후 자동 훅을 쓰려면 `~/.codex/skills/gh-create-pr/scripts/create_pr.py`가 같은 리뷰 스크립트를 호출합니다 (`--no-review-hook`으로 끌 수 있음).

## `PR_REVIEW_CHECK_COMMAND` (저장소별)

리뷰 게시 **전에** 실행할 셸 명령입니다. 실패하면 리뷰 스크립트가 검증 실패로 처리합니다.

| 저장소 | 스크립트 경로 |
|--------|----------------|
| algofit-mobile | `scripts/pr-review-check.sh` — `flutter pub get` · `analyze` · `test` |
| algofit-web | `scripts/pr-review-check.sh` — `npm ci`/`install` · `npm run build` |
| algofit-docs | `scripts/pr-review-check.sh` — `content/questions/*.json` JSON 검증, `docs/*.md` 존재 확인 |

각 저장소 README의 **「PR 리뷰 (로컬 봇)」** 절과 루트 `.env.pr-review.example`을 참고하세요.

## 실행 방법

### 1) 환경 변수

저장소 루트에서 (또는 `.env.pr-review.example` 복사 후):

```bash
export PR_REVIEW_BASE=main
export PR_REVIEW_CHECK_COMMAND="$(git rev-parse --show-toplevel)/scripts/pr-review-check.sh"
```

### 2) PR 번호 또는 URL로 리뷰

```bash
# 예: algofit-mobile PR #1
cd apps/mobile   # 또는 algofit-mobile 클론 루트
export GH_REPO=algorithm-learning-app/algofit-mobile   # 필요 시
python3 ~/.codex/skills/gh-review-pr/scripts/review_pr.py --pr-url 1
```

드라이런:

```bash
python3 ~/.codex/skills/gh-review-pr/scripts/review_pr.py --pr-url 1 --dry-run
```

### 3) PR 생성 직후 (mobile feature 브랜치 예시)

```bash
git checkout feat/world-1-map
git push -u origin feat/world-1-map
gh pr create --base main --title "feat(world): World 1 map and stage routes" --body "..."
# create_pr 스킬을 쓰면 리뷰 훅이 자동 실행됨
export PR_REVIEW_CHECK_COMMAND="$(git rev-parse --show-toplevel)/scripts/pr-review-check.sh"
python3 ~/.codex/skills/gh-review-pr/scripts/review_pr.py --pr-url <PR_URL>
```

### 4) main만 쓰는 저장소 (web / docs)

PR이 없어도 로컬에서 검증만 돌릴 수 있습니다:

```bash
./scripts/pr-review-check.sh
```

나중에 PR을 열면 동일한 `PR_REVIEW_CHECK_COMMAND`를 export한 뒤 `review_pr.py`를 호출하면 됩니다.

## 관련 환경 변수 (요약)

| 변수 | 용도 |
|------|------|
| `PR_REVIEW_BASE` | 비교 기준 브랜치 (보통 `main`) |
| `PR_REVIEW_CHECK_COMMAND` | 리뷰 전 로컬 검증 명령 |
| `PR_REVIEW_MODE` | `issue-comment` (기본) 또는 `review` |
| `PR_REVIEW_TESTS` | 리뷰 본문에 넣을 검증 요약 텍스트 |
| `GH_REPO` | `owner/repo` 강제 지정 |

봇 인증: `~/.codex/githubbot/{org}/.env` (GitHub App) 또는 `gh` 로그인 폴백 — `gh-review-pr` 스킬 참고.

## GitHub Actions는 사용하지 않음

CI 워크플로우 대신 **옵션 2**: 개발자 머신에서 `pr-review-check.sh` 실행 + `review_pr.py`로 PR 코멘트. 팀원마다 Flutter/Node/Python 로컬 환경만 맞추면 됩니다.
