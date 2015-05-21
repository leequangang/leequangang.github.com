---
layout: post
title: "Dirichlet-multinomial distribution (Polya Disribution)"
---


## Dirichlet-multinomial distribution (Polya Disribution)

- This will become a table of contents (this text will be scraped).
{:toc}

前记：这部分内容是最近看 LDA 中的各种文献所思所想，记录下来备忘，欢迎大家点评。其实这个博客也是受许多学者的科技博客的影响才建立的，他们的读书笔记、学习心得等给我很大的帮助，这种分享知识的精神也是我很赞赏的。主体平台搭建用了整2天的时间，希望能够维持下去。

### 一些基本概念[^1]

个人理解 LDA 中的前半部分 $$\alpha\longrightarrow\theta\longrightarrow z$$ 就是波利亚分布。即先从 Diri 中得到各 topic 的分布概率，然后依据该概率下的 Mult 分布采样得到一串 topic 序列（再然后就是从该 topic 序列中采样得到每个word）。

#### Probability mass function

**pmf** is a function that gives the probability that a discrete random variable is exactly equal to some value.

- 通常 pmf 作为离散概率分布的定义
- pmf 不同于 pdf，除了离散与连续的区别外，pdf 的值并不是概率，而是对某个区间的积分来推出该区间的概率。

#### 伯努利分布和二项分布

##### Bernoulli distribution

伯努利分布只有一个参数 $$P=\{p,1-p\}$$，采样的结果是 0 或 1。

- The Bernoulli distribution is simply $$Binomial(1,P)$$
- The categorical distribution is the generalization of the Bernoulli distribution for variables with any constant number of discrete values.
- The Beta distribution is the conjugate prior of the Bernoulli distribution.

##### Binomial Distribution

二项分布有两个参数分别是实验次数 $$N$$ 与概率 $$P=\{p,1-p\}$$，其采样结果 $$Y=\{k, N-k\}$$ 即实验中 0 的个数与 1 的个数。二项分布即重复 N 次的伯努利试验 (Bernoulli trial)，其概率密度函数为

$$
\begin{equation*}
  p(Y|N,P)=\binom{N}{k}p^k(1-p)^{N-k}
\end{equation*}
$$

其中 $$\binom{N}{k}=\frac{N!}{k!(N-k)!}$$ 称为二项式系数。

实际上，当 N=1 时，二项分布就是伯努利分布。

#### Categorical distribution

**分类分布是伯努利分布的推广**  
分类分布只有一个参数 $$P$$，简单理解为一个骰子有 K 个面，每个面的概率是 $$P=\{p_k\}$$, $$k\in [1,K]$$, $$\sum_{k=1}^K p_k=1$$. 扔这个骰子会产生一个输出 $$x$$（输出的就是类别标签，此处是 $$[1,K]$$ 内的值），则 $$x\sim Cat(P)$$，发生概率就是

$$
\begin{equation}
  p(x|P)=p_x
 \label{cat}
\end{equation}
$$

- Dirichlet distribution is the conjugate prior of the Categorical distribution (and also the Multinomial distribution).

#### Multinomial distribution

**多项式分布是二项分布的推广**  
多项式分布有两个参数分别是 $$N$$ 与 $$P$$，同样还是上面的骰子，扔这个骰子 N 次就可以得到一个序列$$X=\{2,3,K,...,6\}$$，不考虑序列 $$X$$ 产生的顺序，只考察扔 N 次会出现几个 1，几个 2，几个 K...或者说只考虑投 N 次骰子得到 $$Y=\{n_1,n_2,...,n_K\}$$, $$\sum_{k=1}^K n_k=N$$ 的概率, 这就是 $$Y\sim Mult(N,P)$$，则

$$
\begin{equation*}
  p(Y|N,P)=\frac{N!}{\prod_{k=1}^K n_k!}\prod_{k=1}^K(p_k)^{n_k}
\end{equation*}
$$

其中 $$n_k$$ 指序列 $$X$$ 中 k 面的个数，$$\sum_{k=1}^K n_k=N$$.  
$$\frac{N!}{\prod_{k=1}^K n_k!}$$ 称为多项式系数，可以参考多项式定理（Multinomial theorem）。

**多项式定理**: $$n$$ 是一个正整数，$$(x_{1}+x_{2}+\ldots+x_{k})^n=\sum{\frac{n!}{n_1!n_2!\cdots n_k!}x_1^{n_1}\ldots x_k^{n_k}}$$, 其中 $$n_1+\ldots n_k=n,n_i\geq0,1\leq i\leq k$$。


