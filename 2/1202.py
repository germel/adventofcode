#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import io
import sys

def add(a, b, r):
    data[r] = data[a] + data[b]
    #print ('add: ', a, '->', data[a], b, '->', data[b], 'res -> ', data[r])

def mlt(a, b, r):
    data[r] = data[a] * data[b]
    #print ('mlt: ', a, '->', data[a], b, '->', data[b], 'res -> ', data[r])

def runme(data):
    for i in range(0, len(data), 4):
        cmd = data[i]
        if(cmd != 99):
            p1 = data[i+1]
            p2 = data[i+2]
            re = data[i+3]
        else:
            return data[0]

        if (cmd == 1):
            add(p1, p2, re)
        elif (cmd == 2):
            mlt(p1, p2, re)
        else:
            return data[0]

f = open('input.txt', 'r')

for line in f:
    data = line[:-1].split(',')

for i in range(0, len(data)):
    data[i] = int(data[i])
odata = data.copy()

print('Original dataset output: ', runme(data))

# Restore the gravity assist program (your puzzle input) to the "1202 program
# alarm" state it had just before the last computer caught fire. To do this,
# before running the program, replace position 1 with the value 12 and replace
# position 2 with the value 2.
data[1], data[2] = 12, 2
print('1202 error output: ', runme(data))

for x in range(0, 99):
    for y in range(0, 99):
        data = odata.copy()
        data[1], data[2] = x, y
        if (runme(data) == 19690720):
            print(data[0], 'data and verb', data[1], data[2])
            sys.exit()
