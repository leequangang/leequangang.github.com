---
layout: post
title: "Kronecker Graphs"
---

## Kronecker Graphs ##

[1][Leskovec-2010-Kronecker Graphs An Approach to Modeling Networks](http://scholar.google.com.hk/scholar?q=Kronecker+Graphs+An+Approach+to+Modeling+Networks&btnG=&hl=zh-CN&as_sdt=0%2C5&as_vis=1)

一个好的真是网络生成模型有2点用处：  
1. 用于推断实、假设检验、模拟，当真网络很难获得或者不可能获得时（未来网络不可能获得）  
2. 强迫我们去思考真实网络的性质（这算是什么用处）

Kronecker graphs即能服从已发现的众多静态网络的性质，也遵从一些最近发现的网络时序演化性质

### Graph Patterns ###


- Degree distribution
- Small diameter
- Hop-plot
- Scree plot
- Network values
- Node triangle participation
- Densification power law
- Shrinking diameter

### Generative models ###


- Random graph model-ER
- BA
- 变种

Kronecker graph[[1]][1]
: Kronecker graph of order $$k$$ is defined by the adjacency matrix $$K_1^k$$, where $$K_1$$ is the Kronecker initiator adjacency matrix.

[1]: http://scholar.google.com.hk/scholar?q=Kronecker+Graphs+An+Approach+to+Modeling+Networks&btnG=&hl=zh-CN&as_sdt=0%2C5&as_vis=1