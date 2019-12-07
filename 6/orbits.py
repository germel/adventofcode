#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import io

rh = []
orb = {}
res = 0

patha = []
pathb = []

def find_parent(n, u):
    for i in u:
        if n in u[i]:
            return i
    return -1

points = open("input.txt", 'r')

for line in points:
    orbrl = line[:-1].split(')')
    if orbrl[0] in orb and orbrl[1] not in orb[orbrl[0]]:
        orb[orbrl[0]] = orb[orbrl[0]] + [orbrl[1]]
    else:
        orb[orbrl[0]] = [orbrl[1]]

for key in orb:
    if orb[key] not in rh:
        rh = rh + orb[key]

for i in rh:
    sigma = 0
    parent = find_parent(i, orb)
    while (parent != -1):
        sigma += 1
        parent = find_parent(parent, orb)
    res += sigma
print('The sum of direct and indirect orbits is: ', res)

def find_path(a, b):
    patha, pathb  = [a], [b]
    parenta = find_parent(a, orb)
    while (parenta != -1):
        patha += [parenta]
        parenta = find_parent(parenta, orb)
    patha.reverse()
    parentb = find_parent(b, orb)
    while (parentb != -1):
        pathb += [parentb]
        parentb = find_parent(parentb, orb)
    pathb.reverse()
    # Discard common paths in patha and pathb
    while True:
        if patha[0] == pathb[0]:
            patha.pop(0)
            pathb.pop(0)
        else:
            return patha, pathb

patha, pathb = find_path('YOU', 'SAN')

pathlen = len(patha) + len(pathb) -2 # -1 hop fom each path

print('To travel from YOU to SAN you have to go hop ', pathlen, 'orbits.')
