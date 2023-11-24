FROM python:3.8.18
USER root

RUN apt-get update && apt-get upgrade -y
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y vim less
RUN apt-get install -y git

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

EXPOSE 5000

RUN apt-get -y install libgl1-mesa-dev # Docker内でOpencvを使うために必要