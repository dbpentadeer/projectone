# --------------------------------------------------------------
# Dockerfile – 打包 myProject（Flask 為例）
# --------------------------------------------------------------

# 1️⃣ 基礎映像 – 輕量的 Python 3.11 slim
FROM python:3.11-slim

# 2️⃣ 設定容器內的工作目錄
WORKDIR /app

# 3️⃣ 若有 requirements.txt，先安裝相依套件（如果沒有則跳過）
COPY requirements.txt . || true
RUN if [ -f requirements.txt ]; then \
        pip install --no-cache-dir -r requirements.txt; \
    fi

# 4️⃣ 複製整個專案（會受到 .dockerignore 的過濾）
COPY . .

# 5️⃣ 設定環境變數 – 讓 Python 直接 flush stdout，方便 docker logs
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# 6️⃣ 預設入口 – 假設 Flask 程式入口是 src/main.py
# 如需其他入口請自行修改此行
CMD ["python", "-u", "src/main.py"]
