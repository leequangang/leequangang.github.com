---
layout: post
title: "OpenMP Tutorial"
tags: [openmp, 并行]
---


##OpenMP Tutorial

- This will become a table of contents (this text will be scraped).
{:toc}
注：最近写C++代码，跑了个实验用了8个多小时，其实实验内容就是简单的重复，后来突然想到我的i5-3210M也是双核四线程的，搞个单机版并行玩玩吧，然后就google了一下午，什么 OpenMP、MPI、TBB、CUDA(面向GPU)等等，鉴于我的菜鸟水平跟单机版并行的初衷最后选择了OpenMP。就跟着网页上例子只在`for`循环前面添加了一条语句`#pragma omp parallel for`居然就跑起来了，so easy！简单的测试下时间由5s变成了3s（幸福来得太突然了^_^）。。。

记录一下自己学习到的内容，备查。

###OpenMP基本用法
- openMP支持的编程语言包括C语言、C++和Fortran，支持OpenMP的编译器包括Sun Studio，Intel Compiler，Microsoft Visual Studio，GCC(这有个[list](r4))

- 选用的是MinGW编译器，编译时只需用`-fopenmp`开启OpenMP支持即可（不开启也能编译，不过是默认的串行模式），如`g++ -fopenmp hello.cpp -o hello`

- 如果只是在for循环前加一句`#pragma omp parallel for`则不需要添加额外的include头文件；如果要用到一些API像`omp_set_num_threads`则要在Cpp文件中添加`#include <omp.h>`  

- 一般而言，编译器默认实现的总线程数等于处理器的核心数，(也可通过`omp_set_num_threads(6)`设置线程数6个，或者`#pragma omp parallel num_threads(5)`来设置)



###实验

- 初始CPU占用状态  ![lognpdf]({{ site.img_url }}/math/lognpdf.png)

![cpu0]({{ site.img_url }}/tech/cpu0.png)

- 串行时CPU占用状态，可见单CPU占用率高

![cpu1]({{ site.img_url }}/tech/cpu1.png)

- 并行时CPU占用状态（默认线程个数4个），所有的CPU线程都利用起来了

![cpu0]({{ site.img_url }}/tech/cpu2.png)

- 并行8线程时CPU占用状态，应该是对应上图中CPU利用率又提升了点，又见缝插针地利用了空闲的CPU运算资源

![cpu0]({{ site.img_url }}/tech/cpu3-8threads.png)

- 我的台式机是i5-3210M 双核四线程，应该是两个物理内核，每个内核有两个逻辑线程。并行化后是有4个线程，但是时间提升仅1倍。有个小孩的作业是抄文章100遍，现在有俩小孩就是两个物理内核，每个小孩可以用左右手一块抄（不过眼睛要时不时在左右手间巡视检查错误，相当于调度）这就有了逻辑上四线程。在串行模式下是一个物理内核的资源运行一个逻辑线程。Intel超线程（Hyper-Threading）技术使处理器增加5%的裸晶面积，就可以换来15%~30%的效能提升，HT能使一个物理内核的资源运行两个逻辑线程。在开启HT下，OpenMP既使用了两个物理内核又在每个内核中开启了2个线程，但是提升主要体现在利用了第二个物理内核，而同一内核的多线程对提升来说效果次之（或者说线程过多反而增加了调度时间）

###参考

参考比较零散大多是google出来的，在此一并感谢

[1] [OpenMP][r1]

[r1]: http://openmp.org/wp/ "显示OpenMP主页"

[2] [通过GCC学习OpenMP框架][r2]

[r2]: http://www.ibm.com/developerworks/cn/aix/library/au-aix-openmp-framework/

[3] [openMP的一点使用经验][r3]

[r3]: http://www.cnblogs.com/yangyangcv/archive/2012/03/23/2413335.html

[r4]: http://openmp.org/wp/openmp-compilers/ "OpenMP Compilers"

[^id]: 这是脚注