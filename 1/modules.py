#!/usr/bin/env python
# -*- coding:utf-8 -*-

fuel = 0
ff = 0

m = open ('input.txt', 'r')

for line in m:
    f = int(int(line)/3)-2
    fuel += f
    while f >= 2:
        f = f/3-2
        if f > -1:
            ff += f

print('fuel:', fuel)
print('Fuel for fuel: ', ff)
print('Total fuel: :', ff+fuel)
