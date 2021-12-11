### How to derive a recurrence for Divide and Conquer Algorithm
As stated in Chapter 2, divide and conquer algorithms can be characterised in three general steps:
- Divide: divide the problem into smaller instances of the same problem,
- Conquer: solve the subproblems recursively,
- Combine: combine the solutions of the subproblems.

To derive a running time bound for divide and conquer algorithms, we can derive a recurrence relation based on the three steps, and analyse them using the following tools that will be discussed in this chapter:
-	Substitution method: guess a running time bound and prove that the guess is the solution for the recurrence using mathematical induction.
-	Recurrence tree method: draw a recurrence tree based on the recurrence to arrive at a good guess for the substitution method.
-	The Master Theorem: use a well-defined theorem based on the recurrence formula to arrive at the running bound. 

For now, let's focus on how to arrive at the recurrence since it will be the first step to analyse the running time complexity: 
Let $T(n)$ be the running time of the problem. When the subproblem is small enough - i.e. when the sub-array is of length 1 each, then we can solve the problem directly in $\Theta(1)$ time. Suppose that the division yields $a$ sub problems, each of size $1/b$ of the original -i.e. if at every step, we divide the original array into 3 sub arrays that are $1/4$ the length of the original, then we have $a=3,b=4$. For merge sort, these numbers are simply $a=2,b=2$, but there are different ways to divide which we will see later on. Hence if it takes $T(n/b)$ to solve a sub array of length $n/b$, then it takes $aT(n/b)$ to solve $a$ subproblems. If it also  takes $D(n)$ to divide the subarrays, and $C(n)$ time to combine them, then we have the following:
$$T(n) = 
\begin{cases}
\Theta(1) &\quad \text{if} \quad &n \leq c\\
aT(n/b) + D(n)+ C(n) &\quad \text{for} \quad &n>c
\end{cases}$$
The first line is taken as the boundary condition, the second line is the recurrence relation, which will be used to analyse the running complexity. In many cases, the divide step takes a constant time - i.e. finding the index to split, hence $D(n)=\Theta(1)$.

To recap:
- The running time of a divide and conquer algorithm can be written as a recurrence.
- The running time of a divide and conquer algorithm includes the time taken to divide into sub-problems, solve the sub-problems, and to combine the solutions:
- If the divide and conquer algorithm partitions an $n$-element array to $a$ sub-portions of length $n/b$, the running time $T(n)$ includes the time to solve $a$ sub problems of length $n/b$ - i.e. $aT(n/b)$, the time to divide the problem into sub-problems is $D(n)$, and the time to combine the sub problems is $C(n)$.

### Exercise 
4.1 Write the recurrence relation for the following algorithms:
-	Insertion sort: $T(n) = T(n-1)+O(n)$
-	Linear search: $T(n) = T(n-1) + \Theta(1)$
-	Binary search: $T(n)=T(n/2)+\Theta(1)$
-	Merge sort: $T(n) = 2T(n/2) + \Theta(n)$

