"""Opt-in Hugging Face dataset publisher, requiring explicit credentials."""
import os
from pathlib import Path

def publish(path: str = "artifacts/benchmark.json") -> str:
    token = os.environ.get("HF_TOKEN")
    repo = os.environ.get("HF_DATASET_REPO")
    if not token or not repo:
        raise RuntimeError("HF_TOKEN and HF_DATASET_REPO must be set")
    if "/" not in repo:
        raise ValueError("HF_DATASET_REPO must be namespace/name")
    artifact = Path(path)
    if not artifact.is_file():
        raise FileNotFoundError(artifact)
    from huggingface_hub import HfApi
    api = HfApi(token=token)
    api.create_repo(repo_id=repo, repo_type="dataset", exist_ok=True)
    api.upload_file(path_or_fileobj=str(artifact), path_in_repo="benchmark.json",
                    repo_id=repo, repo_type="dataset",
                    commit_message="Publish deterministic benchmark fixture")
    return f"https://huggingface.co/datasets/{repo}"

if __name__ == "__main__":
    print(publish())
