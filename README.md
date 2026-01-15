构建：

```bash
docker build -t cj-cronjob:latest .
```

运行：

```bash
REPO_HOST=ghcr.1ms.run
docker pull "$REPO_HOST/jiehui555/cj-cronjob:latest"

cp .env.example .env
docker run -d --env-file .env "$REPO_HOST/jiehui555/cj-cronjob:latest"
```
