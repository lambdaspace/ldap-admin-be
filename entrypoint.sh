mkdir -p /run/ldapadmin

chown -R nginx: /run/ldapadmin

su - nginx -s /bin/sh -c 'gunicorn -c /gunicorn_conf.py ldapadmin.rest:APP'
