#! /usr/bin/python
# -*- coding: utf8 -*-
import sys
From=(sys.argv[1])
To=(sys.argv[2])
read=open(From, "r")
write=open(To, "w")
write.write(str.upper((read.read())))
print ("Done")
read.close()
write.close()