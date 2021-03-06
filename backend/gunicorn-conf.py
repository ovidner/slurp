# -*- coding: utf-8 -*-
from multiprocessing import cpu_count

from environ import Env

env = Env()

bind = ['0.0.0.0:80']

reload = env.bool('GUNICORN_RELOAD', False)
workers = env.int('GUNICORN_WORKERS', cpu_count()*2+1)

loglevel = env.str('GUNICORN_LOG_LEVEL', 'info')
errorlog = '-'  # stderr
accesslog = '-' if env.bool('GUNICORN_ACCESS_LOG', False) else None
