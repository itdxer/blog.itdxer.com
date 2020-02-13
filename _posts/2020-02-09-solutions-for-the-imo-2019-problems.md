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

There are 2 different ways where \\(PQ\\) can be located and each location
produces slightly different solutions. We will ignore case where \\(P=Q\\) since
in this way we won't count them as a line that's parallel to \\(AB\\), although
it will still count as a solution since \\(PP_1Q_1\\) is a triangle and any
triangle is concyclic.

Since \\(AA_1\\) and \\(BB_1\\) intersect (let's call this intersection point
\\(O\\)) we can consider 2 main cases. First case is when \\(PQ\\) is closer to
\\(AB\\) compare to the \\(O\\) (if we compare their shortest distances) and
second case is just the opposite one.

**Let's consider first case**

[ADD IMAGE]

Let's say

$$
\angle CBA = \angle CQ_1Q = b \\
\angle BAC = \angle PP_1C = a \\
$$

$$
\angle ABP_1 = y \implies \angle AB_1B = 180 - a - y \implies \angle ACP_1 = y
$$

since \\(\angle ACP_1 = \angle ABP_1\\) then \\( ABCP_1\\) are concyclic



$$
\angle BAQ = x \implies \angle AA_1B = 180 - b - x = \angle Q_1A_1C \implies
\angle A_1QC = x
$$

since \\(\angle A_1QC = \angle BAQ\\) then \\( ABQ_1C \\) are concyclic

Now we can see that

1. \\(\angle AP_1B = \angle ACB\\), becase  \\( ABCP_1\\) are concyclic
2. \\(\angle AC_1A = \angle ACB\\), becase  \\( ABQ_1C \\) are concyclic

This implies that \\(\angle AP_1B = \angle BQ_1A\\) and it means that
\\(ABQ_1P_1\\) are concyclic

And finally, we can see that \\(\angle QPP_1 = \angle QQ_1P = y\\) which implies
that \\(QPQ_1P_1\\) are concyclic.

**Let's consider second case**

[ADD IMAGE]

Let's say

$$
\angle ABP_1 = \angle AQ_1P_1 = \angle BPQ = y \\
\angle BAQ = \angle BP_1Q_1 = \angle AQP = x \\
\angle QQ_1P = v \\
\angle PP_1Q = w \\
$$

From this we can see that

$$
\angle PQQ_1 = 180 - x \implies \angle QPQ_1 = x - v \\
\angle P_1PQ_1 = 180 - x - y + v \\
\\
\angle QPP_1 = 180 - y \implies \angle PQP_1 = y - w \\
\angle PQQ_1 = 180 - x - y + w
$$

By the law of sines from the \\(PP_1Q\\) triangle

$$
\frac{P_1Q}{\sin(180-y)}=\frac{PQ}{\sin(w)}
$$

By the law of sines from the \\(PQ_1Q\\) triangle

$$
\frac{PQ}{\sin(v)}=\frac{PQ_1}{\sin(180 - x)}
$$

Then

$$
PQ = \frac{PQ_1 \, \sin(v)}{\sin(180 - x)} = \frac{P_1Q \, \sin(w)}{\sin(180-y)}
\\
\frac{PQ_1 \, \sin(v)}{\sin(x)} = \frac{P_1Q \, \sin(w)}{\sin(y)} \\
\frac{PQ_1}{\sin(x)} = \frac{P_1Q \, \sin(w)}{\sin(v) \, \sin(y)}
$$

By the law of sines from the \\(PP_1Q_1\\) triangle

$$
\frac{P_1Q_1}{\sin(180-x-y+v)}=\frac{PQ_1}{\sin(x)}
$$

By the law of sines from the \\(P_1Q_1Q\\) triangle

$$
\frac{P_1Q_1}{\sin(180-x-y+w)}=\frac{P_1Q}{\sin(y)}
$$

Then

$$
P_1Q_1 = \frac{PQ_1 \, \sin(x + y - v)}{\sin(x)} = \frac{P_1Q \, \sin(x + y -
w)}{\sin(y)} \\
\frac{PQ_1}{\sin(x)} = \frac{P_1Q \, \sin(x + y - w)}{\sin(y) \, \sin(x + y -
v)} \\
$$

Now we can combine previous equations to get

$$
\frac{P_1Q \, \sin(x + y - w)}{\sin(y) \, \sin(x + y - v)} = \frac{P_1Q \,
\sin(w)}{\sin(v) \, \sin(y)} \\
\frac{\sin(x + y - w)}{\sin(x + y - v)} = \frac{\sin(w)}{\sin(v)} \\
\sin(y)\sin(x + y - w) = \sin(x + y - v) \sin(w)
$$

Using the following equation we can expand sine functions \\(\sin(a - b) =
\sin(a)\cos(b) - \sin(b)\cos(a)\\)

$$
\sin(v)\sin(x+y)\cos(w) - \sin(v)\sin(w)\cos(x+y) = \sin(w)\sin(x+y)\cos(v) -
\sin(w)\sin(v)\cos(x+y) \\
\sin(v)\sin(x+y)\cos(w) = \sin(w)\sin(x+y)\cos(v)
$$

since \\(0 \lt (x + y) \lt 180 \implies sin(x+y) \ne 0\\) there for we can
cancel it from the previous equation in order to get

$$
\sin(v)\cos(w) - \sin(w)\cos(v) = 0 \\
sin(w - v) = 0
$$

