#!/usr/bin/python

import time


now_ticks=time.time()

print "Number of think since 12:00am, January,1,1970:", now_ticks

now_localtime=time.localtime(time.time())

print "Local Current Time: ", now_localtime
print "data type:", type(now_localtime)


import calendar
cal=calendar.month(2016,11)

print "Calender"
print cal

def someprocdeure():
    time.sleep(2.5)
    
t0 = time.localtime()
print "1.Start Time:",time.strftime('%Y/%m/%d %H:%M:%S',t0)
someprocdeure()
t1 = time.localtime()
print "1.End Time:", time.strftime("%Y/%m/%d %H:%M:%S",t1)

tsec0=time.time()
print "2.Start Time:",time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(tsec0))
someprocdeure()
tsec1=time.time()
print "2.End Time:",time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(tsec1))
print "Time Span=", tsec1-tsec0








