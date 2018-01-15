mkdir -p /run/ldapadmin

rm -f /run/ldapadmin/pid

chown -R www-data: /run/ldapadmin

su - www-data -s /bin/sh -c 'gunicorn -c /gunicorn_conf.py ldapadmin.rest:APP'
