#!/usr/bin/python3
import sys
from itertools import permutations

def main():
    next_biggest_number(sys.argv[1])

def next_biggest_number(num):
    #Turn hopefully valid number into a string
    num = str(num)

    #Get list of all unique permutations of digits in num
    unqPermList = list(set(permutations(num)))

    #Check all elements of unqPermList to see which ones are larger than num
    candidates = []
    for x in unqPermList:
        candidate = int(''.join(list(x)))
        if candidate > int(num):
            candidates.append(candidate)
            #If none are larger than return -1, otherwise return the minimum of the candiates list
    if not candidates:
        return -1
    else:
        return min(candidates)

if __name__ == "__main__":
    main()
