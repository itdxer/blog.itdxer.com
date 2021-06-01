---
title: "Martingale betting strategy in fair casino"
date: 2021-05-24
layout: post


description: "Article aims to correct claims made about the Martingale betting strategy in the Numberphile video and show that actual probability is equal to 50% rather than 1/e as has been stated in the video.

"



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
strategy which has been recently discussed in the Numberphile video.









<div class="responsive-youtube">
<iframe width="560" height="315" src="https://www.youtube.com/embed/zTsRGQj6VT4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div> 





In the video, it has been stated that if one decides to follow the strategy the
probability of doubling the initial amount of money approaches 1/e as the
initial amount approaches infinity. A simpler way to say it is that you get only
a 36-37% chance of doubling your money if you start with more than about 25\$
and you put 1\$ as a first bet.

I believe that the claim is false and actual probability is equal to 50%. The
goal of the article is to show that the produced result leads to strange
consequences and afterwards I want to prove that the actual probability is 50%.
At the very end, I will try to point to the actual mistake in the calculations
shown in the video.




## Assumptions



It's important to remember that calculations assume that a person that follows
the Martingale strategy plays in the casino on the fair roulette wheel. It means
that the probability of observing red equals to 50% and the other 50% of
observing black. In addition, the assumption of the fair casino assumes that
outcomes of all games are [i.i.d.](https://en.wikipedia.org/wiki/Independent_and
_identically_distributed_random_variables)




## Initial indicator of the problem



The most obvious problem with the formula shown in the video can be noticed if
you look at the probability of doubling the money if one enters the casino with
1\$. The formula says that

$$
P(2N\text{ | }N) = \left(1 - \frac{1}{N}\right)^N
$$

So if we plug \\(N=1\\) the formula says that the probability of doubling the
initial amount of money is equal to 0 which is nonsense, since you either win on
the first try and get 2\$ or lose everything with no other money to play with.

One might argue that the formula just gets more accurate when \\(N\\) increases,
but even that's not the case as will be shown later.




## Martingale strategy as two person zero-sum game



Rephrasing the problem can help to see why it's strange when the strategy
produces a probability of winning less than 50%.

Let's assume that person A enters the casino with \\(N\\) dollars and wants to
leave it with \\(2N\\) dollars. The person A is determined to follow the
Martingale strategy and play the fair roulette wheel until loses all of the
money in which case person A will have to leave the casino with nothing (0
dollars). Imagine that instead of going to a casino that person plays with
person B that also has \\(N\\) dollars and the game ends when person A or B ends
up with no money (and the other player will get \\(2N\\) dollars). It's easy to
see that if player A plays with another player or casino it has no effect on the
game since it doesn't change the final goal of the game or intermediate
outcomes. So each turn person A makes a bet by putting a certain amount of money
on red or balck and person B puts exactly the same amount of money on the
opposite color. The following set up exactly reflects how the casino works for
our specific problem and shows it from the perspective of the two person zero-
sum game. It's very easy to see why this is a zerosum game, because only one
person wins and takes all of the money on the table, so the loss for one person
is a gain for another. In addition, since our casino is fair and all outcomes
are i.i.d. It absolutely doesn't matter on which color we bet as long as the
person follows the specified strategy. We can also say that the flip of a coin
determines on which color person A has to bet, so that none of them actually
picks a color on which to bet.

The reason why probability below 50% is a strange result because it indicates
that person B has a larger probability of winning (above 50%) meaning that
strategy which person B follows is actually better. Notice that both players
start with the exact amount of money, they both have the exact random chance of
winning the game, but the strategy that they follow is the only thing that makes
them different. Person B actually follows a slightly different strategy compared
to person A. Recall that in Martingale strategy each time person A loses the
player has to bet double of what was lost and since person B bets the same
amount it means that it happens every time person B wins. Person B actually
follows quite the opposite strategy. Since the selected color doesn't have any
effect on the outcome, the conclusion actually indicates that strategy used by
person B is better. In order to see why the previous conclusion has to be true
(assuming that the Martingale strategy has probability of winning below 50%) for
the given set up we can try switching the strategy. Person A starts the first
bet with 1\$ as before and doubles it each time person A wins. It means that as
before Person B has to bet on the opposite color, but this time double the bet
each time person A wins or we can say that it happens each time person B loses
which is exactly the Martingale strategy.

