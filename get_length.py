#!/usr/bin/env python

# script_name: get_length.py
# Description: Get genome length

import sys 
for line in open(sys.argv[1]):
    if line.startswith('>'):
        data = line.rstrip().split('_')
        leng = data[4] 
        print line[1:-1] + '\t'+ leng
