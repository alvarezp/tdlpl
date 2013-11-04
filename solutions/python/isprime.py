#!/usr/bin/env python

import sys
from math import sqrt

n=int(sys.argv[1])
i=2;
while (i <= sqrt(n)):
	if n % i == 0:
		break
	i=i+1
else:
	print "prime"
	sys.exit(0);

print "not prime"
