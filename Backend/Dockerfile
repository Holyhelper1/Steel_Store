FROM python:3.11

RUN mkdir /steelstore-backend

WORKDIR /steelstore-backend

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

RUN chmod a+x /steelstore-backend/docker/app.sh

CMD ["gunicorn", "app.main:app", "--workers", "4", "--worker-class",  "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]