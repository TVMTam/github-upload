'''Extracting Data With Regular Expressions
In this assignment you will read through and parse a file with text and numbers.
You will extract all the numbers in the file and compute the sum of the number.'''
box = input('Select File: ')
if len(box)>=1:
    box = 'regex_sum_207216.txt'
else:
    box = 'regex_sum_42.txt'

import re

handl = open(box)
numlist=[]
for line in handl:
    if not re.search('[0-9]', line):
        continue
    else:
        a = re.findall('[0-9]+', line)
        print (a)
    for i in range(len(a)):
        num = int(a[i])
        numlist.append(num)
print(numlist)
print ('#of numbers:',len(numlist))
print('Total:' ,sum(numlist))
