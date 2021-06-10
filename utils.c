#include <stdio.h>
#include<stdlib.h>
#include "utils.h"

void display(int *array, int length){
    printf("Displaying array: ");
    for (int i =0;i<length;i++){
        printf("%d ",array[i]);
    }
    printf("\n");
}

void arraycpy(int *src, int *dst, int start, int end){
    // Copy elements from src to dst - index from start including up to end - 1 (does not copy end)
    int j = 0;
    for (int i = start; i < end; i++){
        dst[j] = src[i];
        j++;
    }
}

int* insertion_sort(int *array, int length){
    int *sort = malloc(sizeof(int)*length);
    sort[0] = array[0];
    for (int i = 1; i < length; i++){
        int key = array[i];
        for (int j = i - 1; j >= 0; j--){
            if (sort[j]>key){
                sort[j+1]=sort[j];
            }else{
                sort[j+1]=key;
                break;
            }
        }
    }
    return sort;
}

void merge(int *array, int start, int mid, int end){
    int length_start = mid - start + 1;
    int length_end   = end - mid ;
    int *start_array = malloc(sizeof(int)*(length_start+1));
    int *end_array = malloc(sizeof(int)*(length_end+1));
    arraycpy(array,start_array,start,mid+1);
    arraycpy(array,end_array,mid+1,end+1);
    start_array[length_start]=1e8;
    end_array[length_end]=1e8;

    int i = 0, j = 0, k = 0; 
    for (k = start; k <= end; k++){
        if (start_array[i]>end_array[j]){
            array[k] = end_array[j];
            j++;
        }else{
            array[k] = start_array[i];
            i++;
        }
    }
}

void mergeSort(int *array, int start, int end){
    if (end > start){
        int mid = (end+start)/2;
        mergeSort(array,start,mid);
        mergeSort(array,mid+1,end);
        merge(array,start,mid,end);
    }
}

int *merge_sort(int *array, int length){
    int *sort = malloc(sizeof(int)*length);
    arraycpy(array,sort,0,length);
    mergeSort(sort,0,length-1);
    return sort;
}