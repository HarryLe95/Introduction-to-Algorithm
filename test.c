#include <stdio.h>
#include "utils.h"
#include <stdlib.h>

int main(){
    int array[] = {1,2,32,25,24,7,8,2};
    int length = sizeof(array)/sizeof(array[0]);
    int *sort = merge_sort(array,length);
    display(sort,length);
}