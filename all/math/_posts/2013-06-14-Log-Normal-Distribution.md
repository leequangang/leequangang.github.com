---
layout: post
title: "Log Normal Distribution"
---


##Log Normal Distribution

In probability theory, a log-normal distribution is a continuous probability distribution of a random variable whose logarithm is normally distributed [[1]][r1].

- If $$X\sim\mathcal{N}(\mu,\delta^2)$$ is a normal distribution, then $$\exp(X)\sim Log-\mathcal{N}(\mu,\delta^2)$$.
- If $$X\sim Log-\mathcal{N}(\mu,\delta^2)$$ is distributed log-normally, then $$\ln(X)\sim\mathcal{N}(\mu,\delta^2)$$ is a normal random variable.

![lognpdf]({{ site.img_url }}/math/lognpdf.png)


相关的Matlab函数
lognfit、logncdf、lognpdf、lognrnd、
histfit(A,25,'lognormal')

###参考

[1] [Log-normal distribution][r1]

[r1]: http://en.wikipedia.org/wiki/Log-normal_distribution "wiki"

[2] [logn distribution-wolfram mathworld][r2]

[r2]: http://mathworld.wolfram.com/LogNormalDistribution.html "logn"