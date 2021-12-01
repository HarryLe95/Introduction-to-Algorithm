# Introduction to Sorting
## Why learn algorithm and data structure
In general, algorithm is a well-defined procedure with given input and expected output. More concretely, an algorithm defines a set of actions to be taken in a prescribed order that will transform the required inputs to the desired outputs. The ***sorting*** problem and its associated algorithms are often used as an introduction for beginning students, given its relevance in many areas of computer science. The problem is presented as follows: 

***Input***: A sequence $A$ of $n$ numbers $<a_0,a_1,\dots,a_n>$.
***Output***: A sequence $A'$ that is a reodering of $A$ such that $a'_0 \leq a_1' \leq \dots \leq a_n'$. 

The focus of this course, however, is not on the recognition or the memorisation of well-known sorting algorithms (though doing so does not hurt), but on the understanding of the tools for analysing algorithms. As you can tell from experience, solutions in computer science are often not unique: there are many ways to arrive at the same output. However, depending on the context, some solution are "better" than the others. Algorithm analysis allows us to analyse the strengths and weaknesses of different solution, hence to select the right algorithm for a given task. 

## Chapter layout
We will begin by looking at two variants of sorting algorithms - insertion sort and merge sort. We will then look at some of the tools for analysing algorithms, the first of which is the loop invariant which allows us to show whether an algorithm is correct. The second is running time analysis that introduces us to the big $O$ notation that is often seen in computer science.

## Insertion Sort
The algorithm works by initialising two arrays:
- Array $A$ with elements that need to be sorted.
- Array $A'$ intially empty or intialised with the first element of $A$.

At every loop iteration, we will pick an element to be removed from $A$ and insert it at an appropriate location in $A'$ such that  $A'$ will be in a sorted arrangement. This can be done by checking that element (hereon refered as $a_i$) against elements $a_j'$ starting from the last position (the largest element of $A'$). If $a_i \geq a_j'$ then $a_i$ is inserted at index $j+1$, otherwise, $j$ is decreased by one the the process continues until termination, when the condition is met, or when every element in $A'$ has been scanned, in which case $a_i$ is inserted to the first index. At this point, it is useful to think about an efficient way to do insertion. When inserting $a_i$ to index $j$ of  $A'$, we are basically doing the following: 
- Index incrementation for indices that come after $j$: $a_{k+1}' = a_k'$ for $k \geq j$
- Assignment: $a_j'=a_i$

A naiive way to implement this is to run the previously described process until the inserting index is found and then do index incrementation and assignment. A more efficient way is to do a swap operation at every comparison step if the comparison is not true: if $a_i < a_j'$ then $a_{j+1}'=a_{j}$ and $a_j' = a_i$. An illustration for insertion sort is provided as follows: (figure reproduced from CLRS)![[Pasted image 20211130223823.png]]

#### Pseudo-code for Insertion Sort
```
**Insertion Sort Algorithm**
Input: array A of N elements
Output: array A sorted in increasing order 
-------------------------------------------
for i from 1 to N-1:
	key = A[i]
	j = i - 1
	while j >= 0 and key < A[j]
		A[j+1] = A[j]
		j--
	A[j+1]=key
```

	
#### C/C++ Implementation
```
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

```

#### Python Implementation
```
def insertion_sort(A:
	for i in range(1,len(A)):
		key=A[i]
		j = i - 1
		while key < A[j] and j >= 0:
			A[j+1]=A[j]
			j=j-1
		A[j+1]=key
```

### Loop invariant
Loop invariant is a framework for proving that an algorithm is correct. An algorithm is correct if for every instance, its termination leads to the desired output. There are three main components of any loop invariant proof:

- **Initialisation**: it is true at the begining of the loop.
- **Maintenance**: if it's true before an iteration of the loop, then it is true before the next iteration begins.
- **Termination**: it remains true when the loop ends. 

#### Proof of Loop Invariant Property 
The property that we wants to show is that from initialisation to termination, the sub array A[0:i] is always correctly sorted.
- Initialisation: when i = 1, the array A[0] is correctly sorted.
- Maintenance: when i > 1, A[0:i] is correctly sorted by construction. It is possible to make a proof by contradiction here. 
- Termination: the algorithm terminates when it has scanned through all elements of A. Since we have built a sub-array A[0:N] that is correctly sorted, A is then correctly sorted. 