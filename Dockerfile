FROM docker.1ms.run/library/python:3.11-slim-bookworm

WORKDIR /app

# 镜像源
RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list.d/debian.sources && apt-get update

# 安装依赖
COPY requirements.txt .
RUN pip install -r requirements.txt -i https://mirrors.ustc.edu.cn/pypi/simple
RUN playwright install --only-shell --with-deps chromium

# 清理
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . .

CMD ["python", "main.py"]
