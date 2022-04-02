# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

ARG DB_USR
ARG DB_PWD
ARG DB_URL
ARG DB_PORT
ARG DB_NAME

ENV DB_USR=$DB_USR
ENV DB_PWD=$DB_PWD
ENV DB_URL=$DB_URL
ENV DB_PORT=$DB_PORT
ENV DB_NAME=$DB_NAME

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "flask", "db" , "init"]
CMD [ "flask", "db" , "migrate"]
CMD [ "flask", "db" , "upgrade"]
CMD [ "waitress-serve", "--port=8080" , "--call", "app:create_app"]
