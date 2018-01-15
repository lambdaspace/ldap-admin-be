FROM ubuntu:16.04

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV TERM xterm

RUN apt-get update && apt-get install -y python3 python3-pip nginx

COPY ./ /ldapadmin/

RUN mv /ldapadmin/entrypoint.sh /entrypoint.sh && \
    mv /ldapadmin/src/gunicorn_conf.py /gunicorn_conf.py && \
    mv /ldapadmin/ldapadmin.conf /etc/nginx/sites-available/ && \
    ln -s /etc/nginx/sites-available/ldapadmin.conf /etc/nginx/sites-enabled/ldapadmin.conf && \
    chmod +x /entrypoint.sh && \
    pip3 install /ldapadmin && \
    rm -rf /ldapadmin

EXPOSE 8443

ENTRYPOINT ["/entrypoint.sh"]
