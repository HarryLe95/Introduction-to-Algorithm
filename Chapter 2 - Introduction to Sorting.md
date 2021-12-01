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
Assuming that the for and while loop exit by doing a comparison check (-i.e if the exit condition is met), then the number of times to taken to run through an N-iteration loop is N+1 instead of N like the usual operations. Note that the third column times shows the total number of times that the computer execute this line, hence the times for an inner loop should be multiplied by the number of iterations taken by the outter loops. $t_i$ shows the number of times the inner while loop is executed - i.e. when $i=1$, the maximum number of backtracks is 1, since $j$ can only take $0$. When $i=3$, the maximum number of backtracks is 3 since $j$ can take $2,1,0$. Hence for the worst case analysis, when the inner loop has to run the maximum number of backtracks, $t_i=i$ and we have: 

$$
\begin{align}
T(N) &= (c_1+c_2+c_3+c_7)*N - (c_2+c_3+c_7) + \sum_1^{N-1}(c_4t_i + c_5(t_i-1)+ c_6(t_i-1))\\
&= C_1*N - C_2 + \sum_{i=1}^{N-1}(C_3i + C_4(i-1))
\end{align}
$$

where: 
- $C_1=c_1+c_2+c_3+c_7$
- $C_2 = c_2 + c_3 + c_7$
- $C_3 = c_4$
- $C_4 = c_5+c_6$

From geometric sum formula, we have: 
$$\sum_1^Ni=\frac{N(N+1)}{2}$$
therfore we have:
$$T(N) = C_1N - C_2 + (C_3+C_4)\frac{N(N-1)}{2}-C_4(N-1)$$
After some algebra manipulations, we have the following form:
$$T(N) = aN^2 +bN +C$$
We can see that the running time for worst case follows a quadratic form of N.  We simplify this notion with the idea of **rate of growth**. The idea can be understood intuitively as follows: as N becomes larger and larger, the $N^2$ component dominates in value. At this point, we will use the notation $O(N^2)$ to denote the worst-case running time of the insertion sort algorithm. The mechanics behind this notation will be revisited in later chapter. We usually consider one algorithm to be more efficient than the other by comparing their worst case running times. We will also explain some of the caveats behind this analysis in later chapters. 


### Exercise
- Express $n^3/1000 - 100n^2 -100n + 3$ in the big O notation: 
	```
	O(N^3)
	```
- Consider the following **selection sort** algorithm:
	- Sort an array $A$ by first finding the smallest element of $A$ then exchange it with $A[0]$, then second smallest $A[1]$ and continues until $A[n-2]$. 
	- Write a pseudo code for this algorithm.
	- Prove loop invariant property.
	- Give the best and worst case analysis.
	
	```Python
	def selection_sort(A):
		N = len(A)
		for i in range(N-1):
			key = A[i]
			for j in range(i+1,N): #Find current minimum
				if key > A[j]: #Make a swap if minimum found
					temp=key 
					key = A[j]
					A[j]= temp
			A[i] = key
	```
	
	```Text
	The loop invariant property here is the left section of the array from the
	current iterating idex is sorted:
	Initialisation: A[-1] is trivially sorted since it is empty.
	Maintenance: if A[0:i] is sorted, by the end of the current iteration, 
	A[0:i+1] is sorted. This is because A[i] = min(A[i:]) should be smaller
	than every element of A[0:i]
	since A[0] = min(A[0,:]) <= A[1] = min A'[1,:] <= A[2] = min A''[2,:] ...
	where A^n denotes the resulting array after n iteration.
	Termination: The loop terminates once reaching N-1, when A[0:N-1] is sorted,
	and the left over element A[N-1] should be larger than everything in A[0:N-1]
	due to the idea shown above. Hence A is sorted.
 	```
	
	```Text:
	-----------------------------------------------------------------------------
	Command: 							Cost:		Times:
	def selection_sort(A):				
		N = len(A)						c1			1
		for i in range(N-1):			c2			N
			key = A[i]					c3			N-1
			for j in range(i+1,N):		c4			(sum from 1 to N-1)t_i
				if key > A[j]: 			c5			(sum from 1 to N-1)(t_i-1)
					temp=key 			c6			(sum from 1 to N-1)(t_i-1)
					key = A[j]			c7			(sum from 1 to N-1)(t_i-1)
					A[j]= temp			c8			(sum from 1 to N-1)(t_i-1)
			A[i] = key					c9			N-1
	```
	The time taken for $c_6,c_7,c_8$ components depend on the outcome of the conditional statement in $c_5$. For worst case analysis, assuming that the array is arranged in reversed order (every condition check is  positive), then time calculation:
	
	$$T(N) = c_1 + c_2N + c_3(N-1) + (c_4+c_9)\sum_{i=1}^{N-1}(N-i)+(c_5+c_6+c_7+c_8)\sum_{i=1}^N(N-i-1)$$
	
	After simplifying this  expression, the running time is also quadratic of $N$ and is therefore $O(N^2)$. Note that worst and best case running times for selection sort are the same. 

