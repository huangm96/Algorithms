#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

def helper(big_arr,arr,n):
  print(arr)
  m = 0
  
  big_arr.append(arr)
  #print(big_arr)
  for i in range(n - 1):
    over3 = False
    arr1 = [0] * (n - 1)
    for x in range(len(arr1)):
      if x == m:
        arr1[x] = arr[m] + arr[m + 1]
        if arr1[x] > 3:
          over3 = True
          break
      else:
        if x < m:
          arr1[x] = arr[x]
        else:
          arr1[x] =arr[x+1]
    m += 1
    if over3 == True:
      break
    if not arr1 in big_arr and len(arr1) > 0 :
      helper(big_arr,arr1, n - 1)
  return big_arr

def eating_cookies(n, cache=None):
  big_arr = []
  big_arr=helper(big_arr,[1] * n, n)
  return len(big_arr)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
    


# def f(n):
#   arr=[1]*n
#   print(arr)
#   m=0
#   for i in range(n-1):
#     arr1 = [0] * (n - 1)
#     for x in range(len(arr1)):
#       if x == m:
        
#         arr1[x] = arr[m] + arr[m + 1]
        
#       else:
#         arr1[x] = arr[x]
#     m+=1
#     print(arr1)
    
big_arr=[]


def f2(arr, n):
  print(arr)
  m = 0
  if not arr in big_arr:
    big_arr.append(arr)
  print(big_arr)
  for i in range(n-1):
    arr1 = [0] * (n - 1)
    for x in range(len(arr1)):
      if x == m:
        arr1[x] = arr[m] + arr[m + 1]
      else:
        if x < m:
          arr1[x] = arr[x]
        else:
          arr1[x] =arr[x+1]
    m += 1
    if len(arr1) > 0 and max(arr1)<=3:
      f2(arr1,n-1)
    
    