There are infinitely many solutions to this equations and all of them could be
described by \\(w - v = 180k\\), where \\(k \in N\\)

In addition we know that \\(0 \lt v \lt 180 \implies -180 \lt -v \lt 0 \\) and
\\(0 \lt w \lt 180\\) therefore \\(-180 \lt (w - v) \lt 180\\). This means that
\\(k=0\\) is the only solution which implies that \\(w=v\\) and this proves that
\\(P_1PQQ_1\\) are concyclic.

## Problem 3

![](http://blog.itdxer.com/images/imo-2019/imo-2019-problem-3.png)

### Solution

It's obvious that the only way the game cannot be finished is when a fully
connected graph or a sub-graph with 3 or more nodes is created. In this context,
subgraph is a subset of nodes which is completely disconnect from all other
nodes, but all nodes within this set are connected to each other. It impossible
to finish the game because we need to have "missing" edges in the graph.

Another important observation is that with each step we reduce total number of
links in the graph by 2. For example, let's focus on 3 nodes, namely A, B and C.
Let's say A-B and A-C are connected, but B and C are not connected (just like in
the example above). We can say that A has 2 friends, B has 1 friend and C also
has 1 friend. After 1 operation we get A with no connections, which means that
this person has 0 friends, but B and C have 1 friend each (exactly as it was
before). Of course, B and C got different friends, but number of friends
remained the same. We can think that during each step we reduce number of edges
by 2 in one and only one node. It means that when node has odd number of friends
we will never be able to get 0 edges for this node. Node with odd number of
edges will have at least 1 edge at the end of the game. But it's not a problem
for nodes that have even number of nodes. For them, node could be isolated from
all other nodes which means that it will have 0 edges.

At least in principle, we should be able to get to group of users with 0 or 1
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
to see. Let's take 1 node that has 1010 edges. This node can be connected to all
other 1008 nodes with 1010 edges, but we will need to connect it to 2 more nodes
in order to get 1010 edges. This means that this node has to be connected to at
least 2 nodes that have 1009 connections. And this implies that each node with
1009 edges should be connected to at least 1 node with 1010 friends and it means
that we cannot have fully connected subgraph

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
\\(k\\) edges then a fully connected subgraph will be formed (red line shows a
new link that could be formed in the new step). But we can also see that it's
not the only step that we can perform. There are a few other steps that we can
do and one of them has been shown in the image above (green line). We can see
that after this step one of the nodes lost 2 connections and we no longer can
create a fully connected subgraph from the nodes in a single step. Basically, we
can see that formation of the fully connected graph can be prevented in this
case.

Notice that to prevent formation of a fully connected subgraph, we had to use 4
nodes from the set of nodes, which means that \\(n \ge 3\\). But we don't have
to have 4 nodes. We can just connect node to the 3rd node from this set to which
it's hasn't been connected yet. But even then we will still have a problem for
case, for example, when \\(n=k=2\\), because in this case fully connected
subgraph will be formed and there will be no way of reducing number of edges in
each one of these nodes. This case will be considered separately, since it
reveals a bigger problem with subgraphs that contains only nodes that have only
even number of edges. This special case will be discussed at the very end.

Let's consider second case

![](http://blog.itdxer.com/images/imo-2019/graph-case-2.JPG)

Unlike in the previous example, we need only 3 nodes from the set to perform
this operation. After 2 steps our graph more than 1 step away from forming a
fully connected subgraph and it works for every \\(n \ge 2\\), \\(k\ge1\\) and
\\(l\ge1\\). Nevertheless, we still can have problems with this approach, for
example, for case when \\(n=k=l=2\\). This case will require the same similar
solution to the first case.

And finally, we need to make sure that we can prevent formation of a fully
connected subgraph in first case and seconds cases when \\(n=k=2\\) and
\\(n=k=l=2\\) respectively. Let's explore first case. We have 4 nodes and each
node has 2 edges. In the next step ,we will inevitable get 3 nodes with 2
connections each which will be a fully connected graph. In fact, subgraph in
which all of the nodes have even number of edges will inevitably form a fully
connected subgraph with at least 3 nodes.

We can show that every graph (or subgraph) with all of the nodes that have even
number of connections will eventually produce at least one fully connected
subgraph in which each node has 2 or more edges (even number of edges). First,
notice that in each step some node in the graph loses 2 edges. Which means that
after each step each node in the graph will have even nubmer of edges. This
means that we cannot get nodes with 1 edge (or any odd number of edge) since we
always guarantee to have even number of edges. In addition, we cannot get all
nodes with 0 edges in the graph, since in each step we lose 2 edges and add 1
and there is no way to completely get rid of all of the edges. This shows that
we will not be able to reach desirable goal in case graph (or subgraph) has all
nodes with even number of edges. For this reason, we will won't to avoid having
subgraph with even number of edges as much as we want to avoid having fully
connected subgraphs.

We can avoid formation of the graphs that have only nodes with even number of
edges in exactly the same way that we did it for the graphs that we've
considered before (those that were one step from forming a fully connected
subgraph). Basically, we need to consider cases after which we will get in the
next step a decoupled subgraph with all of the nodes that have only even number
of edges and prevent it from happening in exactly the same way as in the
previously considered cases.

In addition, this strategy resolves issue that we had with subgraphs that have 4
nodes and each node has 2 edges, since they will never occur.

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



