import numpy as np

def insertion_sort(A):
    for i in range(1,len(A)):
        key = A[i]
        for j in range(i-1,-2,-1):
            if (key < A[j]):
                A[j+1]=A[j]
            else:
                break
        A[j+1] = key

def insertion_sort_while(A):
    for i in range(1,len(A)):
        key=A[i]
        j = i - 1
        while key < A[j] and j >= 0:
            A[j+1]=A[j]
            j=j-1
        A[j+1]=key

def reverse_sort(A):
    for i in range(len(A)-2,-1,-1):
        key = A[i]
        j = i + 1
        while (j < len(A) and key < A[j]):
            A[j-1]=A[j]
            j=j+1
        A[j-1]=key

def linear_search(A,v):
    for i in range(len(A)):
        if A[i]==v:
            return i
    return -1


def binary_addition(A,B):
    if len(A) != len(B):
        N = max(len(A),len(B))
        A = np.concatenate([np.zeros(N-len(A)),A],0)
        B = np.concatenate([np.zeros(N-len(B)),B],0)
    N = len(A)
    C = np.zeros(N+1,dtype=np.int8)
    for i in range(N-1,-1,-1):
        C[i+1] = A[i] + B[i]
        if C[i+1] > 1:
            C[i+1] = 0
            C[i] = 1
    return C


def b2d(B):
    N = len(B)
    d = 0
    for i in range(N-1,-1,-1):
        d += pow(2,N-1-i)*B[i]
    return d

def d2b(d):
    if d == 0:
        return np.array([])
    N = int(np.floor(np.log2(d))+1)
    B = np.zeros(N,dtype=np.int8)
    for i in range(N-1,-1,-1):
        if d >= pow(2,i):
            B[N-1-i]=1
            d -= pow(2,i)
    return B

A = d2b(34)
B = d2b(4)
C = binary_addition(A,B)
print(b2d(C))
print("End")