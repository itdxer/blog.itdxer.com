---
title: "Solutions for the IMO 2019 problems"
date: 2020-02-09
---
My solutions for the IMO 2019 problems. I'm an amature in mathematics which
means that these solutions might contain mistakes. Use them at your own risk

## Problem 1

![](http://blog.itdxer.com/images/imo-2019/imo-2019-problem-1.png)

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

**Replace f(a) by linear function**

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

**Finding c**

We can plug linear function with fixed k into the general formula

$$
f(2a) + 2f(b) = f(f(a+b)) \\
4a + c + 4b + 2c = f(2a + 2b + c) \\
4a + 4b + 3c = 4a + 4b + 3c
$$

this equality implies that relation will hold for any possible \\(c\\), but
because we know that function \\(f\\) always outputs integers, it means that
\\(c\\) has to be an integer.

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
2. \\((2^n-1) \mod 7 = 0\\) when n is divisible by 3
3. \\((2^n-1) \mod 5 = 0\\) when n is divisible by 4

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



