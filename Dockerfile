FROM debian:stretch


ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

RUN apt-get update && \
    apt-get install -y \
    python3-pip python3-setuptools \
    python3-wheel nginx && \
    apt-get autoclean

COPY ./ /ldapadmin/

RUN mv /ldapadmin/src/gunicorn_conf.py /gunicorn_conf.py && \
    mv /ldapadmin/ldapadmin.conf /etc/nginx/sites-available/ && \
    ln -s /etc/nginx/sites-available/ldapadmin.conf /etc/nginx/sites-enabled/ldapadmin.conf && \
    pip3 install /ldapadmin && \
    rm -rf /ldapadmin && \
    service nginx restart

EXPOSE 8443

# Don't try to do it in an entrypoint, or pay with your precious time ...
CMD mkdir -p /run/ldapadmin; \
    rm -f /run/ldapadmin/pid; \
    chown -R www-data: /run/ldapadmin; \
    service nginx restart; \
    su - www-data -s /bin/sh -c 'gunicorn -c /gunicorn_conf.py ldapadmin.rest:APP'
