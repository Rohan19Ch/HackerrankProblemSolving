#!/bin/python3

import os
import sys

#
# Complete the countSubstrings function below.
#
def substring(queryStr):
    res = [queryStr[i: j] for i in range(len(queryStr)) for j in range(i + 1, len(queryStr) + 1)]
    return res
def countSubstrings(s, queries):
    subStringsList = []
    for i in queries:
        left = i[0]
        right = i[1]
        newStr = s[left:right+1]
        print(newStr)
        sub_String = substring(newStr)
        print(sub_String)
        subStringsList.append(sub_String)
    print(subStringsList)
    finalStrList = []
    for i in subStringsList:
        res1 = []
        for j in i:
            if j not in res1:
                res1.append(j)
        print(res1)
        finalStrList.append(res1)
    print(finalStrList)
    lenList = []
    for i in finalStrList:
        lenList.append(len(i))
        print(lenList)
    return lenList
if __name__ == '__main__':

    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    s = input()

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = countSubstrings(s, queries)
    input()