Does it mean that by following a "bad" Martingale strategy we actually
discovered another strategy which can be profitable? The answer is NO, since as
you remember we started with the assumption that probability of winning is below
50% which as we will see later is false.




## Expected revenue for unknown winning probability



It can also be shown that probability below 50% produces negative expected
revenue, meaning that on average a person that follows Martingale strategy will
lose money. For example, if a person goes every day to the casino with \\(N\\)
dollars then more often than not that person will come out with no money and
losses from this daily "job" won't cover the expenses. The expected daily profit
can be calculated very easily, but notice that on successful days revenue will
be \\(N\\) dollars and on the other days it will be \\(-N\\).

$$
\begin{align}
\mathbb{E}[R] &= Np + (-N) (1 - p) \\
              &= (2p - 1)N
\end{align}
$$

where \\(R\\) is a daily profit and \\(p\\) is a probability of doubling the
initial amount of money on a specific day.
It's easy to see that for any \\(N\\) and \\(p \lt 0.5\\) expectation is
negative which means that overtime a player will be losing money. And from the
"zero-sum game" point of view we can easily see that casinos have positive
expected revenue even with the fair roulette wheel.

As has been stated before the main assumption is false and it can be shown that
both players have expected revenue equal to zero which at the same time proves
that for \\(N > 0\\) probability has to be equal to \\(0.5\\).




## Expected revenue



There are multiple ways to show that the actual probability of winning is 50%,
but I would like to continue with the most intuitive proof (in my opinion) which
is based on the previous findings and addresses the problem a bit less directly.
Specifically, I want to show that the expected revenue obtained by following the
Martingale strategy is equal to zero which will at the same time prove that the
probability of doubling the initial amount of money is 50% (see previous section
in order to understand how one conclusion follows from the other).

