#!/usr/bin/env python

# script_name: core_2_out_of_2.py
# Description: Compares annotations from 2 files and prints the annotations found in all files
import sys

'''Usage python compare-cogs.py <file1> <file2> '''
first_file_set = set()
second_file_set = set()

for line in open(sys.argv[1]):
    #if line.startswith('mgm'):
    data1 = line.strip().split('\t')
    first_reads = data1[0]
        #print first_reads     
    first_file_set.add(first_reads)

for line in open(sys.argv[2]):
    #if line.startswith('mgm'):
    data2 = line.strip().split('\t')
    second_reads = data2[0]
    #print second_reads
    second_file_set.add(second_reads)

intersection = first_file_set.intersection(second_file_set)
first_file_only = first_file_set.difference(second_file_set)
second_file_only = second_file_set.difference(first_file_set)


for i in intersection:
    print i
