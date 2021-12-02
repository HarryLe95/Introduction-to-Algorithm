import numpy as np
import math 

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

def selection_sort(A):
    N = len(A)
    for i in range(N-1):
        key = A[i]
        for j in range(i+1,N): #Find current minimum
            if key > A[j]: #Make a swap if minimum found
                temp=key 
                key = A[j]
                A[j]= temp
        A[i] = key

def merge_subarrays(E,F,large_val=np.array([1e8])):
    N_E, N_F = len(E), len(F)
    i,j=0,0
    E = np.concatenate([E,large_val],0)
    F = np.concatenate([F,large_val],0)
    S = np.zeros(N_E+N_F)
    for k in range(N_E+N_F):
        if E[i]<F[j]:
            S[k]=E[i]
            i+=1
        else:
            S[k]=F[j]
            j+=1
    return S

def split_index_array(A):
    S = np.zeros(2*len(A)-1,dtype=np.int8)
    S[0] = A[0]
    i_S = 1
    for i_A in range(len(A)-1):    
        S[i_S] = np.ceil((A[i_A] + A[i_A+1])/2)
        S[i_S+1] = A[i_A+1]
        i_S+=2
            
    return S

def print_partitions(A,index_array):
    for i in range(len(index_array)-1):
        print(A[index_array[i]:index_array[i+1]])
    print("\n")

N = 7
A = np.arange(N)
A = A[::-1] 
index_array = np.array([0,N])
n_iter = int(np.ceil(np.log2(N)))



def get_index_array(k,N):
    I = np.arange(2**(k+1)+1)/2**(k+1)
    I = np.ceil(I*N)
    return I.astype(int)

def merge_sort_non_recursive(A):
    n_iter = int(np.ceil(np.log2(N)))    
    for i in range(n_iter):
        I = get_index_array(n_iter-i-1,N)
        for j in range(0,len(I)-1,2):
            E = A[I[j]:I[j+1]]
            F = A[I[j+1]:I[j+2]]
            A[I[j]:I[j+2]] = merge_subarrays(E,F)

def merge_sort_recursive(A,i_start=0,i_end=len(A)):
    i_mid = int(np.ceil((i_start+i_end)/2))
    if (i_end - i_start) > (i_mid-i_start): 
        merge_sort_recursive(A,i_start,i_mid)
        merge_sort_recursive(A,i_mid,i_end)
    A[i_start:i_end] = merge_subarrays(A[i_start:i_mid],A[i_mid:i_end])


merge_sort_recursive(A)
print(A)
print("End")