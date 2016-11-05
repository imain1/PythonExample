""" 
Page 217 of python_touturial.pdf.
Chapter 15. Moudles
"""
#!/usr/bin/python

#Import moudule support
import support
import math #for dir(math)
#Now we can call defined function that moudle as follows
support.print_func("Chang")



Money=2000

def AddMoney():
    global Money
    Money = Money+1
print Money
AddMoney()
print Money



content=dir(math)
print content

content2=dir(support)
print content2
print "support.__file__:", support.__file__
print "support.__doc__:",support.__doc__
print "support.__name__:",support.__name__
print "support.__package__:",support.__package__

