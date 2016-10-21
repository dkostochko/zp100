#!/usr/bin/python
import sys
import string
import re

ins = open( "dumchar_info", "rb" )
outs = open( "scatter.txt", "wb" )
next(ins)
for line in ins:
    if line.startswith("Part_Name"):
        break
    linesp = re.split('\W+', line)
    name = linesp[0].upper()
    start = int(linesp[2],16)
    block = linesp[5]
    if block != 'misc':
        start = start + 0x600000
    outs.write(name + " " + string.replace(hex(start), "L", "") + "\n{\n}\n")
ins.close()
outs.close()
