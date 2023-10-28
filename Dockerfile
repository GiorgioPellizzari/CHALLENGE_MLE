# syntax=docker/dockerfile:1.2
FROM python:3.9.13

WORKDIR /CHALLENGE_MLE
COPY . /CHALLENGE_MLE

RUN pip install -r requirements.txt

CMD uvicorn challenge/api:app --port=8080 --host:0.0.0.0
# put you docker configuration here