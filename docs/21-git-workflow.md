# Git · PR 워크플로

알고핏은 **저장소 3개**(`algofit-mobile`, `algofit-web`, `algofit-docs`)로 나뉩니다. 통합 작업 공간 `algorithm-training`은 로컬 모노레포이며, **기능 개발은 feature 브랜치 → PR → 머지**로 진행합니다. `main`에 기능을 직접 푸시하지 않습니다.

## 저장소 ↔ 작업 경로

| GitHub | 로컬 경로 |
|--------|-----------|
| algofit-mobile | `apps/mobile/` |
| algofit-web | `apps/web/` |
| algofit-docs | `docs/`, `content/`, `scripts/` |

## 기본 흐름

1. **`main` 최신화**
   ```bash
   git checkout main && git pull origin main
   ```
2. **feature 브랜치 생성** (`main`에서 분기)
   ```bash
   git checkout -b feat/짧은-설명
   ```
3. **작은 단위 커밋** — 한 커밋은 한 가지 목적(라우터, UI, 테스트 등). 메시지는 저장소 관례에 맞춤(예: `feat(scope): …`, `chore: …`).
4. **푸시 후 PR**
   ```bash
   git push -u origin feat/짧은-설명
   gh pr create --base main --title "…" --body "…"
   ```
5. **로컬 검증 + 리뷰 훅** — [20-pr-review-setup.md](20-pr-review-setup.md) 참고
   ```bash
   export PR_REVIEW_BASE=main
   export PR_REVIEW_CHECK_COMMAND="$(git rev-parse --show-toplevel)/scripts/pr-review-check.sh"
   ./scripts/pr-review-check.sh
   # 필요 시: python3 ~/.codex/skills/gh-review-pr/scripts/review_pr.py --pr-url <번호>
   ```
6. **리뷰 후 머지** — 기본은 **merge commit**(`gh pr merge --merge`). 저장소가 squash만 쓰도록 정해져 있으면 그에 따름.
7. **머지 후 정리** — `main` pull, 원격 feature 브랜치 삭제.

## `main`에만 직접 푸시해도 되는 경우

- 긴급 **hotfix** (운영 장애)
- **오타·문서 한 줄** 수준의 docs 수정 (팀 합의 시)

그 외 기능·리팩터·콘텐츠 배치 변경은 반드시 PR.

## 커밋 시각 (KST)

사용자가 **「자연스러운 타임스탬프」** 를 요청한 경우에만, 실제 작업 시각에 맞춰 `+0900` 타임존으로 커밋합니다. 평소에는 Git 기본 시각을 사용합니다. `GIT_AUTHOR_DATE` / `GIT_COMMITTER_DATE` 조작은 요청이 있을 때만.

## 모노레포 작업 시

- mobile / web / docs는 **각각 해당 원격**에만 푸시합니다.
- 한 기능이 여러 저장소에 걸치면 **저장소마다 별도 브랜치·PR**을 엽니다.
- PR 본문에 연관 PR 링크를 적어 두면 리뷰에 유리합니다.

## 머지 후 확인

```bash
# mobile 예시
cd apps/mobile && git checkout main && git pull
./scripts/pr-review-check.sh
```

## 관련 문서

- [20-pr-review-setup.md](20-pr-review-setup.md) — `PR_REVIEW_CHECK_COMMAND`, 로컬 봇
