#!/usr/bin/python


import time

now_ticks=time.time()

print "Number of think since 12:00am, January,1,1970:", now_ticks

now_localtime=time.localtime(time.time())

print "Local Current Time: ", now_localtime
print "data type:", type(now_localtime)
