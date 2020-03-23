---
title: "Iterative homogenization by elimination"
date: 2020-03-22
---
### Problem

Let's say we have \\(S\\) objects and each object is associated with one of the
\\(N\\) classes. There are \\(c_i\\) objects associated with the \\(i\\)-th
class. We want to eliminate only \\(b\\) objects in a way that forms
distribution of classes as close as possible to the uniformal distribution.

### Intuition

Intuition suggests that we can eliminate one object at a time by selecting a
class with the largest number of objects in it. It's not quite obvious whether
this is the best strategy to follow. For example, we can start with the
following distribution of classes - \\(c = [12, 6, 7, 13]\\). Next, we can
eliminate 2 objects from it (\\(b = 2\\)).
After elimination we can end up with 10 different outcomes. We can follow our
initial strategy and end up with the following distribution: \\([12, 6, 7,
11]\\) (or \\([11, 6, 7, 12]\\)). Using some other strategy we can get a
different outcome, for example, \\(c = [12, 6, 6, 12]\\). How do we know which
one is closer to the uniformal distribution.

The word "closer" impliest that we need to have a certain measure that allows us
to measure homogenization of the distribution. In order to get the solution we
need to better define our objective.

### Objective

We can use Kullback–Leibler divergence (KL divergence) in order to measure
homogenization of the distribution. We can normalize \\(c\\) in order to convert
it to a probability distribution \\(p\\)

$$
p = [p_1, p_2, ..., p_N] \\
p_i = \frac{c_i}{\sum_{j=1}^{N}{c_j}} \\
$$

And we can define desirable uniformal distribution

$$
u = [u_1, u_2, ..., u_N] \\
u_i = \frac{1}{N}
$$

KL divergence is not symmetric. Comparing \\(u\\) to \\(p\\) is not the same as
comparing \\(p\\) to \\(u\\). We can show that for this problem both versions
will lead to the same solution and order in which distributions are specified is
not important for our purpose.

We can start with the following definition

$$
D_{KL}(u \, || \, p) = \sum_{i=1}^N{u_i \log \frac{u_i}{p_i} } \\
$$

For our problem we want to subtract \\(b\\) objects and after this we will end
up with a distribution \\(q\\)

$$
q = [q_1, q_2, ..., q_N] \\
q_i = \frac{c_i - x_i}{\sum_{j=1}^{N}{c_j - x_j}} \text{, where}
\sum_{i=1}^{N}{x_i}=b
$$

Optimization could be sumarized in the following way

$$
\begin{align}
\mathbf{\min_x} \, & D_{KL}(u \, || \, q)  & \\
\text{subject to: } & \sum_{i=1}^{N}{x_i}=b  & \\
                    &  x_i \geq 0   & \forall i=1,...,N
\end{align}
$$

### Solution

First, we can notice that original function that we want to opimize can be
simplified

$$
\underset{x}{\operatorname{arg\,min}} D_{KL}(u \, || \, q) =
\underset{x}{\operatorname{arg\,max}} \sum_{i=1}^{N} \log q_i
$$


We can use Karush–Kuhn–Tucker (KKT) conditions in order to solve this problem.
Objective could be defined in the following way

$$
L(x, \lambda, \{\eta_j\}) = \sum_{j=1}^{N} \log q_j - \lambda
\left(\sum_{j=1}^{N}{x_j} - b \right) + \sum_{j=1}^{N} \eta_j x_j
$$

and we need to solve the following equation in order to find optimal solution

$$
\frac{\partial}{\partial x_i}\left(\sum_{j=1}^{N} \log q_j\right) - \lambda +
\eta_j = 0
$$

we can rewrite this equation in order to have \\(x_i\\) specified explicitly

$$
-\frac{1}{c_i - x_i} + \frac{N}{\sum_{j=1}^{N}{c_j - x_j}} = \lambda - \eta_i
$$

From the equation above we can notice that

$$
\eta_i - \frac{1}{c_i - x_i} = \eta_j - \frac{1}{c_j - x_j} \text{, where} \, i
\ne j
$$

From the Complementary slackness in the KKT conditions we know that \\(\eta_i
x_i = 0\\). This condition implies that \\(\eta_i\\) and \\(x_i\\) cannot be
non-zero values at the same time. We can consider two cases:

1. There exists at least one more non-zero \\(x_i\\). From this assumption the
following statement is true (since \\(\eta_i = \eta_j = 0\\))

   $$
   \frac{1}{c_i - x_i} = \frac{1}{c_j - x_j} \text{, where} \, i \ne j
   $$

   This equation says that \\(c_i - x_i = c_j - x_j\\). This means that after
elimination we should end up with exactly the same values in each category.

2. There exists at least on \\(x_i=0\\). From this assumption the following
statement is true:

   $$
   \eta_i - \frac{1}{c_i} = -\frac{1}{c_j - x_j}
   $$

   and since \\(\eta_i \ge 0\\) we get that

   $$
   c_j \gt c_j - x_j \ge c_i
   $$

   Since we assumed that \\(x_i=0\\) and \\(x_j \ne 0\\) the equation above
