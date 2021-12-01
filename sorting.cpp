#include <iostream>
using namespace std;

void insertion_sort(int A[], int N){
	for (int i = 1; i < N; i++){
		int key = A[i];
        int j = i - 1;
		for (;j >= 0; j--){
			if (key < A[j]){
				A[j+1]=A[j];
            }
			else{
				break;
			}
		}A[j+1]=key;
	}
}


void display(int A[], int N){
    for (int i = 0; i < N; i++){
        cout << A[i] << " ";
    }
    cout <<endl;
}


void insertion_sort_while(int A[], int N){
    for (int i = 1; i < N; i++){
        int key = A[i];
        int j = i-1;
        while (j >= 0 && key < A[j]){
            A[j+1]=A[j];
            j--;
        }
        A[j+1]=key;
    }
}

int main(){
    int A[] = {4,1,3,2};
    int N = sizeof(A)/sizeof(A[0]);
    insertion_sort_while(A,N);
    display(A,N);
}