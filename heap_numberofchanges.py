def heapify(A, i, heapsize):
    l = 2 * i + 1
    r = 2 * i + 2
    if (r <= heapsize) and (A[l] > A[i]):
        largest = l
    else:
        largest = i
    if (r < heapsize) and (A[r] > A[largest]):
        largest = r
    if largest != i:
        print("0", end= " ")
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp
        heapify(A, largest, heapsize)


def build_heap(A):
    heapsize = len(A)
    for i in range((int(len(A) / 2)) + 1, -1, -1):
        heapify(A, i, heapsize)


def heapsort(A):
    build_heap(A)
    heapsize = len(A)
    print(" <- Te zera oznaczają ilość zamian, ponieższe nie są istotne")
    for i in range(len(A) - 1, -1, -1):
        temp = A[0]
        A[0] = A[i]
        A[i] = temp
        heapsize -= 1
        heapify(A, 0, heapsize)
    return A

print(heapsort(list(map(int, input().split()))))
