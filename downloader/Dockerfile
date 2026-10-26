FROM python:3.12-slim

RUN groupadd --gid 10001 app \
    && useradd --create-home --uid 10001 --gid 10001 app

WORKDIR /home/app

COPY requirements.txt requirements.txt

RUN python -m pip install --no-cache-dir --no-deps -r requirements.txt

RUN mkdir -p /home/app/models \
    && chown -R app:app /home/app

COPY --chown=app:app download_model.py download_model.py

ENV HOME=/home/app
ENV HF_HOME=/home/app/models/.cache

USER app

ENTRYPOINT ["python", "/home/app/download_model.py"]
