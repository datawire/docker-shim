FROM python:3.6-alpine3.7

WORKDIR /app
COPY app.py requirements.txt ./
RUN pip install -Ur requirements.txt

ENTRYPOINT ["python", "app.py"]
