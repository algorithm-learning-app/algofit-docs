# algofit-docs

알고핏 제품 기획·스펙·디자인 에셋 저장소.

- [`docs/`](docs/) — 기획·ADR·Figma 가이드
- [`design/`](design/) — 마스코트 등 디자인 원본

앱 구현: [algofit-mobile](https://github.com/algorithm-learning-app/algofit-mobile) · [algofit-web](https://github.com/algorithm-learning-app/algofit-web)

## PR 리뷰 (로컬 봇)

변경은 보통 `main`에 직접 푸시합니다. PR을 열었을 때:

```bash
export PR_REVIEW_BASE=main
export PR_REVIEW_CHECK_COMMAND="$(git rev-parse --show-toplevel)/scripts/pr-review-check.sh"
python3 ~/.codex/skills/gh-review-pr/scripts/review_pr.py --pr-url <NUMBER>
```

검증만: `./scripts/pr-review-check.sh` (JSON·docs). 상세: [docs/20-pr-review-setup.md](docs/20-pr-review-setup.md).
