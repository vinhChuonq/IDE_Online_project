FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY ./app /app

RUN apt-get update

RUN apt-get install default-jdk -y

RUN apt-get install mono-complete -y
