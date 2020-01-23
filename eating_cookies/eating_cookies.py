#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

# def helper(big_arr,arr,n):
#   print(arr)
#   m = 0
  
#   big_arr.append(arr)
#   #print(big_arr)
#   for i in range(n - 1):
#     over3 = False
#     arr1 = [0] * (n - 1)
#     for x in range(len(arr1)):
#       if x == m:
#         arr1[x] = arr[m] + arr[m + 1]
#         if arr1[x] > 3:
#           over3 = True
#           break
#       else:
#         if x < m:
#           arr1[x] = arr[x]
#         else:
#           arr1[x] =arr[x+1]
#     m += 1
#     if over3 == True:
#       break
#     if not arr1 in big_arr and len(arr1) > 0 :
#       helper(big_arr,arr1, n - 1)
#   return big_arr

# def eating_cookies_1(n, cache=None):
#   big_arr = []
#   big_arr=helper(big_arr,[1] * n, n)
#   return len(big_arr)

# 0: 1

# 1: 1
# 1

# 2: 2
# 11
# 2

# 3: 4
# 111
# 12
# 21
# 3

# 4: 7
# 1111
# 121
# 112
# 13
# 211
# 22
# 31


def eating_cookies(n, cache=None):
  cache={0:1,1:1,2:2}
  if not n in cache:
    cache[n]=eating_cookies(n-1,cache)+eating_cookies(n-2,cache)+eating_cookies(n-3,cache)
  return cache[n]


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
    



    
