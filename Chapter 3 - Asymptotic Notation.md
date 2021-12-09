### Standard Notations and Common Functions
#### Asymptotic Notation
Asymptotic efficiency of algorithm deals with how the running time increases with the size of the input. Usually, an algorithm that is asymptotically more efficient will be the best choice for all but very small inputs. Additionally, it is also important to be clear what type of running time that we are discussing - worst case, expected, best case all come with different notations. 


#### Increasing and Decreasing Functions
Let $f:D\rightarrow \mathbb{R}$ be a mapping from a domain $D \subset \mathbb{R}$ to the real line,  
$f$ **monotonically increasing** if for 
$$x,y\in D,x\leq y \rightarrow f(x) \leq f(y)$$
**monotonically decreasing** if 
$$x\leq y \rightarrow f(x) \geq f(y)$$
Examples:
- $f(x) = x$ is monotonically increasing, since 
$x\leq y \rightarrow f(x)=x \leq f(y) = y$
- $f(x) = 1/x$ is monotonically decreasing, since 
$x\leq y \rightarrow 1/x\geq1/y\rightarrow f(x) \geq f(y)$

#### Floors and Ceilings:
For $x\in\mathbb{R}$: 
$$\lfloor x \rfloor \triangleq \max\{n \in \mathbb{Z}:n\leq x\} \triangleq \inf_{n\in \mathbb{Z}}x$$
$$\lceil x \rceil \triangleq \min\{n \in \mathbb{Z}:n\geq x\} \triangleq \sup_{n\in\mathbb{Z}}x$$

Some useful inequalities:
- 3.2.1/ $x-1<\lfloor x \rfloor \leq x \leq \lceil x \rceil <x+1$

- 3.2.2/ $\lfloor x/2\rfloor + \lceil x/2 \rceil = x$ for $x\in\mathbb{Z}$
	*Proof*:
- When $x$ is divisible by 2 - i.e. $x = 2k$, $\lfloor x/2 \rfloor =\lceil x/2 \rceil = k$. Hence:
	$\lfloor x/2 \rfloor + \lceil x/2 \rceil = k+k=2k=x$
- When $x$ is not divisible by 2 - i.e. $x=2k+1$, hence
$\lfloor x/2 \rfloor = k, \lceil x/2 \rceil=k+1$, and
$\lfloor x/2 \rfloor + \lceil x/2 \rceil =k+k+1=2k+1=x$

- 3.3.3/ The floor function $f(x) = \lfloor x \rfloor$ and the ceiling function $f(x)=\lceil x \rceil$ are monomotically increasing. 
*Proof*: we will show this property for the ceiling function, the proof for the floor function follows the same line of thoughts:
Consider $x,y \in \mathbb{R}$:
$$y = 
\begin{cases}
\lceil x \rceil \quad \text{if} \quad x\leq y \leq \lceil x \rceil \\
\lceil y \rceil \geq y > \lceil x \rceil \geq x \quad \text{if} \quad y > \lceil x \rceil\\
\end{cases}
$$
Hence if $x\leq y$, $\lceil x \rceil \leq \lceil y \rceil$ or $f(x) \leq f(y)$, hence QED.

- 3.3.4/ $\lceil a+b \rceil \leq \lceil a\rceil + \lceil b \rceil$ for $a,b \in\mathbb{R}$:
*Proof*: We have: $\lceil a \rceil \geq a, \lceil b \rceil \geq b$
Hence: 
$$\lceil a\rceil + \lceil b \rceil=\lceil \lceil a \rceil + \lceil b \rceil \rceil \geq \lceil a + b \rceil $$
The inequality occurs due to the monotonically increasing property of the ceiling function.

- 3.3.5/ $\lfloor a + b \rfloor \geq \lfloor a \rfloor + \lfloor b \rfloor$ for $a,b \in \mathbb{R}$:
*Proof*: We have: $\lfloor a \rfloor \leq a, \lfloor b \rfloor \leq b$,
Hence:
$$\lfloor a + b \rfloor \geq \lfloor \lfloor a \rfloor + \lfloor b \rfloor \rfloor=\lfloor a \rfloor + \lfloor b \rfloor$$
The inequality occurs since the floor function is monotonically increasing.

