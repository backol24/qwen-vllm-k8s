# Система инференса для LLM с использованием vLLM в k8s-like среде

Проект запускает Qwen2.5-0.5B-Instruct через vLLM 0.27.0 на CPU. Модель автоматически скачивается в PVC при первом запуске и используется из него после перезапуска Pod.

## Использовалось

- Docker Desktop с 10 ГБ памяти;
- Minikube;
- kubectl.

## Запуск

Образы:

```bash
docker build --platform linux/arm64 -t qwen_vllm:latest .
docker build --platform linux/arm64 -t qwen_downloader:latest downloader/
```

Загрузка minikube и образа:

```bash
minikube start --driver=docker --cpus=4 --memory=8192
minikube image load qwen_vllm:latest
minikube image load qwen_downloader:latest
```

Применение манифестов:

```bash
kubectl apply -k k8s/
```

Логи сервера:

```bash
kubectl logs -f deployment/llm-server -c model-downloader
kubectl logs -f deployment/llm-server -c vllm
```

Открыть доступ:

```bash
kubectl port-forward service/llm-server 8000:8000
```

Отправить запрос:

```bash
curl http://127.0.0.1:8000/v1/chat/completions \
  -H "Authorization: Bearer key123" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen",
    "messages": [
      {
        "role": "user",
        "content": "Что такое LLM? Ответь кратко."
      }
    ],
    "max_tokens": 50
  }'
```

Остановить работу:

```bash
minikube stop
```
