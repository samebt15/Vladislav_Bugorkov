#! /usr/bin/python
# -*- coding: utf8 -*-
import sys
file=(sys.argv[1])
open_file=open(file,"r")
l=0
for line in open_file:
	l=l+1
print ("Number of lines:", l)
open_file.close()