FROM vllm/vllm-openai-cpu:v0.27.0-arm64@sha256:d8ad98d4aa9ae41674b825d505184d55c2ef1f4a9c77e732e53c5caf9a9e5d51

USER root

RUN groupadd --gid 10001 app \
    && useradd --create-home --uid 10001 --gid 10001 app

WORKDIR /home/app

COPY requirements.txt /home/app/requirements.txt

RUN python -m pip install --no-cache-dir --no-deps -r /home/app/requirements.txt

RUN mkdir -p /home/app/models \
    && chown -R app:app /home/app

COPY --chown=app:app start.py /home/app/start.py

ENV HOME=/home/app
ENV HF_HOME=/home/app/models/.cache

USER app

ENTRYPOINT ["python", "/home/app/start.py"]

CMD ["--dtype", "bfloat16", \
     "--max-model-len", "512", \
     "--max-num-seqs", "1", \
     "--kv-cache-memory-bytes", "128M", \
     "--enforce-eager", \
     "--no-enable-log-requests", \
     "--no-enable-log-outputs"]