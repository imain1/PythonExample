
#!/usr/bin/python
#import sys;sys.path.append(r'C:\Users\chkim.TNSU-AUS\.p2\pool\plugins\org.python.pydev_5.3.0.201610121612\pysrc')
#import sys;sys.path.append(r'/usr/local/lib/python2.7/dist-packages')
#import pydevd;
#pydevd.settrace('192.168.2.19')

import platform
osname=platform.system()

print("Hello Python2")
print(osname)

if osname=='windows':
    print("I like window")
elif osname=='linux':
    print("I like linux too")
else:
    print("I don't have computer")

print "done"

filename=osname+".txt"

import sys

try:
    mywrite_file = open(filename,"w")
except IOError:
    print "There was an error to writng to ", filename
    sys.exit(-1)

file_finish='End'
file_text=""
print "Enter '", file_finish, "' when finished"    
while file_text != file_finish :
    file_text=raw_input("Enter Text:")
    if file_text==file_finish:
        mywrite_file.close()
        break
    mywrite_file.write(file_text)
    mywrite_file.write("\n")
mywrite_file.close()
print filename,"is saved"


file_name= raw_input("Input file Name:")
if len(file_name)==0:
    print "Next time please enter something"
    sys.exit()

try:
    myread_file=open(file_name,"r")
except IOError:
    print "there was an file reading error"
    sys.exit()

file_text=myread_file.read()
myread_file.close()
print file_text



