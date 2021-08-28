---
title: "Solution to the split and multiply puzzle from FiveThirtyEight"
date: 2021-06-06
layout: post


description: ""



tags: ['math', 'puzzle']

comments: true
share: true
---



## Problem

> Max the Mathemagician is calling for volunteers. He has a magic wand of length
10 that can be broken anywhere along its length (fractional and decimal lengths
are allowed). After the volunteer chooses these breakpoints, Max will multiply
the lengths of the resulting pieces. For example, if they break the wand near
its midpoint and nowhere else, the resulting product is 5×5, or 25. If the
product is the largest possible, they will win a free backstage pass to his next
show. (Amazing, right?)
>
> You raise your hand to volunteer, and you and Max briefly make eye contact. As
he calls you up to the stage, you know you have this in the bag. What is the
maximum product you can achieve?
>
> Extra credit: Zax the Mathemagician (no relation to Max) has the same routine
in his show, only the wand has a length of 100. What is the maximum product now?



## General solution



Problem can be separated into two parts. First we want to decide into how many
pieces do we want to split the line and second what should be the length of the
line segments. Let's focus on the second part of the problems first.



### Optimal sizes of the segments



We start with a line of length \\(L\\) and we want to split it into \\(n\\)
parts with length \\(x_1\\), \\(x_2\\), ..., \\(x_n\\) such that \\(x_1 + x_2 +
... + x_n = L\\) and \\(x_i \gt 0 \, \forall i \in \\{1, 2, ..., n\\}\\). For a
given \\(n\\) we want to find such a split that maximizes the following function

$$
f(x_1, x_2, ..., x_n) = \prod_{i=1}^{n} x_i
$$

Maximum won't be effected if we apply monotonically increasing function or scale
it by a positive constant

$$
\begin{align}
\underset{x_1, x_2, ..., x_n}{\operatorname{arg\,max}} \, f(x_1, x_2, ..., x_n)
&= \underset{x_1, x_2, ..., x_n}{\operatorname{arg\,max}} \ln\,f(x_1, x_2, ...,
x_n) \\
&= \underset{x_1, x_2, ..., x_n}{\operatorname{arg\,max}} \frac{1}{n}
\ln\,f(x_1, x_2, ..., x_n)\\
&= \underset{x_1, x_2, ..., x_n}{\operatorname{arg\,max}} \frac{1}{n}
\sum_{i=1}^{n} \ln\,x_i
\end{align}
$$

Since logarithm is a concave function we can apply [Jensen's
inequality](https://en.wikipedia.org/wiki/Jensen%27s_inequality) in order to
find an upper bound for the transformed function \\(f\\)

$$
\frac{1}{n} \sum_{i=1}^{n} \ln\,x_i \leq \ln \left(\frac{1}{n} \sum_{i=1}^{n}
\,x_i\right) = \ln \frac{L}{n}
$$

Multiplying both sides by \\(n\\) and exponentiating we find that

$$
\prod_{i=1}^{n} x_i \leq \left(\frac{L}{n}\right)^n
$$

or alternatively

$$
f(x_1, x_2, ..., x_n) \leq f\left(\frac{L}{n}, \frac{L}{n}, ...,
\frac{L}{n}\right)
$$

It shows that dividing line \\(L\\) into equal pieces maximizes the product of
the remaining parts when \\(n\\) is fixed.




### Optimal number of segments



Now we need to find a solution to the following problem

$$
\mathbf{\max_{n \in N}} \, g(n) = \mathbf{\max_{n \in N}} \,
\left(\frac{L}{n}\right)^n
$$



We can calculate derivative in order to find extremum (for \\(n \in R\\) and
\\(n \gt 0\\))

$$
\begin{align}
\frac{dg}{dn} &= \frac{d}{dn} \left(\frac{L}{n}\right)^n \\
              &= \frac{d}{dn} e^{n \ln \frac{L}{n}} \\
              &= g(n) \ln \frac{L}{n\,e}
\end{align}
$$

since \\(g(n) \gt 0 \\), the derivative is equal to zero only when
\\(n=\frac{L}{e}\\). With a second derivative we can actually show that
discovered solution is a maximum

$$
\begin{align}
\frac{d^2g}{dn^2} &= g(n) \left(\left(\ln
\frac{L}{e\,n}\right)^2-\frac{1}{n}\right)
\end{align}
$$

It's very easy to see that if we plug \\(n=\frac{L}{e}\\) the second derivative
will be negative showing that the discovered solution is actually a maximum.

One last part of the problem remains, since we initially wanted to discover
integer solutions, but the discovered solution is not even a rational number
when \\(L\\) is a rational number. Integer solutions can be found by noticing
that the derivative increases in the region \\((0, \frac{L}{e})\\) and decreases
in the region \\((\frac{L}{e}, +\infty)\\). This implies that the two closest
integer solutions (\\(\left\lfloor \frac{L}{e} \right\rfloor\\) and
\\(\left\lceil \frac{L}{e} \right\rceil\\)) are the only two candidates, since
all of the integers further away from the candidates are smaller.

With only two possible candidates, it's very easy to check which one has the
largest value just by evaluating \\(g(n)\\) at both points and selecting the one
which produces the largest value.



## Solution



In order to answer the question above we need to find \\(n\\) using the
procedure derived in the previous section for \\(L=10\\) and \\(L=100\\).

<table>
<tr>
    <th>Length</th>
    <th>Best number of splits</th>
    <th>Largest possible product</th>
</tr>
<tr>
    <td>10</td>
    <td>4</td>
    <td>
    \begin{eqnarray}
    \frac{625}{16}=39.0625
    \end{eqnarray}</td>
</tr>
<tr>
    <td>100</td>
    <td>37</td>
    <td>
    \begin{eqnarray}
    \left(\frac{100}{37}\right)^{37} \approx 9.474 \cdot 10^{15}
    \end{eqnarray}
    </td>
</tr>
</table>

