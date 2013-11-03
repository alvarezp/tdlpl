#!/usr/bin/env python

import sys

i=1
count={}
while (i < len(sys.argv)):
	n=sys.argv[i]
	try:
		count[n]=count[n]+1
	except KeyError:
		count[n]=1
	i=i+1

howmany_of_populars=0
the_popular=-1
howmany_populars=0
for i in count:
	if count[i] == howmany_of_populars:
		howmany_populars = howmany_populars+1
	if count[i] > howmany_of_populars:
		the_popular = i
		howmany_of_populars = count[i]
		howmany_populars = 1

if howmany_populars > 1:
	print "invalid set"
else:
	print str(the_popular) + " " + str(howmany_of_populars)
