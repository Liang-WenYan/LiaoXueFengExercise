# -*- coding: utf-8 -*-
def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    else:
        min = L[0]
        max = L[0]
        for value in L:
            if min >= value:
                min = value
            if max <= value:
                max = value
        return (min, max)
