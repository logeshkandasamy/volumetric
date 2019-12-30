import os

os.system("locust -f locust.py --host=http://blazedemo.com  --csv=sample  --no-web -c 100 -r 1 -t 1m  ")