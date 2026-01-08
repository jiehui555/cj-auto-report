FROM python:3.11-slim-bookworm

WORKDIR /app

# 安装依赖
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN playwright install --only-shell --with-deps chromium

COPY . .

CMD ["python", "main.py"]
