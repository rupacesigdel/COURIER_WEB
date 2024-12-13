FROM python:3.9-slim
WORKDIR /workspace

COPY requirements.txt .

RUN apt-get update && apt-get install -y curl && \
    pip install --upgrade pip
    COPY . .


RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
