# PR 리뷰 (로컬 봇) 설정

GitHub Actions 대신 **로컬에서 검증한 뒤** Codex 스킬이 PR에 코멘트를 남기는 방식입니다. 저장소마다 `PR_REVIEW_CHECK_COMMAND`로 빌드·테스트·콘텐츠 검증을 지정합니다.

## 저장소별 PR / main 현황 (2026-05-17 기준)

| 저장소 | GitHub `main` | 로컬 | PR 정책 |
|--------|---------------|------|---------|
| [algofit-mobile](https://github.com/algorithm-learning-app/algofit-mobile) | `3d718ea` (PR #1 머지됨) | `apps/mobile/` | **feature 브랜치 + PR** |
| [algofit-web](https://github.com/algorithm-learning-app/algofit-web) | `767cd9e` | `apps/web/` | **feature 브랜치 + PR** (앞으로 `main` 직접 푸시 금지) |
| [algofit-docs](https://github.com/algorithm-learning-app/algofit-docs) | `b5a8a95` | `docs/` · `content/` · `scripts/` | **feature 브랜치 + PR** |

Git 브랜치·머지 절차: [21-git-workflow.md](21-git-workflow.md).

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

### 3) PR 생성 직후 (feature 브랜치 예시)

```bash
git checkout -b feat/my-change
# … 커밋 …
git push -u origin feat/my-change
gh pr create --base main --title "feat(scope): …" --body "…"
export PR_REVIEW_CHECK_COMMAND="$(git rev-parse --show-toplevel)/scripts/pr-review-check.sh"
./scripts/pr-review-check.sh
python3 ~/.codex/skills/gh-review-pr/scripts/review_pr.py --pr-url <PR_URL>
```

### 4) `main`에서 검증만 (머지 후 smoke)

```bash
git checkout main && git pull
./scripts/pr-review-check.sh
```

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
