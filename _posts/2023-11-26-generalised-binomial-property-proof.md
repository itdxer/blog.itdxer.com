---
title: "Property of the Generalised Binomial Distribution"
date: 2023-11-24
layout: post


description: "The article covers a rather simple proof of the peculiar property of the generalised binomial distribution"


tags: ['math', 'probability']


comments: true
share: true
---


### Problem


Suppose we have a sequence of independent random binary variables \\(X_1, X_2, ..., X_n\\) with \\(P(X_i=1)=p_i\\). Let \\(r_k\\) be an arithmetic mean of the probabilities among sequences where \\(X_1 + X_2 + ... + X_n = k\\), specifically \\(r_k = \binom{n}{k}^{-1} P(X_1 + X_2 + ... + X_n = k)\\). Show that the identity below always holds for all possible values of \\(p_i\\)


$$
\frac{r_k}{r_{k-1}} \ge \frac{r_{k+1}}{r_{k}}
$$


### Alternative formulation


If we represent \\(r_1, r_2, ..., r_n\\) as a sequence then the problem asks us to prove that each term in the sequence is larger than the geometric mean of its neighbours. Specifically


$$
r_k \ge \sqrt{r_{k-1}r_{k+1}}
$$


It's also an interesting combination of the arithmetic and geometric mean. Also note that the inequality above works for \\(k=0\\) and \\(k=n\\), since \\(r_{-1} = r_{n+1} = 0\\).


### Example


Consider the case \\(n=3\\) where \\(q_k = 1 - p_k\\)


$$
\begin{align}
r_0 &= q_1q_2q_3 \\
r_1 &= \frac{1}{3}\left(p_1q_2q_3 + q_1p_2q_3 + q_1q_2p_3\right) \\
r_2 &= \frac{1}{3}\left(p_1p_2q_3 + p_1q_2p_3 + q_1p_2p_3\right) \\
r_3 &= p_1p_2p_3 \\
\end{align}
$$


### Proof


We want to prove the following statement


$$
r_{n,k}^2 - r_{n,k-1}r_{n,k+1} \ge 0 \label{eq1}\tag{1} \\
$$


It can be proven by induction. Start with the base \\(n=2\\) and \\(k=1\\)


$$
\begin{align}
r_{2,1}^2 - r_{2,0}r_{2,2} &=\left(\frac{1}{2}(p_1q_2 + q_1p_2)\right)^2 - q_1q_2p_1p_2  \\
                          &= \frac{1}{4}p_1^2q_2^2 + \frac{1}{4}q_1^2p_2^2 + \frac{1}{2}q_1q_2p_1p_2 - q_1q_2p_1p_2\\
                          &= \frac{1}{4}(p_1q_2 - q_1p_2)^2 \\
                          &\ge 0
\end{align}
$$




Next, we assume that it holds for all cases with indices less than \\(n\\) and define the following recursive relation


$$
\begin{align}
r_{n,k} = p_n \frac{k}{n} r_{n-1,k-1} + q_n \frac{n-k}{n}r_{n-1,k} \label{eq2}\tag{2} \\
\end{align}
$$




where \\(r_{n,k}=0\\) if \\(k \gt n\\) or \\(k \lt 0\\). With the help of the recursion (\ref{eq2}) we can expand \\(r_{n,k}^2\\) and \\(r_{n,k-1}r_{n,k+1}\\) terms from (\ref{eq1})


$$
\begin{align}
r_{n,k}^2 = &\,p_n^2\frac{k^2}{n^2}r_{n-1,k-1}^2 \label{eq3}\tag{3}\\
           &+q_n^2\frac{(n-k)^2}{n^2}r_{n-1,k}^2 \\
           &+2p_nq_n\frac{k(n-k)}{n^2}r_{n-1,k-1}r_{n-1,k} \\
r_{n,k-1}r_{n,k+1} = &\,p_n^2\frac{k^2-1}{n^2}r_{n-1,k-2}r_{n-1,k} \label{eq4}\tag{4}\\
                    &+ q_n^2 \frac{(n-k)^2-1}{n^2}r_{n-1,k-1}r_{n-1,k+1} \\
                    &+ p_nq_n \frac{(k-1)(n-k-1)}{n^2}r_{n-1,k-2}r_{n-1,k+1} \\
                    &+ p_nq_n \frac{(k+1)(n-k+1)}{n^2}r_{n-1,k-1}r_{n-1,k} \\
\end{align}
$$


By induction, we can use inequalities below in order to simplify (\ref{eq4})


$$
\begin{align}
r_{n-1,k-1}^2 &\ge r_{n-1,k-2}r_{n-1,k} \\
r_{n-1,k}^2   &\ge r_{n-1,k-1}r_{n-1,k+1} \\
r_{n-1,k-1}r_{n-1,k} &\ge r_{n-1,k-2}r_{n-1,k+1} \\
\end{align}
$$


which gives us the following inequality


$$
\begin{align}
r_{n,k-1}r_{n,k+1} \le &\, p_n^2\frac{k^2-1}{n^2}r_{n-1,k-1}^2 \label{eq5}\tag{5}\\
                      & + q_n^2 \frac{(n-k)^2-1}{n^2}r_{n-1,k}^2 \\
                      & + 2p_nq_n\frac{k(n-k)+1}{n^2}r_{n-1,k-1}r_{n-1,k}
\end{align}
$$


Plugging (\ref{eq3}) and (\ref{eq5}) into the LHS of (\ref{eq1}) gives us the desired result


$$
\begin{align}
r_{n,k}^2 - r_{n,k-1}r_{n,k+1} &\ge \frac{1}{n^2}\left(p_n^2 r_{n-1,k-1}^2 + q_n^2 r_{n-1,k}^2 - 2p_nq_nr_{n-1,k-1}r_{n-1,k}\right) \\
                              &= \frac{1}{n^2}(p_nr_{n-1,k-1} - q_nr_{n-1,k})^2 \\
                              &\ge 0
\end{align}
$$


### References

The problem is from **Donald Knuth**'s book: **The Art of Computer Programming, Fascicle 5: Mathematical Preliminaries Redux; Introduction to Backtracking; Dancing Links**. It originally was stated by Isaac Newton without a proof and the first proof was given by James Sylvester (not to suggest that the problem wasn't proved by Newton, perhaps, he just didn't bother to include it into his book).
