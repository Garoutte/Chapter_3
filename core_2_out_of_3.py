#!/usr/bin/env python

# script_name: core_2_out_of_3.py
# Description: Compares annotations from 3 files and prints the annotations found in at least 2 out of the 3 files

import sys

'''Usage python compare-cogs.py <file1> <file2>'''
first_file_set = set()
second_file_set = set()
third_file_set = set()
two_thirds_set = set()
for line in open(sys.argv[1]):
    #if line.startswith('mgm'):
    data1 = line.strip().split('\t')
    first_reads = data1[0]
    #print first_reads
    first_file_set.add(first_reads)
    
for line in open(sys.argv[2]):
    data2 = line.strip().split('\t')
    second_reads = data2[0]
    second_file_set.add(second_reads)
    
for line in open(sys.argv[3]):
    data3 = line.strip().split('\t')
    third_reads = data3[0]
    third_file_set.add(third_reads)
    
intersection = first_file_set.intersection(second_file_set, third_file_set)
first_file_only = first_file_set.difference(second_file_set, third_file_set)
second_file_only = second_file_set.difference(first_file_set, third_file_set)
third_file_only = third_file_set.difference(first_file_set, second_file_set)
first_and_second = first_file_set.intersection(second_file_set)
first_and_third = first_file_set.intersection(third_file_set)
second_and_third = second_file_set.intersection(third_file_set)
two_thirds_set.update(intersection, first_and_second, first_and_third, second_and_third) 

for i in two_thirds_set:
	print i
