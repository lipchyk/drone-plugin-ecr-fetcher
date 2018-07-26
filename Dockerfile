FROM python:2.7-alpine

LABEL maintainer="Siarhei Lipchyk <me@ys-pro.com>"

RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories
RUN apk update 
RUN apk add --no-cache docker
RUN pip install awscli

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["./docker-entrypoint.sh"]
