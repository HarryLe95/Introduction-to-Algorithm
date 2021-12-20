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

### How to solve recurrence equation
#### The substitution method (induction)
The substitution method involves two steps:
- Guess the solution,
- Prove the solution using induction

Example:
Find the upper bound of $T(n)=2T(\lfloor n/2 \rfloor)+n$

*Solution*:
We make a guess that the upper bound for the running time is $O(n\log n)$. We first make an inductive hypothesis that $T(n)\leq cn \log n$ for some $c>0$ and $n$ sufficiently large (based on the definition of $O(n\log n)$). Assume that this holds for some $m<n$, in particular $m=\lfloor n/2 \rfloor$. We then have:
$$T(\lfloor n/2 \rfloor) \leq c\lfloor n/2 \rfloor \log \lfloor n/2 \rfloor \leq c \frac{n}{2}\log\frac{n}{2}$$
The second inequality occurs since $n/2 > \lfloor n/2 \rfloor$ and $\log$ is monotonically increasing.
Hence:
 $$
\begin{align}
T(n) &= 2T(\lfloor n/2 \rfloor)+n\\
&\leq 2c\frac{n}{2}\log\frac{n}{2}+n\\
&= cn \log n - cn\log 2 + n\\
&= cn \log n - cn + n\\
&\leq c n \log n \quad \text{for} \quad c \geq 1
\end{align}
 $$
We are now required to show that this solution is true for the boundary condition to complete the induction proof. Note that for this particular problem, if we assume the boundary condition to be $T(1)=1$, then we will have some problem proving that $T(1)=1\leq c\times 1 \log 1=0$. However, note that using the definition of O, we are only required to find $n_0$ that is the boundary condition, for instance, we can let $n_0=2$, $T(2)=2T(1)+2=4\leq 2c \log 2 = 4c$, which will hold for $c\geq 1$. By choosing $n_0=2,c\geq 1$, we have shown that the inductive hypothesis is satisfied, and that $T(n)=O(n\log n)$. Note that proving the boundary condition is often realtively simple, hence will be omitted from future proofs.

There are a few things that we need to pay attention to when using the subtitution method:
- After making the inductive hypothesis, we need to prove that the recurrence equation has the *exact* form of the inductive hypothesis. For instance, the proof that $T(n)=2T(\lfloor n/2 \rfloor) + n = O(n)$ is incorrect:
$$
\begin{align}
T(n) &\leq 2c \lfloor n/2 \rfloor + n \\
&\leq cn + n \\
&= O(n) \quad \text{wrong}
\end{align}
$$
For the proof to be correct, we will need to show explicitly that $T(n)\leq cn$.

- When the inductive hypothesis is not strong enough, but the guess is correct, we may be able to solve the problem by deducting a lower order term in the inductive hypothesis. For instance, the recurrence $T(n) = T(\lfloor n/2 \rfloor) + T(\lceil n/2 \rceil) + 1$ has the wost case bound of $O(n)$, but if we make the hypothesis: $T(n)\leq cn$, we have:
$$
\begin{align}
T(n) &\leq c \lfloor n/2 \rfloor + c \lceil n/2 \rceil + 1 \\
&= cn + 1 \\
\end{align}
$$
which doesn't have the exact form $T(n) \leq cn$. We can change the hypothesis to be $T(n) \leq cn-d$, hence
$$
\begin{align}
T(n) &\leq c \lfloor n/2 \rfloor -d+ c \lceil n/2 \rceil-d + 1 \\
&= cn -2d+ 1 \\
&\leq  cn - d \quad \text{for} \quad d \geq 1
\end{align}
$$
which does satisfy the exact form $T(n)\leq cn - d$. Note that this inductive hypothesis satisfies $T(n)=O(n)$ since $cn-d<cn$ for $c>0,d\geq 0$. Note that in many problems that require us to subtract a lower order term, it is sufficient to select a positive coefficent such that the recurrence matches the form of the inductive hypothesis. 

- Sometimes, you may be able to change the form of the variables to reduce them to a form that is easier to manage. For instance, $T(n)=2T(\lfloor \sqrt{n} \rfloor) + \log n$, we can set $m=\log n$, hence $\sqrt{n}=2^{m/2}$, and $n=2^m$. Subtituting these expressions into the recurrence:
$$T(2^m)=2T(2^{m/2})+m$$
Let $S(m)=T(2^m)$, we have:
$$S(m)=2 S(m/2)+m=O(m\log m)$$
Hence resubstitute $m=\log n$:
$$T(n)=S(m)=O(m\log m)=O(\log n \log (\log m))$$

### Exercise 
4.1 Write the recurrence relation for the following algorithms:
-	Insertion sort: $T(n) = T(n-1)+O(n)$
-	Linear search: $T(n) = T(n-1) + \Theta(1)$
-	Binary search: $T(n)=T(n/2)+\Theta(1)$
-	Merge sort: $T(n) = 2T(n/2) + \Theta(n)$

4.2 Show that $T(n)=T(n-1)+n=O(n^2)$:
*Proof*: assume inductive form: $T(n) \leq cn^2$, hence
$$
\begin{align}
T(n) &\leq c(n-1)^2 + n \\
&= cn^2 -2cn + 1 + n \\
&\leq cn^2 \quad \text{for } \quad c\geq 1, n\geq1
\end{align}
$$

4.3 Show that $T(n)=T(\lceil n/2\rceil)+1=O(\log n)$:
*Proof*: assume inductive form: $T(n) \leq c \log n$:
$$
\begin{align}
T(n) &\leq c\log \lceil n/2 \rceil+1 \\
&\leq c\log (\frac{n+1}{2})+1\\
&\leq c\log n
\end{align}
$$