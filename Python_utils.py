import numpy as np 
import math 
from itertools import permutations
from typing import Union
from colorama import Fore, Style
import copy

def linear_search(array:np.array,value:Union[int,float],direction:str="forward",criterion:str="equal",*args,**kwargs):
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
            
def insertion_sort(array:np.array,search_method:str="linear",*args,**kwargs):
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

def selection_sort(array:np.array,*args,**kwargs):
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

def bubble_sort(array:np.array,*args,**kwargs):
    """Perform Bubble Sort. For every iteration, iterate from the end of the array to the current index and swap values
    so that the current index has the smallest value of the searched terms.

    Args:
        array (np.array): array to be sorted

    Returns:
        [type]: sorted array
    """
    for i in range(len(array)-1):
        for j in range(len(array)-1,i,-1):
            if array[j] < array[j-1]:
                array[j],array[j-1] = array[j-1],array[j]
    return array 
    
def merge(array:np.array,start_idx:int,mid_idx:int,end_idx,*args,**kwargs):
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
    return array

def merge_inplace(array:np.array,start_idx:int,mid_idx:int,end_idx:int,*args,**kwargs):
    """In-place merging of two sub-arrays in merge sort. (No intermediate array is created)
    First sub-array: array[start_idx:mid_idx]
    Second sub-array: array[mid_idx:end_idx]
    Note that the last idx in np array is exclusive.
    Args:
        array (np.array): array to be sorted
        start_idx (int): start idx of 1st subarray (inclusive)
        mid_idx (int): end idx of 1st subarray (exclusive) and start idx of 2nd sub array (inclusive)
        end_idx ([type]): end idx of 2nd subarray (exclusive)
    """
    first_sub_counter = mid_idx-start_idx
    for i in range(start_idx,end_idx):
        if array[i] >= array[mid_idx]:
            temp=array[mid_idx]
            array[i+1:mid_idx+1]=array[i:mid_idx]
            array[i] = temp
            mid_idx+=1
            if mid_idx >= end_idx:
                break
        else:
            first_sub_counter-=1
            if first_sub_counter==0:
                break
    return array

def merge_sort(array:np.array,*args,**kwargs):
    """Merge sort - non recursive version. Construct index array to guide the merging process
    -i.e the final merge's index array:
    [0, ceil[(0+length)/2], length]
    The index array is computed formulaicly.
    Args:
        array (np.array): array to sort

    Returns:
        array: sorted array
    """
    max_div = math.ceil(np.log2(len(array)))
    for i in range(max_div):
        #Construct index array to merge
        index_array = np.ceil(np.arange(0,np.power(2,max_div-i)+1)/np.power(2,max_div-i)*len(array)).astype(int)
        for i in range(0,len(index_array)-2,2):
            merge(array,index_array[i],index_array[i+1],index_array[i+2])
    return array
    
def merge_sort_recursive(array:np.array,start_idx:int,end_idx:int,*args,**kwargs):
    """Merge Sort - the recursive version

    Args:
        array (np.array): array to be sorted
        start_idx (int): starting index
        end_idx (int): end index

    Returns:
        [type]: sorted array
    """
    mid_idx = math.ceil((start_idx+end_idx)/2)
    if (mid_idx-start_idx) < (end_idx - start_idx):
        merge_sort_recursive(array,start_idx,mid_idx)
        merge_sort_recursive(array,mid_idx,end_idx)
    merge(array,start_idx,mid_idx,end_idx)
    return array 

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
        return 0
    else:
        print(f"{Fore.RED}Test failed. Expected:{expected}, Actual:{actual}, Direction:{direction}, criterion:{criterion}")
        print(f"Array: {array}, Value: {value}{Style.RESET_ALL}")
        return 1
    
def unit_test(array,values,index,direction,criterion,*args,**kwargs):
    error_count = 0
    for val in values:
        mask = compare(array,val,criterion)
        masked_index = index[mask]
        if direction == "forward":
            expected_output=masked_index[0] if len(masked_index)>0 else -1
        if direction == "backward":
            expected_output=masked_index[-1] if len(masked_index)>0 else -1
        actual_output=F(array,val,direction,criterion,*args,**kwargs)
        error_count+=check_output(expected_output,actual_output,direction,criterion,array,val)
    return error_count

def test_search(F,*args,**kwargs):
    error_count=0
    array = np.arange(-5,5)
    array = np.concatenate([array,array[::-1]],axis=0)
    N = len(array)
    values = np.random.choice(array,int(N/2),replace=False)
    index  = np.arange(N)
    #Forward-equal
    error_count+=unit_test(array,values,index,direction="forward",criterion="equal",*args,**kwargs)
    #Forward greater
    error_count+unit_test(array,values,index,direction="forward",criterion="greater",*args,**kwargs)         
    #Forward less
    error_count+unit_test(array,values,index,direction="forward",criterion="less",*args,**kwargs)
    #Forward geq
    error_count+unit_test(array,values,index,direction="forward",criterion="greater equal",*args,**kwargs)
    #Forwarg leq
    error_count+unit_test(array,values,index,direction="forward",criterion="less equal",*args,**kwargs)
    #Backward equal
    error_count+unit_test(array,values,index,direction="backward",criterion="equal",*args,**kwargs)
    #Backward greater
    error_count+unit_test(array,values,index,direction="backward",criterion="greater",*args,**kwargs)
    #Backward less
    error_count+unit_test(array,values,index,direction="backward",criterion="less",*args,**kwargs)
    #Backward geq
    error_count+unit_test(array,values,index,direction="backward",criterion="greater equal",*args,**kwargs)
    #Backward leq
    error_count+unit_test(array,values,index,direction="backward",criterion="less equal",*args,**kwargs)
    if error_count==0:
        print(f"{Fore.GREEN}All tests passed!{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}{copy.error} failed test(s)!{Style.RESET_ALL}")

def test_sort(F,*args,**kwargs):
    error_count=0
    array = np.random.randint(-100,100,[6])
    expected_output = np.sort(array)
    perms = permutations(array)
    for perm in perms:
        N = len(perm)
        actual_output = F(np.array(perm),start_idx=0,end_idx=N,*args,**kwargs)
        if np.all(expected_output==actual_output):
            print(f"{Fore.GREEN}Test passed{Style.RESET_ALL}")
        else:
            print(f"Test failed. Expected: {expected_output}, Actual: {actual_output}")
            error_count+=1
    if error_count==0:
        print(f"{Fore.GREEN}All tests passed!{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}{copy.error} failed test(s)!{Style.RESET_ALL}")

def test_merge(F,*args,**kwargs):
    error_count = 0
    array = np.random.randint(-100,100,[6])
    expected_output = np.sort(array)
    end_idx = len(array)
    mid_idx = math.ceil(end_idx/2)
    permutes = permutations(array)
    for perm in permutes:
        p_array = np.array(perm)
        p_array[0:mid_idx] = np.sort(p_array[0:mid_idx])
        p_array[mid_idx:end_idx] = np.sort(p_array[mid_idx:end_idx])
        output = F(p_array,0,mid_idx,end_idx)
        if np.all(output==expected_output):
            print(f"{Fore.GREEN}Test Passed!{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Test Failed. Expected: {expected_output}, Actual: {output}, Array: {p_array}{Style.RESET_ALL}")
            error_count+=1
    if error_count==0:
        print(f"{Fore.GREEN}All tests passed!{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}{copy.error} failed test(s)!{Style.RESET_ALL}")

if __name__ == "__main__":
    F = bubble_sort
    test_sort(F)

    print("End")