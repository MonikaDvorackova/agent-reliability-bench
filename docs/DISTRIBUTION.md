# Distribution and community onboarding

## 1. GitHub → Hugging Face

GitHub Actions **Benchmark artifact** runs automatically and uploads the JSON output as a downloadable CI artifact. It does not send data to third parties.

To opt in to Hugging Face publication, create the GitHub environment `huggingface-publishing`, add repository secret `HF_TOKEN` (a fine-grained write token with permission for the target repositories), and repository variables `HF_DATASET_REPO` and `HF_SPACE_REPO` in `namespace/name` format. Then run **Publish Hugging Face dataset and Space** manually in Actions. Review the target namespace, token scopes and dataset content first.

The Space is a standalone static browser app. It does not require a private API key and does not run third-party agents.

## 2. Community channels

GitHub Discussions: enable in repository Settings → Features → Discussions (requires repository admin). Link relevant discussions from README once created.

Hacker News: submit a Show HN post manually after the public Space has been tested; describe the exact tool-trace baseline and avoid unsupported claims.

Reddit: check subreddit rules before submitting a technical experiment write-up. Do not automate posting or unsolicited outreach.

LinkedIn and blog: share measured examples, the public Space URL, and the source repository. Publish manually or through an explicitly authorized account integration.

## 3. Feedback

Invite reproducible bug reports through GitHub Issues. Include expected tool trace, observed trace, budget, and the benchmark version. Avoid sharing private agent traces or credentials.

## 4. Measurement

GitHub stars are not active users. Track external issues, unique demo usage where privacy-preserving analytics are available, reproducibility reports, and contributions. Do not invent adoption statistics.

## Free public demo fallback

Hugging Face may return HTTP 402 even when creating a Static Space. This is an external hosting restriction, not a dataset publication failure. The publication workflow reports this condition without failing the dataset job.

For a public demo without Hugging Face hosting, open repository **Settings → Pages → Build and deployment → Source: GitHub Actions**. Then manually run **Deploy demo to GitHub Pages** (or push a change to `static-space/`). The intended public URL is `https://monikadvorackova.github.io/agent-reliability-bench/`; it will work only after Pages is enabled and deployment succeeds. No token is needed for Pages.
