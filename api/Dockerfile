FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1

WORKDIR "/api"
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY . /api

RUN adduser -D user
USER user
