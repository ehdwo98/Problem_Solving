import sys
input=sys.stdin.readline
import datetime

print((datetime.datetime.today()+datetime.timedelta(hours=9)).strftime("%Y-%m-%d"))