# 표준 라이브러리
# import datetime as dt
from datetime import date, datetime

first_date = date(2022, 12, 25)
# print(first_date)

cur_date = date.today()
# print(cur_date)

print(cur_date - first_date)

cur_dt = datetime.now()
print(cur_dt)
print(cur_dt.strftime('%Y-%m-%d')) # date.today()와 동일하지만 str

print(cur_dt.weekday()) # 월요일이 0
print(cur_dt.isoweekday()) # 월요일이 1

# ----------------------------------------------------------------------

# sleep
# 파이썬 => second 단위
# C#, java, C++ => ms 단위 (1초 = 1000)

import time

for x in range(10):
    print(x)
    # time.sleep(1.0) # 초(second) 단위, float ok
    # time.sleep(1)
    # time.sleep(0.1) # 0.1초

# ----------------------------------------------------------------------

import math

print(math.pi)

# ----------------------------------------------------------------------

import os

# print(os.environ)
# print(os.environ['PATH'])
# print(os.getcwd())
# print(os.system('dir'))
# print(os.system('python --version')) # 콘솔 명령어 실행

# ----------------------------------------------------------------------

import json

with open('./Day04/data.json', mode='r', encoding='utf-8') as f:
    # load -> str / loads -> byteArray
    data = json.load(f)

print(data)

# ----------------------------------------------------------------------

# urllib
from urllib.request import urlopen

res = urlopen('https://www.naver.com')
print(res.status) # 200 : OK
print(res.read().decode('utf-8')) # index.html -> 웹 크롤링 기초