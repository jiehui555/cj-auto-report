# -------------------------------
# Builder stage - 安裝 Python 依賴
# -------------------------------
FROM python:3.11-slim-bookworm AS builder

WORKDIR /app

RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# -------------------------------
# Final stage
# -------------------------------
FROM python:3.11-slim-bookworm

WORKDIR /app

# 复制虚拟环境
COPY --from=builder /venv /venv
ENV TZ=Asia/Shanghai
ENV PYTHONUNBUFFERED=1
ENV PATH="/venv/bin:$PATH"

# 安裝 cron + 必要的清理
RUN apt-get update \
 && apt-get install -y --no-install-recommends cron \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# 安裝 playwright
RUN playwright install --with-deps chromium

# 复制程序
COPY . .

# 复制定时配置
COPY crontab /etc/cron.d/my-crontab
RUN chmod 0644 /etc/cron.d/my-crontab \
 && crontab /etc/cron.d/my-crontab

# 建立 cron 日志文件
RUN touch /var/log/cron.log

CMD ["cron","-f", "-L", "2"]
