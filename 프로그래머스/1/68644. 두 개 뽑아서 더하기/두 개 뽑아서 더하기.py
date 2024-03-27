from itertools import combinations

def solution(numbers):
    arr = set()
    for comb in combinations(numbers,2):
        a,b = comb
        arr.add(a+b)
    arr = list(arr)
    arr.sort()
    return arr