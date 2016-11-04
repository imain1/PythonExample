#!/usr/bin/python

dict1={'name':'Zaa','Age':7}
dict2={'name':'Zaanaz','Age':7}
dict3={'name':'Abid','Age':27}
dict4={'name':'Zara','Age':7}

print "cmp(dict1,dict2):%d" %cmp(dict1,dict2)
print "len(dict1):%d" %len(dict1)

mystr=str(dict1)
print "dict1:%s"%(dict1)
print "str(dict1):%s"%mystr


keys=('name','age','sex')

mydic=dict.fromkeys(keys)

print "New Dictionary:%s"%mydic

#print "Value:%s" dict1.get('name')

print "Is dict1 has edu?%s"%dict1.has_key('edu')
print "dict1 items are %s"%dict1.items()

print "Value:%s" %dict1.setdefault('Age',None)
print "Value:%s" %dict1.setdefault('Sex',None)
