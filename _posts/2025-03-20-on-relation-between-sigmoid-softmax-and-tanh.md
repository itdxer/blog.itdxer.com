---
title: "On the relationship between sigmoid, softmax and tanh"
date: 2025-03-20
layout: post

description: "The article shows relations between the sigmoid, softmax, and tanh functions. Specifically, it shows how one of these functions can be used to represent another straightforwardly."

tags: ['deep learning', 'machine learning', 'llm', 'neural networks']

comments: true
share: true
---

If you have even a passing interest in deep learning, chances are you've encountered at least one of these functions: sigmoid, softmax, and tanh. Over the past few decades, they have been integral to numerous research efforts and will likely continue to be so for many years to come. What's truly remarkable is how few people know about the relationship between these functions, and even top researchers can overlook it in their analyses, as we will see later.

In this article, we will use the following definitions for sigmoid, softmax, and tanh functions.

<div class="side-scroll">
$$
\begin{align}
    \text{sigmoid}(x) &= \frac{1}{1 + e^{-x}} \\
    \text{softmax}_i([x_1, x_2, ..., x_n]) &= \frac{e^{x_i}}{\sum_{j=1}^n e^{x_j}} \\
    \text{tanh}(x) &= \frac{e^x-e^{-x}}{e^x + e^{-x}}
\end{align}
$$
</div>

### Relationship between sigmoid and softmax

It's easy to show that sigmoid can be viewed as softmax

<div class="side-scroll">
$$
\begin{align}
\text{sigmoid}(x) &= \frac{1}{1 + e^{-x}} \\
                  &= \frac{e^x}{e^x}\frac{1}{1 + e^{-x}} \\
                  &= \frac{e^x}{e^x + e^{0}} \\
                  &= \text{softmax}_1([x, 0])
\end{align}
$$
</div>

In the same way, we can show that adding a constant to every input of the softmax doesn’t have any impact on its output. More formally, for some constant \\(c\\) we have

<div class="side-scroll">
$$
\text{softmax}_i([x_1 + c, x_2 + c, ..., x_n + c]) = \text{softmax}_i([x_1, x_2, ..., x_n])
$$
</div>

<em style="color: #ccc;">Side note: FlashAttention cleverly leverages this property to combine softmax with all other attention operations into a single kernel. This results in a significant speedup for attention computation on GPUs. [1] [2]</em>

Using this property of the softmax function we can also show that the opposite relation between softmax and sigmoid holds

<div class="side-scroll">
$$
\begin{align}
\text{softmax}_1([x_1, x_2]) &= \text{softmax}_1([x_1 - x_2, 0]) \\
                             &= \text{sigmoid}(x_1 - x_2)
\end{align}
$$
</div>

The main difference here is that with softmax we make a dynamically adjustable threshold for the positive class whereas with sigmoid it's implicitly set to 0.

My personal opinion is that it's better to use sigmoid instead of softmax whenever we train a model for binary classification since we get rid of some of the parameters without losing any predictive power. In addition, it's quite often better in ML to get rid of the symmetries in the proposed solution and reduce the number of local minimums. Although, perhaps in practice that difference will be quite negligible.

### Relationship between tanh and sigmoid

Just like before, let's start by showing the relation between two functions

<div class="side-scroll">
$$
\begin{align}
\text{tanh}(x) &= \frac{e^x-e^{-x}}{e^x + e^{-x}} \\
               &= \frac{1-e^{-2x}}{1 + e^{-2x}} \\
               &= \frac{2 - (1 + e^{-2x})}{1 + e^{-2x}} \\
               &= \frac{2}{1 + e^{-2x}} - 1 \\
               &= 2\,\text{sigmoid}(2x) - 1
\end{align}
$$
</div>

The interesting implication is that if we deal with a simple multi-layer perceptron (MLP) then any difference in performance should be only due to the parameter initialization. Surprisingly, as of today, the scikit-learn library [3] allows one to set tanh and sigmoid as an activation function even though they model exactly the same family of functions since we can simply scale weights and adjust biases to obtain identical outputs.

One particularly amusing example comes from an interesting paper which was released very recently titled "Transformers without Normalization" [4]. The paper explores the possibility of replacing the RMSNorm operation in Transformer blocks (commonly used with LLMs) with a simpler operation that doesn't require us to compute aggregate statistics per each feature vector. They managed to show that they can achieve very similar performance and reduce training and inference time which is a great result. The new transformation is called Dynamic Tanh (DyT) and expressed as the following family of functions, for which parameters \\(\alpha\\), \\(\beta\\), and \\(\gamma\\) are learned during the training.

$$
\begin{align}
\gamma \, \text{tanh}(\alpha x) + \beta
\end{align}
$$

You can notice similarities between the DyT operation and transformations, which can be used to transform tanh to sigmoid

<div class="side-scroll">
$$
\begin{align}
\gamma \, \text{tanh}(\alpha x) + \beta &= 2\gamma \, \text{sigmoid}(2\alpha x) + \beta-\gamma \\
                                        &= \gamma' \, \text{sigmoid}(\alpha' x) + \beta'
\end{align}
$$
</div>

This relationship suggests that the performance of the DyT should be independent of whether we use sigmoid or tanh. Yet, they yielded quite different performance results.

![png]({{ BASE_PATH }}/images/tahn-sigmoid-softmax/dyt-tanh-vs-sigmoid.png)

Assuming that these differences are statistically significant, this potentially suggests that the experiment is flawed due to its sensetivity to the initialization parameters. 

### References

<div>[1] Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, Christopher Ré. FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness. https://arxiv.org/abs/2205.14135</div>
<div>[2] Maxim Milakov and Natalia Gimelshein. Online normalizer calculation for softmax. https://arxiv.org/abs/1805.02867</div>
<div>[3] <a href="https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html">The scikit-learn's MLPClassifier classifier.</a></div>
<div>[4] Jiachen Zhu, Xinlei Chen, Kaiming He, Yann LeCun, Zhuang Liu. Transformers without Normalization. https://arxiv.org/abs/2503.10622</div>