实际上，当 n=1 时，多项式分布就是分类分布。此时多项式分布的输出为一个 N 维向量 $$(0,0,1,0...0)$$ 仅有一个是 1，跟 Categorical 分布的输出 x 是等价的（即1的标志位做分类标签），公式 ($$\ref{cat}$$) 就相应地变成

$$
\begin{equation*}
  p(x|P)=\prod_{k=1}^K(p_k)^{\delta_k}
\end{equation*}
$$

where $$\delta_k$$ evaluates to 1 if $$x=k$$, 0 otherwise.

N 次独立的分类分布 $$Cat(P)$$ 采样与一次多项式分布 $$Mult(N,P)$$ 的采样结果是不同的，表现在系数上的不同。我们假设一个 6 面骰子投掷 N 次，其中 $$n_k$$ 指序列 $$X$$ 中 k 面的个数，$$\sum_{k=1}^K n_k=N$$.

- $$Cat(P)$$ 得到的序列为 $$X=\{2,3,K,...,6\}$$ 或者是 N 个这样的 N 维向量 $$(0,0,...,1,...)$$，其概率：

$$
\begin{equation*}
  p(X|P)=\prod_{k=1}^K(p_k)^{n_k}
\end{equation*}
$$

- 多项式分布 $$Mult(N,P)$$ 得到的序列为 $$Y=\{n_1,n_2,...,n_K\}$$，其概率：

$$
\begin{equation*}
  p(Y|N,P)=\color{#FBA919}{\frac{N!}{\prod_{k=1}^K n_k!}}\prod_{k=1}^K(p_k)^{n_k}
\end{equation*}
$$

其实可以认为 N 次 Categorical 分布采样的得到的是一个多项式分布采样的子集（好像说的也不太准确）

- N=1的多项式分布即 Categorical 分布

#### Dirichlet distribution
未完待续

### Polya Distrubution

#### 模型

#### 计算



###Multinomial & Categorical

> **Note that[[1][r1]]**, in some fields, such as natural language processing, the categorical and multinomial distributions are conflated, and it is common to speak of a "multinomial distribution" when a categorical distribution is actually meant[^2]. This imprecise usage stems from the fact that it is sometimes convenient to express the outcome of a categorical distribution as a "1-of-K" vector (a vector with one element containing a 1 and all other elements containing a 0) rather than as an integer in the range 1 to K; in this form, a categorical distribution is equivalent to a multinomial distribution for a single observation.  
However, conflating the categorical and multinomial distributions can lead to problems. For example, in a Dirichlet-multinomial distribution, which arises commonly in natural language processing models (although not usually with this name) as a result of collapsed Gibbs sampling where Dirichlet distributions are collapsed out of a Hierarchical Bayesian model, it is very important to distinguish categorical from multinomial. The joint distribution of the same variables with the same Dirichlet-multinomial distribution has two different forms depending on whether it is characterized as a distribution whose domain is over individual categorical nodes or over multinomial-style counts of nodes in each particular category (similar to the distinction between a set of Bernoulli-distributed nodes and a single binomial-distributed node). Both forms have very similar-looking probability mass functions (PMF's), which both make reference to multinomial-style counts of nodes in a category. However, the multinomial-style PMF has an extra factor, a multinomial coefficient, that is not present in the categorical-style PMF. Confusing the two can easily lead to incorrect results.

自然语言处理一个基本假设是 "Bag-of-words"，文章的词之间是可交换的。只要词与词频都相同，则认为两篇文章相同（当然现实中是不正确的，如：“我知道你不知道”，“我不知道你知道”，完全是不同的意思）



###参考

[1] [Categorical distribution][r1]

[r1]: http://en.wikipedia.org/wiki/Categorical_distribution#cite_note-minka-1 "Categorical distribution"


[2] [Dirichlet分布及其属性][r2]

[r2]: http://www.cnblogs.com/houkai/archive/2013/05/27/3102465.html "Dirichlet分布及其属性"



[^1]: 大部分概念性东西直接贴自维基百科，可以去搜索关键词，就不一一列出了，在此感谢[Wikipedia](http://en.wikipedia.org/wiki/Main_Page) 提供的知识共享的平台，也感谢那些编辑wiki词条的分享者们

[^2]: 注意[[2][r2]]：在自然语言处理领域，categorical 和 multinomial 分布是混为一谈的，当提到 multinomial 分布时实质意味着是 categorical 分布；当然，categorical 也可以视为 multinomial 的特殊情况。
