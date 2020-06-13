FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y x11-apps
RUN apt-get install -y poppler-utils
# Replace 1000 with your user / group id
ARG uid=1000
ARG gid=1000
RUN groupadd -g ${uid} pdfs && \
    useradd -u ${gid} -g pdfs -r pdf && \
    mkdir -p /home/pdf/pdf_auto_sign && \
    chown ${uid}:${gid} -R /home/pdf

RUN export LC_ALL=ja_JP.UTF-8
RUN export LANG=ja_JP.UTF-8

WORKDIR /home/pdf/
ADD ./pdf_auto_sign/requirements.txt /home/pdf/pdf_auto_sign/
RUN pip install -r /home/pdf/pdf_auto_sign/requirements.txt
USER pdf
ADD . /home/pdf/pdf_auto_sign/