- Consider linear search algorithm in previous exercise: 
	- How many elements in $A$ need to be checked on average, assuming equal likelihood of the search value being in any position in the array. $P(v=A[0])=P(v=A[1])=\dots=\frac{1}{N}$ 
	- What about average case and worst case? 
	```Text
	Best case: found v after 1st attempt 
	Worst case: found v after Nth attempt 
	The average case is a bit tricky: 
	let X be the random variable denoting the number of attempt taken,
	hence we have the probability that X = k - i.e. it takes k attempt to find 
	v: 
	```
	$$
	\begin{align}
	P(k) &= P(X=k) = P(v\neq A[0])\times P(v\neq A[1])\times \dots P(v\neq A[k-2])\times P(v=A[k-1])\\
	&= \left(\frac{N-1}{N}\right)^{k-1}\times\frac{1}{N}
	
	\end{align}
	$$
	
	Hence the expected number of attempts:
	$$\begin{align}
	E(X) &= \sum_{i=0}^{N-1}iP(i)=0 + P(1)+2\times P(2) + N\times P(N)\\
	&=0 + \frac{1}{N} + 2\times\frac{N-1}{N}\times \frac{1}{N}+\dots+
	(N-1)\times \left(\frac{N-1}{N}\right)^{N-1}\times\frac{1}{N}\\
	&= \frac{1}{N}\sum_{i=1}^{N} \left(\frac{N-1}{N}\right)^{i-1}\times i
	\end{align}
	$$
 As $N \rightarrow \infty$, $\frac{N-1}{N}\rightarrow1$, and we can hence simplify the above expression to: 
 $$E(X) = \frac{1}{N}\times \frac{N(N+1)}{2}=\frac{N+1}{2}$$
 A python code with Monte-Carlo simulation: 
 ```Python
N_array = 100
N_trials = 100000
attempt = 0
A = np.arange(N_array)
for i in range(N_trials):
	A = np.random.permutation(A) #Shuffle A around
	attempt += linear_search(A,1) + 1 #Plus one since index from 0
attempt /= N_trials #Average number of attempts
 ```
 
### Divide and Conquer - Merge Sort
So far, the technique that we use to design insertion sort was based on an **incremental** approach, in which we sort an array $A$ by arranging its element one at a time. Another approach **divide and conquer** is based on the idea of breaking down a large problem into smaller and managable chunk to process. At this point, it is also useful to talk about **recursive** algorithms: algorithms that keep calling themselves until the desired solution has been met. Recursive algorithms often follow the divide and conquer approach, in which the original problem is partitioned into sub-problems that are to be solved recursively and the results combined at the end. We will go into greater details on this topic in future chapters. For now, let's present the idea of **merge sort**:
- Divide: divide an array $A$ of $n$ elements into $A'_0$ and $A'_1$, each of length $n/2$.
- Conquer: sort the two sub-arrays recursively. If the length of the array is small enough, we can directly solve the problem. 
- Combine: merge the two sorted sub-arrays. 

It's important to note that the combine step involves more than simply concatenating the two sub-sequence; for example, given two sub-arrays $(1,3,7)$ and $(2,4,5)$, we also need additional processing step so that the final array $(1,2,3,4,5,7)$ is sorted. In merge sort, the algorithm bottoms out when the divided sub-array has a length of 1, in which case, is in a correct order. We will see later on that merge-sort can be improved by combining with insertion-sort when the sub-array is small.

Now let's think about how to merge two already sorted sub-arrays, this process involves the following: 
- Let $i$ and $j$ be the iterating indices through each sub-arrays. For simplicity, we denote $E$ and $F$ as the sub-arrays, and $i \in \{0,1,\dots,N_E-1\}, j \in \{0,1,\dots,N_F-1\}$. 
- Let $S=\{\}$ be the sorted array, with $N_S=N_E+N_F$. 
- Initialise $i=0,j=0$ and begin to iterate through the index $k$ of $S$.
- At each iteration of $k$, set $S[k] = min(E[i],F[j])$, if $E[i] = min(E[i],F[j])$ then increment $i$ by $1$. Otherwise, increment $j$ by one. This ensures that as $k$ is incremented, either $i$ or $j$ is incremented, and since $k$ can iterate through a maximum of $N_S=N_E+N_F$ times, both sub-arrays $E$ and $F$ have been scanned by the end of $N_S$ iterations.  
- Once one array has been out-of-index (will definitely happen if one sub-array is longer than the other -i.e. $F$ is longer than $E$), the compiler will return an index-out-of-bound error if we try to compare $E[N_E]$ and $F[j]$. To avoid this problem, we can either pre-pad each sub-array with a large number so that once $E$ runs out of legitimate values, comparison will be between the legitimate values of  $F$ and the very large illegitimate value of $E$, in which case, values of $F$ should always be selected. 

The pseudo-code for this process is written as follows:
```Python
def merge_subarrays(E,F):
	
```