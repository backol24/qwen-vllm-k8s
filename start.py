import os
import sys
from pathlib import Path


def main():
    model_id = os.getenv("MODEL_ID", "Qwen/Qwen2.5-0.5B-Instruct")
    model_dir = Path("/home/app/models") / model_id.replace("/", "--")
    ready = model_dir / ".download-complete"

    if not ready.exists():
        raise RuntimeError("Model files are not downloaded.")

    os.execvp("vllm", ["vllm", "serve", str(model_dir),
                       "--served-model-name", "qwen", *sys.argv[1:]])

if __name__ == "__main__":
    main()
