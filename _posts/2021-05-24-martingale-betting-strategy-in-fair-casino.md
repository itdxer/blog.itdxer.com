---
title: "Martingale betting strategy in fair casino"
date: 2021-05-24
layout: post


description: "The article aims to correct the claim about the martingale betting strategy in the Numberphile video and show that the actual probability is equal to 50% rather than 1/e, as stated in the video."



tags: ['math', 'statistics']

comments: true
share: true
---









<style>
img {margin: 0 auto;}
iframe {display: block; margin: 0 auto; padding-bottom: 1.5em;} 
.center {text-align: center;}
twitter-widget {margin: 0 auto;}
.responsive-youtube {overflow:hidden; padding-bottom:56.25%; position:relative; height:0; max-width: 560px; margin: 0 auto;}
.responsive-youtube iframe {left:0; top:0; height:100%; width:100%; position:absolute;}
</style>





## Problem



[Martingale strategy](https://shorturl.at/wyAOR) is a rather famous gambling
strategy that has been recently discussed in the Numberphile video.









<div class="responsive-youtube">
<iframe width="560" height="315" src="https://www.youtube.com/embed/zTsRGQj6VT4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div> 





In the video, it has been stated that if one decides to follow the strategy, the
probability of doubling the initial amount of money approaches 1/e as the
initial amount approaches infinity. A more straightforward way to say it is that
you get only a 36-37% chance of doubling your money if you start with more than
about 25\$ and you put 1\$ as a first bet.

The claim is false, and the actual probability equals 50%. The article aims to
show that the produced result leads to strange consequences, and afterward, I
want to prove that the true probability is 50%. Ultimately, I will point to the
actual mistake in the calculations shown in the video.



## Assumptions



It's important to remember that calculations assume a person following the
martingale betting strategy plays in the casino on the fair roulette wheel. It
means that the probability of observing red equals 50% and the other 50% of
observing black. In addition, the assumption of the fair casino implies that
outcomes of all games are [i.i.d.](https://en.wikipedia.org/wiki/Independent_and
_identically_distributed_random_variables)



## Initial indicator of the problem



The most obvious problem with the formula shown in the video can be noticed if
you look at the probability of doubling the money if one enters the casino with
1\$. The formula says that

$$
P(2N\text{ | }N) = \left(1 - \frac{1}{N}\right)^N
$$

So if we plug \\(N=1\\), the formula says that the probability of doubling the
initial amount of money equals 0, which is nonsense, since you either win on the
first try and get 2\$ or lose everything.

One might argue that the formula gets more accurate when \\(N\\) increases, but
that's not the case, as will be shown later.



## Optional stopping theorem



[Martingale](https://en.wikipedia.org/wiki/Martingale_(probability_theory)) is
also a name for the general family of stochastic processes, and the game
described in the video is one of them. The most famous result associated with
martingales is the [optional stopping
theorem](https://en.wikipedia.org/wiki/Optional_stopping_theorem). According to
the theorem, no strategy can modify your initial expectation, meaning that the
martingale betting strategy and "all-in" betting strategy would have precisely
the same expectation, namely 50%.

Even without any knowledge about martingales, there are ways to convince
ourselves that the answer is wrong.



## Martingale strategy as two person zero-sum game



Rephrasing the problem can help us to see why it's strange when the strategy
produces a probability of winning less than 50%.

Let's assume that Alice enters a casino with \\(N\\) dollars and wants to play
the game until she wins \\(2N\\) dollars. Alice is determined to follow the
martingale betting strategy and play the fair roulette wheel until she loses all
of the money, in which case Alice will have to leave the casino with no money.
Imagine that instead of going to a casino, Alice plays with her friend Bob that
also has \\(N\\) dollars, and the game ends when Alice or Bob ends up with no
money (and the other player gets \\(2N\\) dollars). It's easy to see that if
Alice plays with Bob or a casino, it has no effect on the game since it doesn't
change the game's final goal or intermediate outcomes. So each turn, Alice makes
a bet by putting a certain amount of money on red or black, and Bob puts the
same amount on the opposite color. The following setup exactly reflects how the
casino works for our specific problem and shows it from the perspective of the
two-person zero-sum game. It's easy to see why this is a zero-sum game because
only one person wins and takes all the money on the table, so the loss for one
person is a gain for another. In addition, since our casino is fair and all
outcomes are i.i.d., it absolutely doesn't matter on which color we bet as long
as the person follows the specified strategy. We can also say that the coin flip
determines which color Alice has to bet, so neither Bob nor Alice pick a color
on which to bet.

Now we can go back to our original problem and understand why the probability
below 50% is strange. A probability below 50% indicates that Bob has a larger
probability of winning (above 50%), meaning that strategy that Bob follows is
better. Notice that both players start with the exact amount of money and have
the exact random chance of winning the game, but the strategy they follow is the
only thing that makes them different. Bob actually follows a slightly different
strategy compared to Alice. Recall that in the martingale betting strategy, each
time Alice loses, she has to bet double of what was lost, and since Bob bets the
same amount, it means that it happens every time Bob wins. Bob actually follows
quite the opposite strategy. Since the selected color doesn't affect the
outcome, the conclusion indicates that the strategy used by Bob is better.

Does it mean that by following the martingale betting strategy, we discovered
another strategy that can be profitable? The answer is no, since, as you
remember, we started with the assumption that the probability of winning is
below 50%, which, as we will see later, is false.



## Expected revenue for unknown winning probability



It can be shown that a probability below 50% produces negative expected revenue,
meaning that, on average, a person that follows the martingale betting strategy
will lose money. For example, if a person goes every day to the casino with
\\(N\\) dollars, then more often than not, that person will come out with no
money, and losses from this daily "job" won't cover the expenses. The expected
daily profit can be calculated very easily, but notice that on successful days
revenue will be \\(N\\) dollars, and on the other days, it will be \\(-N\\).

$$
\begin{align}
\mathbb{E}[R] &= Np + (-N) (1 - p) \\
              &= (2p - 1)N
\end{align}
$$

where \\(R\\) is a daily profit and \\(p\\) is the probability of doubling the
initial amount of money on a specific day and the expectation is implicitly
conditions on \\(N\\) and \\(p\\).
It's easy to see that for any \\(N \gt 0\\) and \\(p \lt 0.5\\), the expectation
is negative, meaning that a player will lose money over time. And from the
"zero-sum game" point of view, we can see that casinos have positive expected
revenue even with the fair roulette wheel.

As stated before, the main assumption is false, and it can be shown that both
players have expected revenue equal to zero, which simultaneously proves that
for positive \\(N\\), probability has to be equal to 50%.



## Expected revenue



There are multiple ways to show that the actual probability of winning is 50%,
but I would like to continue with the most intuitive proof (in my opinion),
which is based on the previous findings and addresses the problem a bit less
directly. Specifically, I want to show that the expected revenue obtained by
following the martingale betting strategy is equal to zero, which will, at the
same time, prove that the probability of doubling the initial amount of money is
50% (see the previous section to understand how one conclusion follows from the
other).

We can rewrite expectation \\(\mathbb{E}[R]\\) using [the law of the total
expectation](https://en.wikipedia.org/wiki/Law_of_total_expectation)

$$
\begin{align}
\mathbb{E}[R] &= \mathbb{E}[\mathbb{E}[R\text{ | }T]] \\
                           &= \mathbb{E}[\mathbb{E}[\sum_{t=1}^{T}R_t\text{ |
}T]] \\
                           &= \mathbb{E}[\sum_{t=1}^{T}\mathbb{E}[R_t\text{ |
}T]] \\
\end{align}
$$

where \\(R\\) is the total revenue generated by the strategy, \\(T\\) is the
total number of martingale cycles encountered in the game, and \\(R_t\\) is a
revenue on \\(t\\)-th cycle. It's important to clarify at this point the meaning
of the term "martingale cycle". The strategy follows "cycles" where each cycle
begins with a fixed bet (e.g., 1\\\$) and continues until we either win or can
no longer double the previous amount.

We can apply the law of total expectation one more time to the inner most
expectation by implicitly defining a distribution of steps \\(K\\) in the
\\(t\\)-th cycle.

$$
\mathbb{E}[R_t\text{ | }T] = \mathbb{E}[\mathbb{E}[R_t\text{ | }K,T]\text{ | }T]
$$

In \\(K\\) steps of a cycle a player can lose \\((2^K - 1)\\) dollars with
\\(1/2^K\\) probability or win 1\\\$ in which case conditional expectation will
be

$$
\mathbb{E}[R_t\text{ | }K,T]= \left(1 - \frac{1}{2^K}\right) \, - (2^K -
1)\frac{1}{2^K} = 0
$$



And since the conditional expectation is equal to zero, it means that
distributions over \\(T\\) and \\(K\\) are completely irrelevant to the final
expectation and overall expected revenue is zero, \\(\mathbb{E}[R] = 0\\). So if
player starts with \\(N\\) dollars and wants to finish the game with \\(D\\)
dollars (for \\(D > N\\)) then the expected revenue will be

$$
\begin{align}
\mathbb{E}[R] &= (D - N)p + (-N) (1 - p) \\
                            &= Dp - N
\end{align}
$$

but since the expectation is equal to zero we get

$$
p = \frac{N}{D}
$$

and if \\(D=2N\\) than \\(p=0.5\\)





## Simulation



Simple simulation can show similar conclusions (they can't be exactly the same),
and a large number of simulations can produce probabilities very close to 0.5.
Each simulation player enters the casino with 50\$ and plays on the fair
roulette wheel by following the martingale betting strategy until the player
wins 100\$ or loses everything. When a player doesn't have enough money to
double the previous bet, the player gives up and starts another round by betting
1\$ and doubling each time the person loses the game. We can run simulation
100,000 times and observe that roughly 50% of the time game ends with double the
initial amount (and it works for any positive \\(N\\))

Python code with the simulation can be found
[here](https://gist.github.com/itdxer/1d8f3ae5585671261475154aaa2d297e).



## Problem with the conclusion in the video



I believe that the main problem in the video happens because it was ignored that
a player can recover large losses from money that couldn't cover doubled the
amount of losses in the previous bet. Specifically, we can rewrite the initial
amount of money in the following way.

$$
N = 2^k - 1 + m
$$

where \\( 0 \leq m \lt 2^k\\) and \\(k \geq 1\\)

The new way of writing \\(N\\) allows us to derive the probability of winning a
dollar by following the martingale betting strategy with a finite budget. For
any \\(N\\), we have a budget that allows us to continue the strategy, but we
will terminate it as soon as we run out of budget (after \\(k\\) subsequent
losses). The remaining \\(m\\) dollars can help us to recover previous losses
(which gives us another chance and increases the probability of winning). Notice
also that \\(m\\) changes over time (because \\(N\\) changes), which means that
the more successful games a player had before, the more likely that the player
will recover larger losses. The correct way to specify the probability of
winning can be shown to be

$$
\begin{align}
P(N+1\text{ | }N) = &P(N+1\text{ | }W,N)\,P(W\text{ | }N) + \\
                    &P(N+1\text{ | }L,N)\,P(L\text{ | }N)
\end{align}
$$

where \\(W\\) indicates that a player managed to win 1\$ by following the
strategy for one cycle, and \\(L\\) means that we ran out of money and can no
longer continue with the cycle (\\(W\\) and \\(L\\) are the only possible
outcomes). In this case, it's evident that \\(P(N+1\text{ | }W,N)=1\\) because
we started with \\(N\\) dollars and got 1\$ after following the martingale
betting strategy. Also, we can show that \\(P(N+1\text{ | }L,N) = P(N+1\text{ |
}m)\\) which means that we lost \\(2^k-1\\) dollars and now we're left with
\\(m\\) dollars, which gives us a small probability of recovering from our
initial losses and earning back \\(N+1\\) dollars. And at last, we can show that

$$
P(L\text{ | }N) = \frac{1}{2^k}
$$

and since \\(P(L\text{ | }N) = 1 - P(W\text{ | }N)\\) we get the following
result

$$
P(N+1\text{ | }N) = 1 - \frac{1}{2^k} + \frac{1}{2^k} P(N+1\text{ | }m)
$$

The formula above slightly differs from the one produced in the video and
highlights the mistake.




