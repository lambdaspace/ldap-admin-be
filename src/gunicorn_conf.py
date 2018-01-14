pidfile = '/run/ldapadmin/pid'
workers = 4
threads = 4
worker_class = 'aiohttp.worker.GunicornWebWorker'
bind = 'unix:/run/ldapadmin/socket'
umask = '117'
