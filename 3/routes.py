#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import io

def addpoints(direction, distance, points):
    distance += 1
    #print(direction, distance, points[-1:])
    tlist = []
    if (direction == 'R'):
        for i in range(1, distance):
            tlist += [[i, 0]]
    elif (direction == 'L'):
        for i in range(1, distance):
            tlist += [[-i, 0]]
    elif (direction == 'U'):
        for i in range(1, distance):
            tlist += [[0, i]]
    elif (direction == 'D'):
        for i in range(1, distance):
            tlist += [[0, -i]]
    else:
        sys.exit('The void swallowed you. Die, sucker!')

    last_position = points[-1:]
    for i in range (0, len(tlist)):
        points.append([tlist[i][0] + last_position[0][0], tlist[i][1] + last_position[0][1]])
    return True

f = open('input.txt', 'r')
o = f.readline()[:-1].split(',')
p = f.readline()[:-1].split(',')

#o = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
#p = ['U62','R66','U55','R34','D71','R55','D58','R83']
 
opoints, ppoints = [[0, 0]], [[0, 0]]
cabledistance = []
manhattandistance = []
while (len(o) > 0 and len(p) > 0):
    ov, od = o[0][0], int(o[0][1:])
    pv, pd = p[0][0], int(p[0][1:])
    o.pop(0)
    p.pop(0)
    addpoints(ov, od, opoints)
    addpoints(pv, pd, ppoints)

for i in range(1, (len(opoints))):
    for j in range(1, (len(ppoints))):
        if (opoints[i] == ppoints[j]):
            cabledistance.append(i+j)
            manhattandistance.append(abs(opoints[i][0])+abs(opoints[i][1]))

cabledistance.sort()
manhattandistance.sort()
print ('Shortest Manhattan distance is', manhattandistance[0], 'and shortest cable distance is', cabledistance[0])
