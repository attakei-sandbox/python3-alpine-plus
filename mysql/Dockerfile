FROM python:3.6-alpine

RUN apk add \
        --no-cache \
        mariadb-client-libs \
        mysql-dev gcc musl-dev && \
    pip install \
        --no-cache-dir \
        mysqlclient && \
    apk del \
        mysql-dev gcc musl-dev
