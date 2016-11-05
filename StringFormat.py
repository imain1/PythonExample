#!/usr/bin/python

print "My name is %s and weight is %d Kg" %('Chang',70)


number= 0xffff

print "number %d(%x:%X)" %(number,number,number)


print "Exponential:%e" %(number)
print "Exponential:%E" %(number)
print "Shorter:%+g" %(number)


minus_number= -100

print "munus_number=%+d" %(minus_number)

mystr= "this is a string example ...wow!"

print "str.capitalize():", mystr.capitalize()

str_title="Title"

print "str_title:", str_title.center(30)


str_name="      Chang Hwan     "
print "name:%s" %(str_name.strip())

str_document_subject="what we have to do today"

print "Title:",str_document_subject.title()

print "Title 4:",str_document_subject.split()

str_data="Christopher,512-545-0676,220 Valona Roop, TX, 78681"
print "member:", str_data.split(',')


str_contents="Today, we will do below things \n1.Ptyhon study\n2.Visit my daughters school.\n3 exercise 1hour running."
print str_contents.splitlines()
print str_contents.splitlines(4)
