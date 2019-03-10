#-*-coding=utf-8 -*-
a=10
s=1
for i in range(1,11):
	s=s*i
print s


from functools import reduce

def chengfa(x,y):
	return x*y
a1=10
b1=reduce(chengfa,range(1,a1+1))
print b1