FROM tiangolo/uwsgi-nginx-flask:python3.6
LABEL MAINTAINER="duynd3"

COPY ./app /app
WORKDIR /app

RUN rm -f /etc/localtime
RUN cp /usr/share/zoneinfo/Asia/Ho_Chi_Minh /etc/localtime

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN apt-get install -y rsync

RUN pip install -r requirements.txt