- 3.3.6/ $\left \lceil \frac{\lceil x/a \rceil}b\right\rceil =\left\lceil \frac{x}{ab}\right\rceil$ for $x\in\mathbb{R^+}, a,b\in\mathbb{N}$

	*Proof*:
	Observe that the equality is true if $x$ is divisible by $a$ -i.e. $|x/a|=k\in \mathbb{N}$ or $b=1$. Hence, we will show that the equality is still true if the remainder is not an integer. We have:
	$$\lfloor x/a\rfloor = k < x/a < \lceil x/a \rceil = k + 1$$
	Therefore, by the increasing property of ceiling function:
	$$\lceil k/b \rceil \leq \lceil x/ab \rceil \leq \lceil (k+1)/b \rceil$$
	Consider when $k$ is divisible by $b$, then 
	$$\lceil k/b \rceil < \lceil x/ab \rceil = \lceil (k+1)/b \rceil=\lceil k/b \rceil+1$$
	The last equality occurs since $\lceil k/b \rceil + 1=k/b+1$ is the smallest integer upperbound for $\lceil (k+1)/b\rceil$.
	Otherwise, we have:
	$$\lceil k/b \rceil=\lfloor k/b \rfloor+1$$
	Let:
	$$\frac{k+1}{b}=\left\lfloor \frac{k}{b}\right\rfloor+r$$
	It is easy to show that $r \in (0,1]$: $0 < r = (k+1)/b-\lfloor k/b \rfloor \leq (k+1)/1-k=1$
	By the increasing property of the ceiling function: 
	$$\left\lceil \frac{k}{b} \right\rceil \leq \left\lceil \frac{k+1}{b} \right\rceil \leq \left\lfloor \frac{k}{b}\right\rfloor+ \lceil r \rceil= \left\lfloor \frac{k}{b}\right\rfloor+1=\left\lceil \frac{k}{b} \right\rceil$$
	Hence, 
	$$\left\lceil \frac{k}{b} \right\rceil = \left\lceil \frac{x}{ab} \right\rceil = \left\lceil \frac{k+1}{b}\right\rceil$$
	Hence QED
	
- 3.3.7/ $\lfloor \lfloor x/a \rfloor/b \rfloor = \lfloor x/ab \rfloor$ for $x\in\mathbb{R^+}, a,b \in \mathbb{N}$:
If $x$ is divisible by  a or $b=1$, then the equality is fulfilled. Otherwise, let $k \in \mathbb{N} = \lfloor x/a \rfloor$, we have:
$$k<x/a<k+1$$
and 
$$\lfloor k/b \rfloor \leq \lfloor x/ab \rfloor \leq \lfloor (k+1)/b \rfloor$$
Consider when $k$ is divisible by $b$, then $\lfloor k/b \rfloor = k/b$, by the increasing property of the floor function:
$$\lfloor k/b + 1/b \rfloor \leq k/b + 1$$
The equality of which occurs only when b = 1, therefore, for $b>1$:
$$k/b = \lfloor k/b \rfloor = \lfloor x/ab \rfloor =\lfloor (k+1)/b \rfloor < k/b + 1$$
When $k$ is not divisible by $b$, again, let 
$$\frac{k+1}{b}=\left\lfloor \frac{k}{b}\right\rfloor+r$$
Hence:
$$
\left\lfloor \frac{k+1}{b} \right\rfloor = \left\lfloor \frac{k}{b}\right\rfloor + \lfloor r \rfloor=\left\lfloor \frac{k}{b}\right\rfloor
$$
since $r=1$ only when $b=1$. Hence QED

- 3.3.8 Prove the following:
$$\left\lceil \frac{a}{b} \right\rceil \leq \frac{a+b-1}{b}$$
$$\left\lfloor \frac{a}{b} \right\rfloor \geq \frac{a-b+1}{b}$$