implies that every zero is associated with the smallest \\(c_i\\) value and
every non-zero is associated with the largest \\(c_j\\) value. This observation
matches our initial intuition. Equation implies that we should remove objects
from the most common classes first.

### Algorithm

There are multiple different algorithms that could be derived from the previous
equations. We can find one by using the following definitions

1. \\(A = \\{ i \, \| \, x_i=0 \\} \\)
2. \\(\overset{\\_}{A} = \\{ i \, \| \, x_i\ne0 \\}\\)
3. \\(\|\overset{\\_}{A}\| = m \\) and \\(\|A\| = n- m \\)
4. \\(\sum_{i=1}^N{c_i} = C\\)
5. \\( k = c_i - x_i, \forall i \in \overset{-}{A}\\)
6. \\(c_i \le c_j, \forall i \le j \\)

$$
\begin{align}
\sum_{i=1}^N{c_i - x_i} &= C - b \\
\sum_{j \in A}{c_j} + \sum_{i \in \overset{\_}{A}}{c_i - x_i} &= C - b \\
\sum_{j \in A}{c_j} + \sum_{i \in \overset{\_}{A}}{c_i - x_i} &= C - b \\
\sum_{j \in A}{c_j} + m \, k &= C - b \\
k = \frac{C - b - \sum_{j \in A}{c_j}}{m} &= \frac{\sum_{j \in
\overset{\_}{A}}{c_j} - b}{m}
\end{align}
$$

If we assume that there is at least one \\(x_i = 0\\) then the following should
be true

$$
\begin{align}
c_{n-m} &\le \frac{\sum_{j \in \overset{\_}{A}}{c_j} - b}{m} \\
b &\le \sum_{j \in \overset{\_}{A}}{c_j} - m \, c_{n-m}
\end{align}
$$

and this equation will work if \\(c_0 = 0\\) (which implies that we have N+1
category, but one additional category doesn't have objects in it).

In addition, after some rearrangement of terms we can create the following
equation.

$$
\begin{align}
b &\le \sum_{a = 1}^{m} a \, (c_{n - a + 1} - c_{n - a})
\end{align}
$$

### Reversing order of distributions in the KL divergence function

$$
\begin{align}
\mathbf{\min_x} \, & D_{KL}(q \, || \, u)  & \\
\text{subject to: } & \sum_{i=1}^{N}{x_i}=b  & \\
                    &  x_i \geq 0   & \forall i=1,...,N
\end{align}
$$

As before, main equation could be simplified

$$
\underset{x}{\operatorname{arg\,min}} \, D_{KL}(q \, || \, u) =
\underset{x}{\operatorname{arg\,min}} \sum_{i=1}^{N} q_i \log q_i
$$

On the right side, we have a negative entropy, and minimum will mean that we
just need to maximize entropy of the distribution \\(q\\)

$$
\underset{x}{\operatorname{arg\,min}} \, D_{KL}(q \, || \, u) =
\underset{x}{\operatorname{arg\,max}} \, H(q)
$$


$$
L(x, \lambda, \{\eta_j\}) = \sum_{j=1}^{N} q_j \log q_j + \lambda
\left(\sum_{j=1}^{N}{x_j} - b \right) - \sum_{j=1}^{N} \eta_j x_j
$$

from which follows that

$$
\sum_{j=1}^{N} q_j \log q_j - \frac{\log q_i}{S} + \lambda - \eta_i = 0 \\
\eta_i + \frac{\log q_i}{S} = \lambda + \frac{1}{S} \sum_{j=1}^{N} q_j \log q_j
$$

where \\(S = \sum_{j=1}^{N} c_j - x_j \\)

and based on the same logic as before we can show that

$$
\eta_i + \frac{\log (c_i - x_i)}{S} = \eta_j + \frac{\log (c_j - x_j)}{S},
\forall i,j = 1...N
$$

And again, we can go through two cases:

1. if we assume that \\(x_i=0\\) and \\(x_j\ne0\\) then \\(c_j \gt c_j - x_j \ge
c_i\\)
2. if we assume that \\(x_i\ne0\\) and \\(x_j\ne0\\) then \\(c_j - x_j = c_i -
x_i\\)

The same conclusion could be drawn from these equations which shows that order
of the distribution doesn't make a difference for this problem

### Handling discrete cases

Developed equations can produce non-integer solutions. These results won't be
suitable for our initial problem. Solution could be easily modified in order to
work with integers. First, we can notice that non-integer values will be
produced only for cases when \\( \sum_{j \in \overset{\\_}{A}}{c_j} - b \\) is
not divisible by \\(m\\) without the remainder. Instead, we can ue the following
equation

$$
k = \left\lceil\frac{\sum_{j \in \overset{\_}{A}}{c_j} - b}{m}\right\rceil - s_j
$$

where

$$
s_j = \begin{cases}
1 &\quad j \gt n-r \\
0 &\quad\text{otherwise.} 
\end{cases}
$$

and

$$
\\
r = \sum_{j \in \overset{-}{A}}{c_j} - b \bmod {m}
$$


This is just one way of defining \\(s_j\\) function, but any strategy will work.
It's asy to see why this solution is the best that we can get from the previous
equations and given that \\(m\\) categories have exactly the same value it
doesn't really matter from which of the categories we subtract remaining ones.



