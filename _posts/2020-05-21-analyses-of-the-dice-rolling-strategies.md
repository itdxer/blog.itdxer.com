---
title: "Analyses of the dice rolling strategies"
date: 2020-05-21
---
## Problem

Problem from the [FiveThirtyEight](https://fivethirtyeight.com/features/can-you-
find-the-best-dungeons-dragons-strategy/) website

> The fifth edition of Dungeons & Dragons introduced a system of “advantage and
disadvantage.” When you roll a die “with advantage,” you roll the die twice and
keep the higher result. Rolling “with disadvantage” is similar, except you keep
the lower result instead. The rules further specify that when a player rolls
with both advantage and disadvantage, they cancel out, and the player rolls a
single die. Yawn!
>
> There are two other, more mathematically interesting ways that advantage and
disadvantage could be combined. First, you could have “advantage of
disadvantage,” meaning you roll twice with disadvantage and then keep the higher
result. Or, you could have “disadvantage of advantage,” meaning you roll twice
with advantage and then keep the lower result. With a fair 20-sided die, which
situation produces the highest expected roll: advantage of disadvantage,
disadvantage of advantage or rolling a single die?
>
> Extra Credit: Instead of maximizing your expected roll, suppose you need to
roll N or better with your 20-sided die. For each value of N, is it better to
use advantage of disadvantage, disadvantage of advantage or rolling a single
die?

## Deriving statistics for 3 strategies

### Notations


- \\(N\\) - number of sides on a die
- \\(b\\) - number on one of the sides of the die, \\(b \in [1, N]\\)
- \\(x, y, z, u, v\\) - are results obtained from throwing a single die (results
in range \\([1, N]\\))

$$
\max(x, y)=
\begin{cases}
    x,& \text{if } x\geq y\\
    y,              & \text{otherwise}
\end{cases}
$$

$$
\min(x, y)=
\begin{cases}
    x,& \text{if } x\leq y\\
    y,              & \text{otherwise}
\end{cases}
$$




### Abbreviations

- **PMF** - Probability mass funciton
- **CMF** - Cumulative mass funciton

### Rolling a signle die

PMF:

$$
p(b) = p(x = b) = \frac{1}{N}
$$

CMF:

$$
P(b) = p(x \le b) = \frac{b}{N}
$$

### Advantages

This strategy is only needed in order to calculate a bit more complicated
strategies that are only based on advantages and disadvantages. We need to find
PMF

$$
p(\max(x, y) = b)
$$

This problem could be solved rather easily by noticing that \\(max(x, y)\\)
equals \\(b\\) either when \\(x = y = b\\) or one of the variables is equal to
\\(b\\) but the other is smaller than \\(b\\). When one value is smaller than
the other because there are two possibilities in which either \\(x=b\\) or
\\(y=b\\) which means we need to count these cases twice. These observations
lead to the following PMF

$$
\begin{align}
p(\max(x, y) = b) &= \sum_{i=1}^{b-1} 2\,p(b)\,p(i) + p(b)\,p(b) \\
                 &= 2\,p(b)\,\sum_{i=1}^{b-1} p(i) + p(b)^2 \\
\end{align}
$$

and by replacing \\(p(b)\\) and \\(p(i)\\) with PMF values from the single roll
strategy we get the following PMF

$$
\begin{align}
p(\max(x, y) = b) &= \frac{2}{N}\,\sum_{i=1}^{b - 1} \frac{1}{N} + \frac{1}{N^2}
\\
                 &= \frac{2b - 1}{N^2} \\
\end{align}
$$

### Disadvantages

Similar logic could be applied to the disadvantages strategy in which case we
will get the following PMF

$$
\begin{align}
p(\min(x, y) = b) = 2\,p(b)\,\sum_{i=b+1}^{N} p(i) + p(b)^2 \\
\end{align}
$$

and by replacing \\(p(b)\\) and \\(p(i)\\) with PMF values from the single roll
strategy we get the following PMF

$$
\begin{align}
p(\min(x, y) = b) &= \frac{2}{N}\,\sum_{i=b+1}^{N} \frac{1}{N} + \frac{1}{N^2}
\\
                 &= \frac{2 (N - b) + 1}{N^2} \\
\end{align}
$$

From PMF we can see that advantages and disadvantages have the same shape,
expect that one distributions is a flipped version of the other distribution






### Disadvantage of advantages

For this problem general PMF formula for disadvantages could be applied here as
well

$$
\begin{align}
p(\min(\max(x, y), \max(u, v)) = b) = 2\,p(b)\,\sum_{i=b+1}^{N} p(i) + p(b)^2 \\
\end{align}
$$

The only difference is that now we need to use PMF from advanages rather than
from a single roll distribution

$$
\begin{align}
p(\min(\max(x, y), \max(u, v)) = b)
    &= \left(\frac{2b - 1}{N^2}\right)^2 + 2 \frac{2b - 1}{N^2} \,
\sum_{i=b+1}^{N^2} \frac{2i - 1}{N^2} \\
    &= \frac{1}{N^4}(-4\,b^3 + 6\,b^2 + 4\,b\,(N^2-1) - 2\,N^2+1)
\end{align}
$$

And from PMF it's easy to find CMF

$$
\begin{align}
p(\min(\max(x, y), \max(u, v)) \leq b) = \frac{1}{N^4}(2\,b^2\,N^2 - b^4)
\end{align}
$$

### Advantage of disadvantages

For this problem we can apply general formula for advantages

$$
\begin{align}
p(\max(\min(x, y), \min(u, v)) = b) = 2\,p(b)\,\sum_{i=1}^{b-1} p(i) + p(b)^2 \\
\end{align}
$$

