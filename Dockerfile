FROM python:3.7

#обновить образ
RUN apt-get update -y
RUN apt-get upgrade -y

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/nasa

COPY ./requirements.txt /usr/srs/requirements.txt
RUN pip install -r /usr/srs/requirements.txt

COPY . /usr/src/nasa