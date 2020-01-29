#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max_num = 0
  max_num_index = 0
  if len(prices) < 2:
    return 0
  # find the max num from index 1
  for i in range(1, len(prices)):
    if prices[i] > max_num:
      max_num = prices[i]
      max_num_index = i
  # if the index of the max = 1, return prices[1]-prices[0]
  if max_num_index == 1:
    return prices[1] - prices[0]

  # else find the smallest from 0 to the index of the max num, return prices[index of max]- prices[index of min]
  else:
    min_num = prices[0]
    for x in range(1, max_num_index):
      if prices[x] < min_num:
        min_num = prices[x]
    return max_num-min_num

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))