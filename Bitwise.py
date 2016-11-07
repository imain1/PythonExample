#!/usr/bin/python

a=0xffff
b=0x1111
c=a&b

print 'c=',hex(c)

a=10
b=20
mylist=[10,20,30,40,50]

if(a not in mylist):
    print 'a=',a,'is not in mylist',mylist
else:
    print 'a=',a,'is in mylist',mylist
    
    

if( b in mylist):
    print 'b=',b,'is in mylist',mylist
else:
    print 'b=',b,'is not in mylist',mylist


if (a is b):
    print 'a is b'
else:
    print 'a is not b'
        


count =0

while (count<9):
    print "count=",count
    count+=1


var = 0

while var < 5:
    var = var+1
    print "var=",var
else:
    print "(else)var=",var

    
    
