#!/usr/bin/python
"""
player: 1:3 3**1
r
p
s

player: 2:9 3**2
rr
rp
rs
pr
pp
ps
sr
sp
ss

player: 3 : 27  3**3
"""


import sys

def rock_paper_scissors(n):
  # if n = 1 [['rock'], ['paper'], ['scissors']]
  # if n = 2, add [['rock'], ['paper'], ['scissors']] to the item in n(1),
  if n == 0:
    return [[]]
  elif n == 1:
    return [['rock'], ['paper'], ['scissors']]
  else:
    arr = [[]] * 3 ** n
    
    returned_arr = rock_paper_scissors(n - 1)
    x=0
    for i in range(len(returned_arr)):
      arr[x] = returned_arr[i] + ["rock"]
      x += 1
      arr[x] = returned_arr[i] + ["paper"]
      x += 1
      arr[x] = returned_arr[i] + ["scissors"]
      x += 1
    
    return arr

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]') 
