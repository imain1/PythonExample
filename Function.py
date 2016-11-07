#!/usr/bin/python

"""Look here if we want to use print without new line
   we need to add 
     from __future__ import print_function
   and use "print(" somtihing", end='')
   but, for this , we cannot use print... of 2.7 version.
"""

from __future__ import print_function
#from pydevd import line

   
def printme(str):
    "This print a passed string into this function"
    print(str);
    return;


#printme("I'm the first call to user defined function!")

#printme("Again second call to the same function!")

def changeme(mylist):
    print ("mylist.append([1,2,3,4])")
    mylist.append([1,2,3,4])
    mylist[2]=20
    
    print ("values inside this function:", mylist)
    return

def changeme2(mylist):
    print ("mylist=[1,2,3,4]")
    mylist=[1,2,3,4];
    print ("values inside this function:", mylist)
    return

def list_test(selection):
    print ("list test --- selection:",selection,"----")
    
    mylist = [10, 20, 30]
    print ("before change : ", mylist)
    if(selection==1):
        print ("selection is 1")
        changeme(mylist)
    else:
        print ("selection is not 1") 
        changeme2(mylist)
    print ("after change : ", mylist)
    list_count = len(mylist)
    print ("count:", str(list_count))
    
    for i  in range(0, list_count):
        print ("mylist[" + str(i) + "]:", mylist[i])

    return

def print_identify(name="Noname",age="9999"):
    print ("name=",name)
    print ("age=",str(age))
 

def print_information(*vartuple):
    
    "This prints a variable passed arguments"
    print ("-------------------------------------------")
    for var in vartuple:
        print (var+",",end='')
    print ("")
    return

sum = lambda arg1,arg2: arg1+arg2
def function_test():
    print_identify(age=10, name="Chang")
    print_identify()
    print_information("Chang","42","Senior Software Engineer","Austin")
    print_information("Christoper","43")
    
    c=sum(10,20)
    print ("lambda function c=%d"%(c))
    

    
def main():
    list_test(1)
    list_test(2)
#    function_test()
   
   
    
if __name__=='__main__':
    main()
    
    
