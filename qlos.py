import random
from timeit import default_timer as timer
from datetime import timedelta
import sys
sys.setrecursionlimit(10**6)


class quick():

    def __init__(self, tab, piw):
        self.A = tab
        self.P = piw

    def quicksort_pomoc(self, A, p, r):
        if(p < r):
            q = self.partitionrand(A, p, r)
            self.quicksort_pomoc(A, p, q)
            self.quicksort_pomoc(A, q + 1, r)

    def partitionrand(self, A, p, r):
        randpivot = self.P  # random.randrange(p, r) #PODAJ PIWOT
        print("Element piwot:", A[randpivot],
              "   Indeks w tablicy: ", randpivot)
        A[p], A[randpivot] = A[randpivot], A[p]
        return self.partition(A, p, r)

    def partition(self, A, p, r):
        pivot = p
        i = p - 1
        j = r + 1
        while True:
            while True:
                i = i + 1
                if A[i] >= A[pivot]:
                    break
            while True:
                j = j - 1
                if A[j] <= A[pivot]:
                    break
            if i >= j:
                return j
            A[i], A[j] = A[j], A[i]

    def quicksort(self, A):
        self.quicksort_pomoc(A, 0, len(A) - 1)
        return A
