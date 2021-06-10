#include <stdio.h>
#include "utils.h"

int main(){
    int array[] = {1,23,5,6,4,2};
    int length = sizeof(array)/sizeof(array[0]);
    int *sort = insertion_sort(array,length);
    display(sort,length);
    return 0;
}