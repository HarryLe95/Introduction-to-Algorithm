import numpy as np 
import math 
from itertools import permutations
from typing import Union
from colorama import Fore, Style
import copy

def linear_search(array:np.array,value:Union[int,float],direction:str="forward",criterion:str="equal"):
    """Search an array in an element-wise manner in the given direction and return outputs based on given criterion

    Args:
        array (np.array): Search array
        value (Union[int,float]): Search value
        direction (str, optional): either ["forward","backward"]. Forward searches from the first to last element. Defaults to "forward".
        criterion (str, optional): among ["greater","less","greater equal","less equal", "equal"]. Defaults to "equal".
    Output:
        The first index in the given direction that first satisfies the given criterion, otherwise -1
    """
    assert direction in ["forward","backward"] 
    assert criterion in ["greater","less","greater equal","less equal", "equal"]
    N = len(array)
    for i in range(N):
        if direction == "forward":
            key = array[i]
            if compare(key,value,criterion):
                return i
        if direction == "backward":
            key = array[N-i-1]
            if compare(key,value,criterion):
                return N-i-1
    return -1
 
def insertion_sort(array:np.array,search_method:str="linear"):
    """Perform insertion sort. At every iteration, backtrack and find the index of the first element less than current value,
       then insert by advancing right. 
    Args:
        array (np.array): array to sort
        search_method (str, optional): backtrack search method. Defaults to "linear".
    Returns:
        A (np.array): sorted array
    """
    N = len(array)
    A = copy.deepcopy(array)
    for i in range(1,N):
        key = A[i]
        if search_method == "linear":
            insert_index = linear_search(A[:i],key,direction="backward",criterion="less")
        A[insert_index+2:i+1] = A[insert_index+1:i]
        A[insert_index+1] = key
    return A

def selection_sort(array:np.array):
    """Perform selection sort. At every iteration, find the minimum element of the sliced array 
    and swap with the value at current iteration.1
    Args:
        array (np.array): array to sort

    Returns:
        A [np.array]: sorted array
    """
    N = len(array)
    A = copy.deepcopy(array)
    for i in range(N-1):
        index = np.argmin(A[i:])+i #Find index with min value (+i to adjust for array slicing)
        #Swap values
        A[i], A[index]=A[index], A[i]
    return A

def merge(array:np.array,start_idx:int,mid_idx:int,end_idx):
    """Merging of two sub-arrays in merge sort.
    First sub-array: array[start_idx:mid_idx]
    Second sub-array: array[mid_idx:end_idx]
    Note that the last idx in np array is exclusive.
    Args:
        array (np.array): array to be sorted
        start_idx (int): start idx of 1st subarray (inclusive)
        mid_idx (int): end idx of 1st subarray (exclusive) and start idx of 2nd sub array (inclusive)
        end_idx ([type]): end idx of 2nd subarray (exclusive)
    """
    sub_1 = np.array(array[start_idx:mid_idx],copy=True)
    sub_2 = np.array(array[mid_idx:end_idx],copy=True)
    idx_1, idx_2 = 0, 0
    for i in range(start_idx,end_idx):
        if idx_1 >= mid_idx-start_idx:
            array[i:end_idx] = sub_2[idx_2:]
            break
        if idx_2 >= end_idx-mid_idx:
            array[i:end_idx] = sub_1[idx_1:]
            break
        if sub_1[idx_1] < sub_2[idx_2]:
            array[i] = sub_1[idx_1]
            idx_1+=1
        else:
            array[i] = sub_2[idx_2]
            idx_2+=1        

