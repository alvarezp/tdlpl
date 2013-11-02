#!/usr/bin/env python

import sys
from math import sqrt

def isprime(n):
	i=2;
	while (i <= sqrt(n)):
		if n % i == 0:
			break
		i=i+1
	else:
		return "yes"
		return
	return "no"

i = int(sys.argv[1])
f = i + 9
p = ""
while (i <= f):
	p = p + isprime(i) + " "
	i=i+1

p = p + isprime(i)

print p
