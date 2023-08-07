ARG BASE_IMAGE=python:3.10-slim
FROM $BASE_IMAGE AS base

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 5000
CMD python ./app.py