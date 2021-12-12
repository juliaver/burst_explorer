# https://docs.gunicorn.org/en/stable/settings.html

import multiprocessing
from dotenv import load_dotenv
load_dotenv()

bind = "0.0.0.0:5000"
workers = 2 * multiprocessing.cpu_count() - 1
threads = 2 * multiprocessing.cpu_count()
timeout = 30
keepalive = 2
max_requests = 500
max_requests_jitter = 100
chdir = "/home/julia/burst_explorer"
worker_tmp_dir = "/dev/shm"
forwarded_allow_ips = "*"
proxy_allow_ips = "*"
loglevel = "info"
