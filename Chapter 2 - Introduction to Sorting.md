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
```Pseudo-code
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
```C++
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
```python
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

### Exercise
- Rewrite insertion sort to produce non-increasing instead of non-decreasing order.

	```Python
	def reverse_sort(A):
		for i in range(len(A)-2,-1,-1):
			key = A[i]
			j = i + 1
			while (j<len(A) and key < A[j]):
				A[j-1]=A[j]
				j=j+1
			A[j-1]=key
	```

- Consider the searching problem: 
	- **Input**: $A = <a_0,\dots,a_N>$ and a value $v$
	- **Output**: index $i$ such that $A[i]==v$ or $-1$ if does not exist.
	- Write pseudo code for **linear search** which scans through the sequence looking for $v$.
	- Prove using **loop invariant** that the algorithm is correct.

	 ```Python
	 def linear_search(A,v):
	    i = -1
		for i in range(len(A)):
			if A[i]==v:
				return i
		return -1
	 ```
	 
	 ```Text
	 Proof using loop invariant concept: 
	 We prove that using the linear search algorithm, the correct 
	 answer has already been provided, otherwise -1.
	 Initialisation: set i = -1: trivially correct since we haven't
	 found the matching instance.
	 Maintenance: If at the beginning of each loop, the matching
	 element/index has not been found, then by the end of the loop
	 iteration, the index has either been found - returned or set 
	 to -1. 
	 Termination: Also trivial since if the index has been found
	 -> Returned, otherwise it has scanned through all elements
	 without finding the matching index. Hence return -1.
	 ```
- Consider the problem of adding two n-bit integers, stored in two n-element arrays A and B. The sum should be stored in binary form in (n+1) element array C. Write pseudo code. 

	```Python
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
	```
	Some functions for testing: 
	```Python
	def d2b(d):
		#Converts declimal to binary
		if d == 0: 
			return np.array([])
		N = int(np.floor(np.log2(d))+1)
		B = np.zeros(N,dtype=np.int8)
		for i in range(N-1,-1,-1):
			if d >= pow(2,i):
				B[N-1-i]=1
				d-=pow(2,i)
		return B
	```
	
	```Python
	def b2d(B):
		#Converts binary to decimal
		N = len(B)
		d = 0 
		for i in range(N-1,-1,-1):
			d+= pow(2,N-1-i)*B[i]
		return d
	```
	
### Analysing algorithms:
Actual time taken for an execution of an algorithm varies based on the underlying software and hardware. What is often more useful is to think about is the number of calculations that the computer needs to carry out for a given algorithm. This can be measured in the number of multiplication, addition, and other operations carried out, but we can abstract away this concept by thinking about how such number changes with an increase in the amount of input data. Here, analysis is often simplified using the notion of input size. Assuming that each operation costs the computer an amount of $c$ seconds (c is often a random variable), we will show later on that instead of using a messy formulation of computation cost with a lot of $c$, we can abstract away the idea using the big O notion. 

Let's provide an example by analysing the run time of insertion sort: 

```Pseudo-code
**Insertion Sort Algorithm**
Input: array A of N elements
Output: array A sorted in increasing order 
-------------------------------------------
Command:							Cost:	Times:
for i from 1 to N-1:				c1		N
	key = A[i]						c2		N-1
	j = i - 1						c3		N-1
	while j >= 0 and key < A[j]		c4		(sum from 1 to N-1)*t_i
		A[j+1] = A[j]				c5		(sum from 1 to N-1)*(t_i-1)
		j--							c6     	(sum from 1 to N-1)*(t_i-1)
	A[j+1]=key						c7		N-1
```
Assuming that the for and while loop exit by doing a comparison check (-i.e if the exit condition is met), then the number of times to taken to run through an N-iteration loop is N+1 instead of N like the usual operations. Note that the third column times shows the total number of times that the computer execute this line, hence the times for an inner loop should be multiplied by the number of iterations taken by the outter loops. $t_i$ shows the number of times the inner while loop is executed - i.e. when $i=1$, the maximum nHence for the worst case analysis, we can have: 

$$T(n) = (c_1+c_2+c_3+c_7)*N - (c_2+c_3+c_7) + \sum_1^{N-1}(c_4t_i + c_5(t_i-1)+ c_6(t_i-1))$$

From geometric sum formula, we have: 
$$\sum_1^Ni=\frac{N(N+1)}{2}$$