def merge_inplace(array:np.array,start_idx:int,mid_idx:int,end_idx:int):
    """In-place merging of two sub-arrays in merge sort.
    First sub-array: array[start_idx:mid_idx]
    Second sub-array: array[mid_idx:end_idx]
    Note that the last idx in np array is exclusive.
    Args:
        array (np.array): array to be sorted
        start_idx (int): start idx of 1st subarray (inclusive)
        mid_idx (int): end idx of 1st subarray (exclusive) and start idx of 2nd sub array (inclusive)
        end_idx ([type]): end idx of 2nd subarray (exclusive)
    """
    i, j = start_idx, mid_idx
    temp_1, temp_2 = array[i],array[j]
    for k in range(start_idx,end_idx):
        if temp_1 < temp_2:
            i = i + 1  
            temp = array[i] if i < mid_idx else 1e9
            array[k]= temp_1
            temp_1 = temp
        else:
            j = j + 1 
            temp = array[j] if j < end_idx else 1e9
            array[k] = temp_2
            temp_2 = temp
        print(array,temp_1,temp_2,i,j)
            

def compare(a,b,criterion:str):
    # Function to compare a against b based on criterion (
    # Criterion is one of  ["greater","less","greater equal","less equal", "equal"])
    # Return boolean output
    if criterion == "greater":
        return a > b
    if criterion == "less":
        return a < b
    if criterion == "greater equal":
        return a >= b
    if criterion == "less equal":
        return a <= b
    if criterion == "equal":
        return a == b

def check_output(expected,actual,direction,criterion,array,value):
    if expected==actual:
        print(f"{Fore.GREEN}Test passed{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Test failed. Expected:{expected}, Actual:{actual}, Direction:{direction}, criterion:{criterion}")
        print(f"Array: {array}, Value: {value}{Style.RESET_ALL}")

def unit_test(array,values,index,direction,criterion,*args,**kwargs):
    for val in values:
        mask = compare(array,val,criterion)
        masked_index = index[mask]
        if direction == "forward":
            expected_output=masked_index[0] if len(masked_index)>0 else -1
        if direction == "backward":
            expected_output=masked_index[-1] if len(masked_index)>0 else -1
        actual_output=F(array,val,direction,criterion,*args,**kwargs)
        check_output(expected_output,actual_output,direction,criterion,array,val)
 
def test_search(F,*args,**kwargs):
    array = np.arange(-5,5)
    array = np.concatenate([array,array[::-1]],axis=0)
    N = len(array)
    values = np.random.choice(array,int(N/2),replace=False)
    index  = np.arange(N)
    #Forward-equal
    unit_test(array,values,index,direction="forward",criterion="equal",*args,**kwargs)
    #Forward greater
    unit_test(array,values,index,direction="forward",criterion="greater",*args,**kwargs)         
    #Forward less
    unit_test(array,values,index,direction="forward",criterion="less",*args,**kwargs)
    #Forward geq
    unit_test(array,values,index,direction="forward",criterion="greater equal",*args,**kwargs)
    #Forwarg leq
    unit_test(array,values,index,direction="forward",criterion="less equal",*args,**kwargs)
    #Backward equal
    unit_test(array,values,index,direction="backward",criterion="equal",*args,**kwargs)
    #Backward greater
    unit_test(array,values,index,direction="backward",criterion="greater",*args,**kwargs)
    #Backward less
    unit_test(array,values,index,direction="backward",criterion="less",*args,**kwargs)
    #Backward geq
    unit_test(array,values,index,direction="backward",criterion="greater equal",*args,**kwargs)
    #Backward leq
    unit_test(array,values,index,direction="backward",criterion="less equal",*args,**kwargs)
    
def test_sort(F,*args,**kwargs):
    array = np.random.randint(-100,100,[6])
    expected_output = np.sort(array)
    perms = permutations(array)
    for perm in perms:
        actual_output = F(np.array(perm),*args,**kwargs)
        if np.all(expected_output==actual_output):
            print(f"{Fore.GREEN}Test passed{Style.RESET_ALL}")
        else:
            print(f"Test failed. Expected: {expected_output}, Actual: {actual_output}")

if __name__ == "__main__":
    A = np.array([1,3,16,19,21,2,5,7,8,11])
    print(A[0:math.ceil(len(A)/2)],A[math.ceil(len(A)/2):len(A)])
    merge_inplace(A,0,math.ceil(len(A)/2),len(A))
    print(A)
    print("End")