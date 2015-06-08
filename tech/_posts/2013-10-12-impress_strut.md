---
layout: post
title: "Strut: 利用impress.js制作Web版PPT"
tags: [impress, strut, html5, js]
published: ture
---


## Strut: 利用impress.js制作Web版PPT

- This will become a table of contents (this text will be scraped).
{:toc}

### impress.js
[impress的Github主页](https://github.com/bartaz/impress.js/)   
impress.js可制作Web版的PPT，效果很炫，跟prezi类似。，这有两个Demo[中文](http://eyehere.net/wp-content/uploads/2012/11/impress_cn.html#/bored)跟[英文](http://bartaz.github.io/impress.js/#/bored)。但是impress制作起来很费劲，全是代码形式，这有一个[中文教程](http://eyehere.net/2012/impress-js-chinese-course-tutorial/)，可喜的是有人制作了很多种工具来方便使用。我个人感觉Strut是比较好用的一个。

### Strut
[Strut的Github主页](https://github.com/tantaman/Strut)  
这有一个[网页版](http://strut.io/)的可用，导出时就选择做好的PPT然后ctrl+s保存。也可以下载一个编译好的[本地版](http://code.google.com/p/strut/downloads/list)在本地浏览器打开直接使用。不过本地版的功能好像不如网页版的多，可能现阶段版本间没有同步。

Strut可以使用css，可用markdown来编写，应该也可以用mathjax，可以后续开发一下。

不过可以从Github上下载自己编译使用（编译出来的就跟上面的本地版是一样的）。Linux下的编译方法[[1]][r1]在安装插件时出现很多错误没搞定，我**在windows上编译成功了**。

1. 首先安装[node.js](http://nodejs.org/)(node.js是个很强大的工具，但我用不到...)，版本要在v0.8版之后不然grunt安装不成功。

2. 安装grunt，`npm install grunt`。

3. 然后去Github上下载Strut，（这里遇到一个大坑，折腾到晚上2点才搞明白，原来Github上的Download下来的zip里面的文件是不完整的，有好些文件都缺失，太坑了，通过Github的桌面版Clone下来才是完整的，莫非我中奖了？）

4. 进入Strut目录安装所需插件`npm install`

5. 最后就是使用方法了，有两种：

    - 运行`grunt server`：运行后直接可以在浏览器上使用localhost:9000访问

    - 编译`grunt build`：编译完会发现多出了一个dist的目录，这个目录就是已编译的网页了，和下载的本地版本一样的，直接在浏览器中打开使用。(Chorme可以打开，firefox好像不行)

ps:后来换了个linux虚拟机，安装成功了。

1. 编译安装node.js, `wget http://nodejs.org/dist/v0.10.20/node-v0.10.20.tar.gz`，解压后编译安装，`./configure、make、make install`

2. 安装插件`npm install -g grunt-cli`

3. 下载strut `git clone https://github.com/tantaman/Strut.git`

4. 第4、5步跟上面一样。

### With Mathjax
后来测试了一下，把Strut里面的`\test\index.html`、`\app\index.html`、\app\preview_export 里面的`bespoke.html`、`handouts.html`、`impress.html`这五个html文件的`</head>`的前面里添上 Mathjax 的代码

~~~~
<!-- This is for Mathjax -->
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

<!-- Mathjax autoNumber-->
<script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        TeX: {equationNumbers: {autoNumber: ["AMS"], useLabelIds: true}},
        "HTML-CSS": {linebreaks: {automatic: true}},
        SVG: {linebreaks: {automatic: true}}
    });
</script>

<!-- Mathjax inlineMath-->
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    extensions: ["tex2jax.js"],
    jax: ["input/TeX", "output/HTML-CSS"],
    tex2jax: {
    inlineMath: [ ['$','$'], ["\\(","\\)"] ],
    displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
    processEscapes: true
  },
  "HTML-CSS": { availableFonts: ["TeX"] }
});
</script>
~~~~

不过结果生成的PPT里面的公式右键弹出的窗口失效了，不知如何修改了。另外这样的PPT需要联网使用Mathjax，当然也可以把上面的Mathjax地址换成自己的本地版就可以在本地使用了。

[这是我自己编译的一个本地版 with Mathjax](http://pan.baidu.com/s/1km05o)

### References
[1] [安装并使用Strut放映impress.js生成的ppt][r1]

[r1]:http://my.oschina.net/u/943306/blog/156797 "安装并使用Strut放映impress.js生成的ppt"
