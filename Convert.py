#!/usr/bin/python
from nt import lstat



a=ord('a')
mychar=chr(a)

print 'mychar',mychar,'(',a,')'

x=1
y=3
#strmessage=raw_input("what do you want to do with x,y:")
#z=eval(strmessage)
#print 'x=',x,'y=',y,strmessage,'=',z

strbuf="chkim,paul,steve,jeff"

tp=tuple(strbuf)
lst=list(strbuf)
print strbuf
print tp
print 'list:',lst

ts=[("name","chkim"),("phone","512-545-0676"),("grade","good")]

mandict=dict(ts)

print "mandict:",mandict

gen=((i,i+1)for i in range(10,50,10))

dgen=dict(gen)
print dgen

import datetime

now=datetime.datetime.now()
print 'str(now):',str(now)
print 'repr(now):',repr(now)

a=9.0
b=2
c=a/b
d=a//b
print 'c=',c
print 'd=',d
