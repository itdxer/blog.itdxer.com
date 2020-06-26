---
title: "Coin flipping game from IMO 2019"
date: 2020-05-13
layout: post


description: "Solution to my favorite problem from the IMO 2019"



tags: ['math', 'puzzle', 'imo']

comments: true
share: true
---



## Problem



![](http://blog.itdxer.com/images/imo-2019/imo-2019-problem-5.png)



## Notations



Before we start we will need to introduce a few notations that can help with the
proof.



### Left and right movement in the process

Let's start with \\(N\\) coins and find \\(k\\) coins with \\(H\\). Next we find
a coin at k-th position. There are two possible outcomes:

1. Coin at the k-th position shows \\(H\\) (head). In this case, we flip the
coin from \\(H \to T\\) which means that now we have \\(k-1\\) coins with
\\(H\\) and in the next step we will have to check coin at \\((k-1)\\)-th
position

2. Coin at k-th position has \\(T\\) on it. In this can we flip coin from \\(T
\to H\\) which means that now we have \\(k+1\\) coins with \\(H\\) and in the
next step we will have to check coin at \\((k+1)\\)-th position

It's easy to see that after one operation, the number of coins with \\(H\\)
either increased or decreased by one. In this case, if the game didn't get
finished, we continue flipping a coin to the left or to the right from the coin
observed in the previous step.



### The "Hat" notation

We can imagine that there is a cursor that points at \\(k\\)-th position at the
first step and when we flip the coin this cursor always moves to the next coin
in one of the two possible directions. We can indicate the coin at which the
cursor points before the flip was made with a "hat" symbol. For example, we can
start with the following sequence \\(HHTTHTHH\\) and go through 5 steps in order
to see how state evolves with the new notation

1. \\(HHTT\widehat{H}THH\\)
2. \\(HHT\widehat{T}TTHH\\)
3. \\(HHTH\widehat{T}THH\\)
4. \\(HHTHH\widehat{T}HH\\)
5. \\(HHTHHH\widehat{H}H\\)

In the first step, we can see that the sequence looks exactly like the initial
sequence except that there is a "hat" on top of the 5th coin (because the
original sequence has 5 \\(H\\)s). In the second step, we can see that the coin
in the  5th position changed from \\(H \to T\\) and the hat moved to the 4th
coin.




### The "Side hat" notation

We can go one step further and introduce another notation for the intermediate
step. In a single step we flip a coin and move the cursor to the next coin and
with an intermediate step we will be able to do one operation at a time. We can
imagine that each coin in the sequence "passes" the "hat" from right to the left
or from left to the right. In addition, we can say that every time a coin flips
(from \\(H \to T\\) or from \\(T \to H\\)) this hat falls and the other coin
next to the hat picks it up and the whole process continues. Whether hat falls
to the left or to the right from the coin depends on its initial state. When
\\(H\\) changes to \\(T\\) the hat falls to the left and to the right in the
opposite case. For example, instead of writing \\(H\widehat{H}T \to
\widehat{H}TT\\) we can write \\(H\widehat{H}T \to H \langle TT \to
\widehat{H}TT\\). With this new notation, previous sequence could be written in
the following way


1. \\(HHTT\widehat{H}THH\\)
2. \\(HHTT \langle T THH\\)
3. \\(HHT\widehat{T}TTHH\\)
4. \\(HHT H \rangle TTHH\\)
5. \\(HHTH\widehat{T}THH\\)
6. \\(HHTHH \rangle THH\\)
7. \\(HHTHH\widehat{T}HH\\)
8. \\(HHTHHH \rangle HH\\)
9. \\(HHTHHH\widehat{H}H\\)
10. \\(HHTHHH \langle T H\\)

It's important to note that we don't have to use intermediate steps all the
time. In fact, we can limit ourselves to one of the notations. For example, it
might be enough to avoid all of the odd steps and focus only on the steps with
even indices and in this case we will get the same step-by-step process, but in
a slightly different format.



### The "Sequence group" notation

Now we need to introduce one last notation. We can notice something interesting
in the way a sequence changes when there are multiple repeated face values in a
row. For example, let's say we have a sequence \\(\widehat{H}TTT\\) and if we
look through the first few steps we can notice some useful patterns.

1. \\(\widehat{H}TTT\\)
2. \\(H\widehat{H}TT\\)
3. \\(HH\widehat{H}T\\)
4. \\(HHH\widehat{H}\\)

Basically, repeated value of the coin forces us to apply the same operation over
and over until the game ends or a new value has been encountered. In order to
avoid repeating this operation over and over we can introduce notation in which
sequence of the repeated face values could be combined into a single group and
number of coins in this group could be represented with a subscript. This group
will be called **elementary group**. For example, we can look through a few
simple examples

1. \\(HHHTTHH \to H_3T_2H_2\\)
2. \\(HHHH \to H_4\\)
3. \\(HTHT \to H_1T_1H_1T_1\\)

Notice that these examples don't use the hat notation. We can simply assume that
hat could be always assigned to a group with one face value in it. Although we
can do it this will create some problems later when "hat" starts moving from one
face value to another. Instead, we can completely ignore "hat" notation and
focus only on the "side hat" notation (although similar trick could be done to
the "hat" notation). We can assume that in subsequence of the form \\(...H_m
\rangle...\\) hat on the right side always belongs to the right most coin in the
subsequence and the same applies to the \\(...\langle T_m...\\) with the only
difference that this time the side hat belongs to the left most element. In the
beginning of the game, we might encounter a problem when the cursor points to a
coin within an elementary group. We can see that with all new notations it
shouldn’t be a problem. For example, let's say we have the following sequence
\\(HHTTHTTHH\\).  For case like this we can assume that any group will be forced
to become separated into groups that can't be merged and this will be forced by
the visual separator. So the previous example will be transformed into the
following sequence \\(HHTTHTTHH \to H_2T_3 \rangle T_2H_2\\)



## Proof



For any sequence there is a large number of possible arrangements of an
elementary group into which sequence could be transformed. In the proof we
always assume that sequences are transformed into a sequence of elementary
groups in such a way that two groups with the same face value cannot be next to
each other. In some way it's very similar to the effect that coprimes have in
fractions in the sense that sequence cannot be compressed into a smaller number
of groups.

The goal of the proof is to show that any sequence of steps could be classified
as one operation on the original sequence after which the number of groups
always reduces by at least 1 unless the sequence could be expressed as a single
elementary group.






First, we focus our attention to the place with a "side hat" in it. These are
all possible options

1. \\(\langle T_N\\)
2. \\(H_N \rangle\\)
3. \\(...H_n \rangle T_m...\\)
4. \\(...H_m \langle T_n...\\)
5. \\(...H_n \rangle H_m...\\)
6. \\(...T_m \langle T_n...\\)



First and second options are quite trivial, because these are two special cases.
These cases represent the only two possibilities when the "side hat" operator
doesn't have any sequences on one of the sides. First case means that the game
just ended and the second case represents an arrangement in which the game will
end in exactly \\(N\\) steps. This implies that every sequence that could be
represented in the form of one group could be finished either in 0 steps (end of
the game) or exactly \\(N\\) steps, where \\(N\\) is an initial length of the
original sequence (a.k.a number of coins).



Third and Fourth are also quite simple cases. In the third sequence, we know
that after one step we get the following partition \\(...H_n \rangle T_m... \to
...H_{n+1} \rangle T_{m-1}... \\) and after \\(m\\) steps we will get \\(...H_n
\rangle T_m... \overset{m}{\to} ...H_{n+m} \rangle... \\). And the same could be
shown for the fourth sequence, since after \\(m\\) steps we will get \\(...H_m
\langle T_n... \overset{m}{\to} ... \langle T_{n+m}...\\).



The fifth case is a bit less straightforward, because after one step we will end
up with more elementary groups than we started with

$$
...H_n \rangle H_m... \to ...H_n \langle T_1 H_{m-1}...
$$

and after \\(m\\) steps we will get

$$
...H_n \rangle H_m... \overset{m}{\to} ...\langle T_{n+1} H_{m-1}...
$$

For the case \\(m=1\\) we get \\(H_{m-1}=H_0\\) which is a group with no coins.
It means that after \\(m\\) steps we managed to reduce the number of groups.
Let's consider the case where \\(m\ge2\\). We know that there has to be a group
to the left from \\(T_{n+1}\\), because there are some \\(H\\)s to the right and
the operator should point to the k-th coin. Also, we know that the group to the
left cannot be in the form \\(H_k\\), otherwise it would have been combined with
the \\(H_n\\), because we assume that two groups next to each other have two
different face values. It means that we have to have a sequence \\(...T_k
\langle T_{n+1} H_{m-1}...\\). We can see how this sequence changes overtime


$$
\begin{align}
...H_n \rangle H_m... &= ...T_kH_n \rangle H_m... \\
    & \overset{n+1}{\to} ...T_k \langle T_{n+1} H_{m-1}... \\
    & \overset{1}{\to} ...T_{k-1} H_1 \rangle T_{n+1} H_{m-1}... \\
    & \overset{n+1}{\to} ...T_{k-1} H_{n+2} \rangle H_{m-1}... \\
\end{align}
$$

We can see that pattern repeats and we will either run out of \\(T\\)s or
\\(H\\)s in one of the groups in which case again the number of elementary
groups in the sequence will be reduced. We can show that for cases where \\(k\ge
m\\) we will get a sequence

$$
...T_kH_n \rangle H_m... \overset{x}{\to} ...T_{k-m+1} \langle T_{n+2m-1+c}
$$

otherwise

$$
...T_kH_n \rangle H_m... \overset{y}{\to} ...H_{n+2k+c} \rangle H_{m-k}...
$$

where \\(x=(m + n)(2m - 1)\\), \\(y=(2k + 2n + 1)k\\) and \\(c\ge0\\). \\(c\\)
could be positive in case one of the formed group will be next to the other
group with the same face value in which case these groups will be merged based
on the initial assumption.



And the 6th case could be shown to be the same as the 5th case after a finite
number of steps. As in the 5th case we have the same problem and as before we
know that \\(T_n\\) cannot be the last elementary group in the sequence and we
cannot have another \\(T\\) which means that the next group in the sequence
should be of the form \\(H_k\\)


$$
...T_m \langle T_n... = ...T_m \langle T_n H_k...
$$

we can notice that after \\(n+1\\) steps we get sequence that looks exactly like
sequence from the 5th case

$$
...T_m \langle T_n H_k... \overset{n+1}{\to} ...T_{m-1}H_{n+1} \rangle  H_k...
$$

It means that the same logic could be applied to this case as well and we
guarantee to reduce the number of elementary groups after a finite number of
steps.






And finally, we can conclude that when there are 2 or more elementary groups in
the sequence than after a finite number of steps the number of basic groups will
be reduced. And for cases where we have only one basic group we know that either
we finished the game or the game will end in exactly \\(N\\) steps. These step
prove that from any initial condition the game could be ended in finite number
of steps



## Find expected number of steps



As part of the second task we need to find the expected number of steps that we
need to make in order to reach the end of the game with \\(N\\) coins. It looks
like a difficult problem, considering that there are \\(2^N\\) possible
arrangements of coins. We can make the problem quite simple by noticing an
interesting pattern.






Let's say we start with a random sequence of \\(N\\) coins. And now let's
imagine that we managed to find one extra coint, but instead of generating a new
sequence we just decide to add this new coin at the end of the sequence. We know
that the new coin should be either \\(T\\) or \\(H\\).

Let's consider both cases. How will the number of steps change in case the new
coin came up \\(T\\)? It's easy to show that this wouldn't make any difference,
because this last coin will never be flipped from \\(T \to H\\). The only way to
change \\(T \to H\\) is when we have \\(N+1\\) coins with \\(H\\). Even if the
first \\(N\\) coins are all \\(H\\)s the last one is always \\(T\\) meaning that
we will never have a situation where the cursor points to the \\((N+1)\\)-th
coin.



And now we can think about the second case where the last coin is \\(H\\).
Because we proved that the game always ends in a finite number of steps there
must be a way to convert any sequence of coins into an elementary group of the
form \\(T_{N+1}\\) (\\(N+1\\) because we started with \\(N\\) coins and added
one coin at the end of the sequence). Since the last coin is \\(H\\) we
definitely know that within this process there has to be one step in which we
will change the last coin from \\(H \to T\\). The last coin can be changed only
when we have \\(N+1\\) coins with face value \\(H\\) which means that at some
point sequence that ends with \\(H\\) should be transformed into the sequence of
the form \\(H_{N+1}\\) and then after \\(N+1\\) steps it will be transformed to
\\(T_{N+1}\\).



Now it looks like we got an inverse problem where we want to know what's the
expected number of steps after which sequence that ends with \\(H\\) converts to
\\(H_{N+1}\\). First, we can notice that just need to find a way to transform
first \\(N\\) coins to the sequence of the form \\(H_N\\) and because last coin
is always \\(H\\) we will automatically end up with the \\(H_{N+1}\\) sequence.

If we rephrase the original problem and count \\(T\\)s instead of \\(H\\)s and
flip coin at \\(N-k\\)-th position where counting starts from right to left we
will always get exactly the same sequences after every step. Now let's say we
replace \\(H \to T\\) and \\(T \to H\\), and count \\(H\\)s again, but still
numerating coins from right to left. Because we replaced \\(T \to H\\) it means
that at the end we want to get a sequence \\(H_N\\) rather than \\(T_N\\). And
finally, we can reverse the position of all coins in order to be able to count
from left to right without changing the initial index of the coin. This point of
view shows that each sequence has a pair that could be obtained by replacing all
\\(H \to T\\) and \\(T \to H\\) and reversing order of the coins. With this
point of view we know that the expected number of steps that we need to do to
form a sequence \\(H_N\\) is exactly the same as the expected number of steps
for the original problem.



And finally, if we say that \\(\mathbb{E}_N\\) is the expected number of steps
before the game with \\(N\\) coin ends then we can express it in the form

$$
\begin{align}
\mathbb{E}_N &= \frac{1}{2}\mathbb{E}_{N-1} + \frac{1}{2} (N + \mathbb{E}_{N-1})
\\
             &= \mathbb{E}_{N-1} + \frac{N}{2} \\
\end{align}
$$

It's also very easy to show that

$$
\mathbb{E}_1 = 1/2
$$.

It's \\(1/2\\) because game with one coin either ends immediately or after one
step, so expected value is equal to \\(1/2\\) (or we can say that for
\\(\mathbb{E}_{0}=0\\), because with no coins game ends immediately).

And finally we can see that

$$
\begin{align}
\mathbb{E}_N &= \sum_{i=1}^{N} \frac{i}{2} \\
             &= \frac{1}{2} \sum_{i=1}^{N} i \\
             &= \frac{N(N+1)}{4}
\end{align}
$$




