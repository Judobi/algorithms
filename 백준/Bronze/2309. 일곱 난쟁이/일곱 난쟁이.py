import random
import sys

tall = [0] * 9
for i in range(9):
  tall[i] = int(sys.stdin.readline())

while 1:
  result = random.sample(tall, 7)
  if sum(result) == 100:
    result = sorted(result)
    print(*result, sep='\n')
    break