FROM tiangolo/uvicorn-gunicorn-fastapi

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV PORT=3000
