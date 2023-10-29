# syntax=docker/dockerfile:1.2
FROM python:3.9.13

WORKDIR /CHALLENGE_MLE
COPY . /CHALLENGE_MLE

RUN pip install -r requirements.txt
RUN pip install -r requirements-test.txt
RUN pip install -r requirements-dev.txt


EXPOSE 5200
CMD uvicorn challenge.api:app --port=5200 --host=0.0.0.0

# put you docker configuration here