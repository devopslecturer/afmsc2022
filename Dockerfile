# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "waitress-serve", "--port=8080" , "--call", "app:create_app"]
CMD [ "flask", "db" , "init"]
CMD [ "flask", "db" , "migrate"]
CMD [ "flask", "db" , "upgrade"]