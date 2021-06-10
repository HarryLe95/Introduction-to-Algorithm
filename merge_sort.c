#include <stdio.h>
#include "utils.h"
#include <stdlib.h>

int main(){
    int array[] = {9,8,1,2,3,5,4,10,11,6,7};
    int length = sizeof(array)/sizeof(array[0]);
    int *sort = merge_sort(array,length);
    display(sort,length);
}