#!/usr/bin/python

import re
from _ast import Num

"""
Example for Match and Search
re.I: performs Case-insensitive matching
re.M: Make $ match the end of line (not just the end of the string), and make ^match the start of any line (not just the start of the string).
"""
line = "Cats are smater then dogs"
matchObj=re.match(r'(.*) are (.*?) .*',line,re.M|re.I) 

if matchObj:
    print "matchObj.group():", matchObj.group()
    print "matchObj.group(1):",matchObj.group(1)
    print "matchObj.group(2):",matchObj.group(2)

else:
    print "no match!"
 

matchObj=re.match(r'dogs',line,re.M|re.I)   

if matchObj:
    print "match --> matchObj.group():", matchObj.group()
else:
    print "No match"
    
searchObj = re.search(r'dogs',line,re.M|re.I)
if searchObj:
    print "serarch --> searchObj.group():",searchObj.group()
else:
    print "Nothing Founc"

"""
Example for Search and Replace
"""
phone ="2004-959-559 # this is phone number"

#delete Python style Comment

num=re.sub(r'#.*$',"",phone)

print "Phone Num:",num

#remove anything other then digits
num=re.sub(r'\D',"",phone)
print "Phone Num:",num



""" 
belows are Regular - Expression Examples
"""

str_contents= "I am studying Python now, and it will be ended today. I will be studying basic tomorrow.too"

#str_expression=r'.*ing\s[Pp]ython\s'
#str_expression=r'\sno[wu]'
#str_expression=r'[a-zA-Z0-9]'
#str_expression=r'[^aeiou]'
#str_expression=r'[^AEIOU]'
str_expression=r'[Pp]ytho?|[Bb]asi?\w\Z'
#reg_option=re.M|re.I
reg_option=re.M
matchObj= re.match(str_expression,str_contents,reg_option)
if matchObj:
    print "match --> matchObj.group():", matchObj.group()
else:
    print "No match"
    
searchObj= re.search(str_expression,str_contents,reg_option)
if searchObj:
    print "search --> searchObj.group():", searchObj.group()
else:
    print "No search"
    






