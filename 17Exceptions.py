#!/usr/bin/python


def KelvinToFahrenheit(Temperature):
        assert(Temperature >= 0),"Colder than absoluate Zero"
        
        return ((Temperature -273)*1.8)+32
    
print KelvinToFahrenheit(273)
print int(KelvinToFahrenheit(505.78))
#print KelvinToFahrenheit(-5)


try:
    fh=open("thestfile.txt","w")
    fh.write("this is my test file for exception handling test!!")
except IOError:
    print "Error: Can\'t find file or read data"
else:
    print "Written content in the file successfully"
    fh.close()
    

try:
    fh=open("testfile2.txt","r")
    try:
        fh.write("What is the finally block?")
    finally:
        print 'goint to close the file'
        fh.close()
except IOError,ex:
    print "Error: can not find file or read data:\n", ex

        

def FunctionName(level):
    if level < 1:
        raise "Invalid Level!",level


try:
    FunctionName(0)
except "Invalid Level!":
    print "Error function level"
else:
    print "functoin level is good"

    