And similarly we can derive PMF

$$
\begin{align}
p(\max(\min(x, y), \min(u, v)) = b) = \frac{1}{N^4}(
    &4\,b^3 - 6\,b^2\,(2\,N + 1)\,+ \\
    &+4\,b\,(2\,N^2 + 3\,N + 1) - (2\,N+1)^2)
\end{align}
$$

And as before we can calculate CMF

$$
\begin{align}
p(\max(\min(x, y), \min(u, v)) \leq b) = \frac{1}{N^4}(b^4 - 4Nb^3 + 4N^2b^2)
\end{align}
$$

## Which strategy is more likely to produce 20?

From the PMF we can set \\(N=b=20\\) and check the results

- Single roll strategy: \\(p(x = 20) = 0.05\\)
- Disadvantage of advantages: \\(p(x = 20) = \frac{39^2}{400^2} \approx 0.01 \\)
- Advantage of disadvantage: \\(p(x = 20) = \frac{801}{400^2} \approx 0.005 \\)

From these values we can see that a signle dice roll is a much more likely to
produce 20 on a 20-sided dice.

## Which strategy is more likely to produce value above some fixed number?

For this problem we need to focus on CMF values.

$$
P(x\geq b) \geq P(y\geq b) \\
1 - P(x\lt b) \geq 1 \ - P(y\lt b) \\
1 - P(x\leq b - 1) \geq 1 \ - P(y\leq b - 1) \\
P(x\leq b - 1) \leq P(y\leq b - 1)
$$

we will try to find for which \\(b\\)s the following inequality holds, but we
need to remember that true values needs to be adjusted by one unit

$$
P(x\leq b) \leq P(y\leq b)
$$

### Comparing disadvantage of advantages with advantage of disadvantages


$$
\begin{align}
P(x\leq b) &\leq P(y\leq b) \\
p(\min(\max(x, y), \max(u, v)) \leq b) &\leq p(\max(\min(x, y), \min(u, v)) \leq
b) \\
\frac{1}{N^4}(2\,b^2\,N^2 - b^4) &\leq \frac{1}{N^4}(b^4 - 4Nb^3 + 4N^2b^2)
\end{align}
$$

by rearranging the terms we can find that this inequality holds when

$$
(b-N)^2 \geq 0
$$

and this is true for every \\(b\\) which means that **disadvantage of advantages
is always better compare to advantage of disadvantages**.






### Comparing disadvantage of advantages with a single roll strategy


$$
\begin{align}
P(x\leq b) &\leq P(y\leq b) \\
p(\min(\max(x, y), \max(u, v)) \leq b) &\leq p(z \leq b) \\
\frac{1}{N^4}(2\,b^2\,N^2 - b^4) &\leq \frac{b}{N}
\end{align}
$$

by rearranging the terms we can find that this inequality holds when

$$
(N - b)(N^2 - N\,b - b^2) \geq 0
$$

and since \\(N \geq b\\) the whole inequality will be true when \\((N^2 - N\,b -
b^2) \geq 0\\). This is a quadratic equation with two roots.

$$
(N^2 - N\,b - b^2) = -(b + N \phi)(b - \frac{N}{\phi})
$$

where \\(\phi\\) is a golden ration

$$
\phi = \frac{\sqrt{5} + 1}{2}
$$

And this equation could be greater than 0 only when \\(b \leq \frac{N}{\phi}\\)
(although since \\(\phi\\) is irrational and \\(N\\) and \\(b\\) are integers
equality will never be possible).

But in the original equation we subtracted 1 from \\(b\\) which means that the
following condition should be true in order to have better probability of
reaching the desired result with disadvantage of advantages strategy compared to
the single roll strategy.

$$
b \leq \frac{N}{\phi} + 1
$$




### Comparing advantage of disadvantages with a single roll strategy


$$
\begin{align}
P(x\leq b) &\leq P(y\leq b) \\
p(\max(\min(x, y), \min(u, v)) \leq b) &\leq p(z \leq b) \\
\frac{1}{N^4}(b^4 - 4Nb^3 + 4N^2b^2) &\leq \frac{b}{N}
\end{align}
$$

by rearranging the terms we can find that this inequality holds when

$$
(N - b)(b^2 - 3bN + N^2) \geq 0
$$

and as before, since \\(N - b \geq 0\\) we only need to have the following
inequality to hold

$$
b^2 - 3bN + N^2 \geq 0
$$

quadratic equation has two roots and could be written in the following form

$$
b^2 - 3bN + N^2 = (b - \phi^2 N)\left(b - \frac{N}{\phi^2}\right)
$$

left term is always negative for \\(b \leq N\\) which means that the only
condition when above equation holds can happen only when

$$
b \leq \frac{N}{\phi^2}
$$

and as before we need to add 1, because \\(b - 1\\) was replaced with \\(b\\) in
the initial equation

$$
b \leq \frac{N}{\phi^2} + 1
$$

## Conclusion

Assuming that \\(N=20\\) the following conclusions could be made

1. Disadvantage of advantages is always better than advantage of disadvantages
2. Disadvantage of advantages is better than single roll only when \\(b \leq
13\\)
3. Advantage of disadvantages is better than single roll only when \\(b \leq
8\\)


## Simulations

All of the conclusions could be verified with simple simulations

- [Simulation
#1](https://gist.github.com/itdxer/8a5d073965abaeb0a3bc2cab3b9951fc)
- [Simulation
#2](https://gist.github.com/itdxer/a9556e09a2c5ee1e0c9226419d79eb80)
