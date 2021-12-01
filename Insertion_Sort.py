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


A = [4,3,2,1]
insertion_sort_while(A)
print(A)
print("End")