#!/usr/bin/env python

#Script_name: add_abund.py
#Description: Adds abundance to the contig name

import sys
d = {}
for line in open(sys.argv[1]):
    data = line.rstrip().split(' ')
    contig = data[0]
    med = float(data[1])
    if d.has_key(contig):
        d[contig].append(med)
    else:
        d[contig]  = med

for line in open(sys.argv[2]):
    if line.startswith('>'):
        datum = line.rstrip().split('\t')
        contig_name = datum[0][1:]
        if d.has_key(contig_name):
            print ">"+ contig_name + "_[cov=" + str(d[contig_name]) + "]"
    else: 
        print line[:-1]
