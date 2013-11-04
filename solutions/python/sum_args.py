#!/usr/bin/env python

import sys

sum_=0
for i in sys.argv[1:]:
	sum_ = sum_ + int(i)

print sum_
