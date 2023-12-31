# syntax=docker/dockerfile:1

FROM python:3.11

WORKDIR /app
ENV FLASK_APP run.py

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
