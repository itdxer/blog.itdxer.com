---
title: "Solutions for the IMO 2019 problems"
date: 2020-02-09
---
My solutions for the IMO 2019 problems. I'm an amature in mathematics which
means that these solutions might contain mistakes. Use them at your own risk

## Problem 1

![](http://blog.itdxer.com/images/imo-2019/imo-2019-problem-1.png)

### Solution

**Important observation:** Orders of the variables \\(a\\) and \\(b\\) matters
on the left, but not on the right

$$
f(2a) + 2f(b) = f(f(a+b)) = f(2b) + 2f(a)
$$

Next we can explore a few corner cases

**Explore function when a = 0**

$$
f(0) + 2f(b) = f(f(b)) \\
f(2b) + 2f(0) = f(f(b))
$$

we can multiply first equation by 2 and subtract second equation from it

$$
4f(b) - f(2b) = f(f(b))
$$

therefore

$$
4f(b) - f(2b) = f(2b) + 2f(0) \\
2f(b) - f(2b) = f(0) \\
f(2b) = 2f(b) - f(0)
$$

and finally

$$
f(2b) + 2f(a) = 2f(b) - f(0) + 2f(a) = f(f(a+b))
$$

**Explore function for c = a + 1 and d = b - 1**

$$
2f(a + 1) + 2f(b - 1) - f(0) = f(f(a+b)) = 2f(a) + 2f(b) - f(0) \\
f(a+1) - f(a) = f(b) - f(b - 1)
$$

\\(a\\) and \\(b\\) are independent from each other and we can set them equal to
any integer number. Based on this fact the derived euqation implies that
difference between function outputs evaluated on two subsequent integers is
constant. This means that \\(\,f\\) is a linear function

$$
f(a) = ka + c
$$

for some k and c

Let's plug this linear function into two different equations that we've derived
before

First, for cases when **b = 0**

$$
2f(a) + f(0) = f(f(a)) \\
2\,k\,a + 3c = k^2a + kc + c \\
2ka + 2c = k^2a + kc \\
4ka + 4c = 2k^2a + 2kc
$$

Second, for cases **a = b**

$$
2f(a) + 2f(a) - f(0) = f(f(2a)) \\
4ka + 3c = 2k^2a + kc + c \\
4ka + 2c = 2k^2a+kc
$$

We can subtract second equation from the first one and we will get that \\(2c =
kc\\) which means that \\(k = 2\\)

We can plug linear function with fixed k into the general formula

$$
f(2a) + 2f(b) = f(f(a+b)) \\
4a + c + 4b + 2c = f(2a + 2b + c) \\
4a + 4b + 3c = 4a + 4b + 3c
$$

this equality implies that relation will hold for any possible \\(c\\), but
because we know that function \\(f\\) always outputs integers, it means that
\\(c\\) has to be an integer.

**Final equation**

$$
f(a) = 2a + c
$$

where \\(c \in \mathbb{Z}\\)

## Problem 2

![](http://blog.itdxer.com/images/imo-2019/imo-2019-problem-2.png)

### Solution

[WORK IN PROGRESS]

## Problem 3

![](http://blog.itdxer.com/images/imo-2019/imo-2019-problem-3.png)

### Solution

It's obvious that the only way the game cannot be finished is when we a fully
connected graph or a sub-graph with 3 or more points. In this context, subgraph
is a subset of points that completely disconnect from all other points, but all
points within this set are connected to each other. It impossible to finish the
game because we need to have "missing" edges in the graph.

Another important observation is that with each step we reduce total number of
links in the graph by 2. There is a different way to see this event. Let's focus
on 3 nodes, namely A, B and C. Let's say A-B and A-C are connected, but B and C
are not connected (just like in the example above). We can say that A has 2
friends, B has 1 friend and C also has 1 friend. After 1 operation we get A with
no connections, which means that this person has 0 friends, but B and C have 1
friend each (exactly as it was before). Of course, B and C got different
friends, but number of friends remained the same. We can think that during each
step we reduce number of edges by 2 in one and only one node. It means that when
node has odd number of friends we will never be able to get 0 edges for this
node. Node with odd number of edges will have at least 1 edge at the end of the
game. But it's not a problem for nodes that have even number of nodes. For them,
node could be isolated from all other nodes which means that it will have zero
edges.

At least in principle we should be able to get to group of users with 0 or 1
connection, but we cannot just subtract 2 edges from some random node per each
event, since the node might not have legal moves that would allow us to get rid
of the two edges. Simple example is a fully connected graph that has 3 nodes
where each node is connected to each other.

Initially, we don't have any fully connected subgraphs in the graph. It's easy
to see, since the only 2 possible fully connected subgraphs should contain
either 1010 nodes with 1009 edges each or 1011 nodes with 1010 connections each.
Second case is impossible, since we have only 1009 nodes with 1010 edges. The
first option coud have been possible, but the problem is that we have 1009 nodes
with 1010 edges in addition to 1010 nodes with 1009 edges which means that we
cannot have fully connected subgraph with 1010 nodes and 1009 edges. It's easy
to see. Let's take 1 node that has 1010 friends. This node can be connected to
all other 1008 nodes with 1010 edges, but we will need 2 more nodes in order to
get 1010 edges. This means that this node has to be connected to atleast 2 nodes
that have 1009 connections. And this implies that each node with 1009 edges
should be connected to at least 1 node with 1010 friends and it means that we
cannot have fully connected subgraph

Since we don't have any fully connected subgraphs, the only reason why we might
not reach desirable goal is in case one fully connected subgraph will be formed.
We can show that any possible formation of a fully connected subgraph could be
prevented.

Let's say that we kept changing the graph by applying events to the random nodes
in the graph, we repeat this process until we reach state of the graph that's
one step from forming the fully connected subgraph. Let's say that we can put
all of the nodes, that will be formed into a fully connected subgraph in the
next step, into one set. With this configuration, there are two distinct ways in
which fully connected subgraph can be formed.  Either in the next step node in
this set will lose 2 connections after which fully connected subgraph will be
formed or there is another node outside of the graph which is connected to
exactly 2 nodes from the set and will lose 2 connections in the next step.

Let's consider the first case

![](http://blog.itdxer.com/images/imo-2019/graph-case-1.JPG)

On the image above, we can see that if we remove 2 edges from the node that has
\\(k\\) edges then fully connected subgraph will be formed (red line show a new
link that could be formed in the new step). But we can also see that it's not
the only step that we can perform. There are a few other steps that we can do
and one of them has been shown in the image above (green line). We can see that
after this step one of the nodes lost 2 connections and we no longer can create
a fully connected subgraph from the nodes in a single step. Basically, we can
see that formation of the fully connected graph can be prevented in this case.

Notice that to prevent formation of a fully connected subgraph, we had to use 4
nodes from the set of nodes, which means that \\(n \ge 3\\). Previous logic
doesn't work for case, for example, when \\(n=k=2\\), because in this case fully
connected subgraph will be formed and there will be no way of reducing number of
edges in each one of these nodes. Another way of looking at this problem by
noticing that we've selected node with \\(k\\)) connections to which we want to
apply main operation. There is no unique way of selecting it and every operation
is basically exactly the same (since we have a subgraph with 4 nodes and each
one of these nodes has 2 edges which means that graph has a certain symmetry to
it). This case will be considered separately, since it reveals a bigger problem
with subgraphs that contains only nodes that have only even number of edges.
This special case will be discussed at the very end.

Let's consider second case

![](http://blog.itdxer.com/images/imo-2019/graph-case-2.JPG)

Unlike in the previous example, we need only 3 nodes from the set to perform
this operation. After 2 steps our graph more than 1 step away from forming a
fully connected subgraph and it works for every \\(n \ge 2\\), \\(k\ge1\\) and
\\(l\ge1\\).

And finally, we need to make sure that we can prevent formation of a fully
connected subgraph in first case with \\(n=k=2\\). Let's explore this case. We
have 4 nodes and each node has 2 edges. In the next step we will inevitable get
3 nodes with 2 connections each which will be a fully connected graph. In fact,
subgraph in which all of the nodes have even number of edges will inevitably
form fully connected subgraph with at least 3 nodes.

[Add explanation to the last statement]

We can avoid formation of the graphs that have only nodes with even number of
edges in exactly the same way that we did it for the graphs that we've
considered before (those that were one step from forming a fully connected
subgraph). Basically, we need to consider cases after which we will get in the
next step a decoupled subgraph with all the nodes that have only even number of
edges and prevent it from happening in exactly the same way as in the previously
considered cases.

By following all of these steps we will guarantee that fully connected subgraphs
(with more then 2 nodes in them) will not be formed and therefor desirable goal
could be reached.

## Problem 4

![](http://blog.itdxer.com/images/imo-2019/imo-2019-problem-4.png)

**Discovering solutions manually**

It's easy to find a few simple solutions for small \\(n\\). For \\(n=1\\),
\\(k=1\\) and for \\(n=2\\), \\(k = 3\\). It's interesting to note that for
\\(n=4\\) we get \\(\frac{8!}{2}\\) which is not a solution, but nevertheless
it's pretty close.

**Rewriting expression with exponents**

we can express every multiplier on the right hand side \\((2^n - 2^k)\\) with
\\(2^k(2^{n-k} - 1)\\) and we will get
$$
(2^n - 1)(2^n - 2)(2^n - 4)...(2^n - 2^{n-1}) =
2^{\frac{n(n-1)}{2}}\prod^{n}_{m=1} (2^m - 1)
$$

Note that we separated odd from even numbers and in order to understand what
kind of \\(k\\)s are possible we need to strudy odd numbers

**Studying behaviour of the odd numbers**

for \\(f(n) = 2^n - 1\\) and first few \\(n\\) values we get the following table

| n  | f(n)      |
|----|--------------|
| 1  | 1            |
| 2  | 3            |
| 3  | 7            |
|  4 | 15=3*5       |
| 5  | 31           |
| 6  | 63=3*3*7     |
| 7  | 127          |
| 8  | 255=3*5*17   |
| 9  | 511=7*73     |
| 10 | 1023=11*3*31 |

From the table above we can make a few interesting observations

1. for \\(n=5\\) we get 31, which is a prime number. It means that for \\(n \ge
5\\), \\(k\ge31\\)
2. \\((2^n-1) \mod 7 = 0\\) when \\(n\\) is divisible by 3
3. \\((2^n-1) \mod 5 = 0\\) when \\(n\\) is divisible by 4

from 2nd and 3rd observations we can see that in the product \\(\prod^{n}_{m=1}
(2^m - 1)\\) we get more 5s than 7s which is quite unusual behaviour for the
\\(k!\\) function, since there we expect more 5s than 7s

it's easy to show that for any \\(n\ge9\\) we will always have more 7s than 5s,
which is a problem for \\(k!\\), since there we expect more 5s than 7s when we
factorize \\(k!\\) into primes. This statement implies that we will never get
any solutions for \\(n\ge9\\)

And finally, from the first most observation we can see that for \\(n\ge5\\),
\\(k\ge31\\). We've already tested solutions for \\(1\le n \le 4\\) and found 2
solutions, but for \\(k\ge31\\) we need to have way more factors that we really
get from the \\(2^n-1\\) numbers multiplied together. For example, there is no
prime number 29 in factorization from every \\(2^n-1\\) that we've calculated,
which means that we don't have solutions from \\(n\lt9\\) and therefore we don't
have more solutions apart those that has been already discovered

**All possible solutions**

1. \\(n=1\\) and \\(k=1\\)
2. \\(n=2\\) and \\(k=3\\)

## Problem 5

![](http://blog.itdxer.com/images/imo-2019/imo-2019-problem-5.png)

### Solution

[WORK IN PROGRESS]

## Problem 6

![](http://blog.itdxer.com/images/imo-2019/imo-2019-problem-6.png)

### Solution

[WORK IN PROGRESS]



