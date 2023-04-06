import sys
from itertools import permutations
input = sys.stdin.readline

n, k = int(input()), int(input())
cards = [input().rstrip() for _ in range(n)]
array = set()

for i in permutations(cards, k):
    array.add(''.join(i))
    
print(len(array))