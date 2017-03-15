#! /usr/bin/python
# -*- coding: utf8 -*-
import sys
import math
a=float(sys.argv[1])
b=float(sys.argv[2])
c=float(sys.argv[2])
if len (sys.argv)>4:
	print ("Введено много параметров")
	sys.exit(1)
D=b*b-4*a*c
print ("Квадратное уравнение: {0}*x^2+{1}*x+{2}=0".format(a,b,c))
if D==0:
	x1=(-b)/(2*a)
	q=a*x1*x1+b*x1+c
	print ("Первый корень", x1)
	print ("Решение при корне x1", q)
elif D>0:
	x1=(-b+math.sqrt(D))/(2*a)
	x2=(-b-math.sqrt(D))/(2*a)
	q1=a*x1*x1+b*x1+c
	q2=a*x2*x2+b*x2+c
	print ("Первый корень", x1)
	print ("Второй корень", x2)
	print ("Решение при x1", q1)
	print ("Решение при x2", q2)
else:
	print ("Нет корней")