import os
from pathlib import Path
from huggingface_hub import snapshot_download


def main():
    model_id = os.getenv("MODEL_ID", "Qwen/Qwen2.5-0.5B-Instruct")
    model_dir = Path("/home/app/models") / model_id.replace("/", "--")
    ready = model_dir / ".download-complete"

    if ready.exists():
        print("Using saved model.", flush=True)
        return

    print("Downloading model.", flush=True)
    model_dir.mkdir(parents=True, exist_ok=True)
    snapshot_download(repo_id=model_id, local_dir=model_dir,
                      token=os.getenv("HF_TOKEN") or None)
    ready.touch()

if __name__ == "__main__":
    main()