We can rewrite expectation using [the law of the total
expectation](https://en.wikipedia.org/wiki/Law_of_total_expectation)

$$
\begin{align}
\mathbb{E}[R\text{ | }N,D] &= \mathbb{E}[\mathbb{E}[R\text{ | }M,N,D]\text{ |
}N,D] \\
                           &= \mathbb{E}[\mathbb{E}[R\text{ | }M]\text{ | }N,D]
\end{align}
$$

where \\(R\\) is a revenue generated by the strategy, \\(N\\) is an initial
amount of money that player has, \\(D\\) is a desired amount of money that
player wants to get and \\(M\\) is a maximum number of steps that player can
play with the given amount of money (\\(M \geq 1\\)) one cycle of the Martingale
strategy.

Equation above implies that revenue is conditionally independent from \\(N\\)
and \\(D\\) given \\(M\\). It's easy to see that inner expectation doesn't
depend on \\(N\\) or \\(D\\) when \\(M\\) is known, but first we'll need to
slightly modify the problem in a way that wouldn't effect our expectation. We
can imagine the following process. Each time a player makes one dollar bet we
can say that the player starts a cycle of the Martingale strategy. Before
starting the cycle the player can calculate what is the maximum number of steps
the player can play in one cycle of the strategy given the amount of money that
the player has and we can call this value \\(M\\). It's perfectly fine that a
player can play and win at least once in less than \\(M\\) steps, it's just when
the player loses all games within a cycle then the cycle has to be terminated
and a new one begins in case the player has enough money. But we can imagine an
alternative process. The player can always play \\(M\\) games within a cycle. It
clearly happens anyway when player loses all \\(M\\) games, but when player wins
in \\(K\\) (\\(K \leq M\\)) games we can imagine that the player can just wait
near the table table the remaining \\(M-K\\) games without making any bets.
Waiting near the table has no effect on the expectation since the player doesn't
gain or lose money by doing that. So now in \\(M\\) games (including those where
player doesn't play the game) player can lose \\((-2^M + 1)\\) dollars with
\\(1/2^M\\) probability or win 1 dollar in which case conditional expectation
will be

$$
\begin{align}
\mathbb{E}[R\text{ | }M] &= \left(1 - \frac{1}{2^M}\right) \, + \frac{-2^M +
1}{2^M} \\
                         &= 0
\end{align}
$$

And since conditional expectation is equal to zero it means that distribution of
\\(M\\) is completely irrelevant to the final expectation and overall expected
revenue is \\(\mathbb{E}[R\text{ | }N, D] = 0\\).

If player starts with \\(N\\) dollars and wants to finish the game with \\(D\\)
dollars (for \\(D > N\\)) then the expected revenue will be

$$
\begin{align}
\mathbb{E}[R\text{ | }N, D] &= (D - N)p + (-N) (1 - p) \\
                            &= Dp - N
\end{align}
$$

but since expectation is equal to 0 we get

$$
p = \frac{N}{D}
$$

and if \\(D=2N\\) than \\(p=0.5\\)




## Simulation



Very basic simulation can show similar conclusions (they can't be exactly the
same) and a large number of simulations can produce probabilities very close to
0.5. In each simulation player enters the casino with 50\$ and plays on the fair
roulette wheel by following the Martingale strategy until wins 100\$ or loses
everything. When a player doesn't have enough money to double the previous bet,
the player gives up and starts another round by betting 1\$ and doubling each
time the person loses the game. We can run simulation 100,000 times and observe
that roughly 50% of the time game ends up with double the initial amount (and it
works for any positive \\(N\\))

Python code with the simulation can be found
[here](https://gist.github.com/itdxer/1d8f3ae5585671261475154aaa2d297e).



## Problem with the conclusion in the video



I believe that the main problem in the video happens by ignoring the possibility
of players recovering large losses from money that couldn't cover doubled the
amount of losses in the previous bet. Specifically, we can rewrite the initial
amount of money in the following way.

$$
N = 2^k - 1 + m
$$

where \\( 0 \leq m \lt 2^k\\) and \\(k \geq 1\\)

The new way of writing \\(N\\) allows us to derive the actual probability of
winning an extra dollar by following the Martingale strategy with a finite
budget. For any \\(N\\) we basically have a budget that allows us to continue
the Martingale strategy, but we will terminate it as soon as we run out of
budget (after \\(k\\) subsequent losses). The remaining \\(m\\) dollars can help
us to recover previous losses (which gives us another chance and increases
probability of winning). Notice also that \\(m\\) changes overtime (because
\\(N\\) changes) which means that the more successful games a player had before
the more likely the player will recover larger losses produced by the Martingale
strategy. The correct way to specify probability of winning can be shown to be

$$
\begin{align}
P(N+1\text{ | }N) = &P(N+1\text{ | }W,N)\,P(W\text{ | }N) + \\
                    &P(N+1\text{ | }L,N)\,P(L\text{ | }N)
\end{align}
$$

where \\(W\\) indicates that a player managed to win 1\$ by following the
Martingale strategy and \\(L\\) means that we ran out of money that would have
allowed us to continue following the strategy (\\(W\\) and \\(L\\) are the only
possible outcomes). In this case, it's obvious that \\(P(N+1\text{ | }W,N)=1\\),
because we started with \\(N\\) dollars and got 1\$ after following the
Martingale strategy. Also we can show that \\(P(N+1\text{ | }L,N) = P(N+1\text{
| }m)\\) which means that we lost \\(2^k-1\\) dollars and now we're left with
\\(m\\) dollars, which gives us a small probability of still recovering from our
initial losses and earning back \\(N+1\\) dollars. And at last, we can show that

$$
P(L\text{ | }N) = \frac{1}{2^k}
$$

and since \\(P(L\text{ | }N) = 1 - P(W\text{ | }N)\\) we get the following
result

$$
P(N+1\text{ | }N) = 1 - \frac{1}{2^k} + \frac{1}{2^k} P(N+1\text{ | }m)
$$

In addition, it's important to specify that \\(P(X\text{ | }0) = 0 \, \forall \,
X \gt 0 \\), because with no money there won't be an option to earn some.