*Proof*:
When $a$ is divisible by $b$, the inequality can easilly be shown. When $a$ is not divisible by $b$, let:
$$\frac{m}{b} = \left\lceil \frac{a}{b} \right\rceil$$
$$\frac{n}{b} = \left\lfloor\frac{a}{b} \right\rfloor$$
Then, 
$$\frac{m-n}{b}=1$$
Or 
$$m-n = b$$
Hence 
$$m-a < m - n = b$$ 
and 
$$a - n < m - n = b$$
Or 
$$m-a \leq b - 1$$
and 
$$a-n \leq b-1$$
Therefore,
$$\left\lceil \frac{a}{b} \right\rceil = \frac{m}{b} \leq \frac{a + b - 1}{b}$$
$$\left\lfloor \frac{a}{b} \right\rfloor = \frac{n}{b} \geq \frac{a - b + 1}{b}$$
QED

#### Logarithms
Define a function $\log_b()$ such that $log_b(b^n)=n$ for $b \in \mathbb{R}$.
If $b>1$ then $\log_b()$ is strictly increasing. 
For all $a>0,b>0,c>0, a,b,c \in \mathbb{R}, n \in \mathbb{N}$
- 3.3.9/ $a = b^{\log_ba}$
*Proof*:
$$
\begin{align}
&a = b^{\log_b(a)}\\
\iff &\log_b(a) = \log_b(b^{\log_b(a)}) \quad \text{By definition.}
\end{align}
$$

- 3.3.10/ $\log_c(ab)=\log_c(a) + \log_c(b)$
*Proof*:
$$
\begin{align}
&\log_c(ab)=\log_c(a) + \log_c(b)\\
\iff & ab = c^{\log_c(ab)} = c^{\log_c(a) + \log_c(b)}\\
\iff & ab = c^{\log_c(a)}\times c^{\log_c(b)} \quad \text{By definition}
\end{align}
$$

- 3.3.11/$\log_b(a^n) = n\log_b(a)$ 
*Proof*:
$$
\begin{align}
&b^{\log_ba^n } = b^{n\log_ba} \\
\iff &a^n = (b^{\log_ba})^n 
\end{align}
$$

- 3.3.12/ $\log_b(a) = \frac{1}{\log_a(b)}$
*Proof*:
$$
\begin{align}
&\log_ba = \frac{1}{\log_ab} \\
\iff &\log_ba \times \log_ab = 1 \\ 
\iff & b^{\log_ba \times \log_ab} = b^1 = b\\
\iff & a^{ \log_ab} = b
\end{align}
$$

- 3.3.13/ $\log_b(1/a)=-\log_b(a)$
*Proof*:
$$\log_b(1/a) = \log_b(a^-1) = -1 \times \log_b(a) = -\log_b(a)$$

- 3.3.14/ $\log_b a = \log_c a / \log_c b$
*Proof*:
$$
\begin{align}
&\log_b(a) = \frac{\log_c a}{\log_cb} \\
\iff &\log_ba \times \log_cb = \log_c a \\ 
\iff & c^{\log_ba \times \log_cb} = c^{\log_c a} = a\\
\iff & b^{ \log_ba} = a
\end{align}
$$

Equation 3.3.14 allows us  to change the base of logarithmic function from one constant to another by multiplying another constant, hence for the big O notation involving logarithmic terms, it does not matter the base and $\log$ is used implicitly with base $e$. 
We say that a function is *polylogarithmically bounded* if $f(n) = O(\log^kn)$ where $\log^kn=(\log n)^k$ Note that any positive polynomial function grows faster than any polylogarithmic function. *Prove this as an exercise*.
$$\log^k n = o(n^a) \quad \text{for }a > 0$$ 

#### Polynomials:
Given a nonnegative integer $d$, a polynomial in n of degree d is:
$$p(n) = \sum_{i=0}^d a_in^i$$
We say that a function is polynomially bounded if $f(n) = O(n^k)$ for some constant $k$.

#### Exponentials:
Prove the following: 
$$\lim_{n\rightarrow \infty} \frac{n^b}{a^n}=0 \quad \text{for } a > 1$$
as an exercise, hence deduce that: 
$$n^b = o(a^n)$$
Therefore, an exponential function with a base 1 is strictly increasing and that it grows faster than any polynomial function. 