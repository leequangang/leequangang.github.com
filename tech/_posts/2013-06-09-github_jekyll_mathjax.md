---
layout: post
title: "Github+jekyll+Mathjax搭建Blog"
tags: [jekyll, github, markdown]
---


##Github+jekyll+Mathjax搭建Blog

- This will become a table of contents (this text will be scraped).
{:toc}

前记：最近用wordpress搭建了个Blog想写点笔记之类的东西（原因是看到那些大牛们的个人博客都太好了，想学习一下^_^）,于是申请了个空间玩了几天wordpress，挑模版，找公式插件（感谢[Mathjax](http://mathjax.com)）,等折腾完了要动手写的时候突然想到数据库+不稳定的空间+繁杂的公式要是哪天没备份不就掉坑里了- -!所以博客也迟迟没有添加内容...


直到有一天上午看到了Markdown，然后是jekyll (虽说至今都没明白这是个啥，只知道他用ruby写的，可以建静态bolg)，然后是Github，接下来就是整整2天的折腾了。第一天Github,第二天jekyll+Github，也遇到了很多坑，在此记一下备用。

###搭建Blog

####1.在Github中建立名为 username.github.com的仓库
建好后去setting自动生成主页；网上找一个模版clone到本地然后做一下修改（说的简单，做起来也不这么轻松了）...
多说一句Github的自建项目主页模版很漂亮！

[一堆网站模版](https://github.com/mojombo/jekyll/wiki/Sites)(我用的是第5个überduper感觉既简洁有有色彩)

####2.win7下安装本地jekyll环境
- 安装Ruby：[rubyinstaller-1.9.2](http://rubyinstaller.org/downloads/)
- 安装Ruby [DevKit](http://cloud.github.com/downloads/oneclick/rubyinstaller/DevKit-tdm-32-4.5.2-20111229-1559-sfx.exe)：解压到本地，如D:

进入cmd，执行

    D:\devkit>ruby dk.rb init
    D:\devkit>ruby dk.rb install

删除默认的下载源，改成淘宝的镜像

    D:\devkit>gem sources --remove https://rubygems.org/
    D:\devkit>gem sources -a http://ruby.taobao.org/

安装jekyll、kramdown

    gem install jekyll
    gem install kramdown

本地测试(jekyll新版本的命令有更新)

    jekyll serve

然后就可以在浏览器中输入`localhost:4000`来查看网站

jekyll中文编码问题 'C:\Ruby192\lib\ruby\gems\1.9.1\gems\jekyll-1.0.3\lib\jekyll\convertible.rb' 第31行

    self.content = File.read(File.join(base, name))

替换为

    self.content = File.read(File.join(base, name), :encoding => "utf-8")

####3.Github for win上传
上传到Github

####4.mathjax的兼容问题
在_layouts/default.html中`<head>`标签添加

    <script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

kramdown支持公式，要在_config.yml中添加'markdown:  kramdown'
行内公式用`$$行内公式$$`,
行间公式要另起空行结束也要空行


    $$
    行间式
    $$

[开启编号功能](3)
In equation ($$\ref{sample}$$), we find the value of an
interesting integral:

$$
\begin{equation}
  \int_0^\infty \frac{x^3}{e^x-1}\,dx = \frac{\pi^4}{15}
  \label{sample}
\end{equation}
$$

####5.添加Disqus评论模块
国外第三方评论系统

###注意 

- .md文件名不能是中文 否则会出错
- 文件名的单词间不能有空格，用+代替(+的话存在url转义问题，有时候不注意会出错，还是用_吧！)
- 命名规则为`年-月-日-英文名.md`，例如`2013-06-09-github+jekyll+mathjax.md`
- 可以利用`{:toc}`来自动生成目录

		- 这里是目录(编译后这句话会被忽略)
		{:toc}

- .md开头要有一段代码来引入格式 ( *列表中嵌套代码开头要用两个`\tab`，并且开头要有空行* )

		---
		layout: post
		title: "Github+jekyll+Mathjax搭建Blog"
		---
- 可以用三个以上的`~~~`来定义代码块开始与结束如

		~~~
		def what?
		  42
		end
		~~~

~~~~
#include "trim_mean.h"
#include <iostream>
int main()
{
  int x[8]={1, 2, 3, 4, 5, 6, 7, 8};
  double tm = trimmean<int>(8, x, 0.5);
  std::cout <<"The mean of the interior of the x array is: "<<tm<<std::endl;
  return 0;
}
~~~~


- 插入图片：在`_config.yml`中定义变量`img_url: http://leequangang.github.com/images` 然后在.md文档中插入
![logo图片]（｛｛site.img_ url }}/logo.png)即可现实图片

- 脚注[^id]定义是：`[^1]:`，引用语法是`[^1]`

		脚注[^id]
		[^id]: 这是脚注

- 在引用中`>`使用公式`$$公式$$`不显示，不知为何？
- This is a [reference style link][linkid] to a page. 

		This is a [reference style link][linkid] to a page.
		[linkid]: http://www.google.com/ "可选提示文本"`
- 参考文献的引用就可以通过双链接来实现[[0]][f0]

		通过双链接来实现[[0]][f0]
		[0] [google][f0]

		[f0]: http://google.com "显示google主页"
		*注意上面两个之间要有空行*

表头      | 列1        | 列 2               |  列3        | 列4
----------|------------|:-------------------|------------:|:--------------:
行1       | *强调*     | 公式语法 $$\frac{x}{y^2}$$ | 链接语法 [Google](http://www.google.com.cn)  | 内容中间对齐
行2       | _强调_     | 内容左对齐         | 内容右对齐  | 内容中间对齐
行3       | **强调**   | 内容左对齐长       | 内容右对齐  | 内容中间对齐
行4       | __强调__   | 内容左对齐         | 内容右对齐  | 内容中间对齐


|---
| Default aligned | Left aligned | Center aligned | Right aligned
|-|:-|:-:|-:
| First body part | Second cell | Third cell | fourth cell
| Second line |foo | **strong** | baz
| Third line |quux | baz | bar
|---
| Second body
| 2 line
|===
| Footer row

###参考
[0] [google][f0]

[f0]: http://google.com "显示google主页"

[1] [Jekyll使用MathJax来显示数学式](http://cyukang.com/2013/03/03/try-mathjax.html "显示公式")

[2] [怎样使用Markdown](http://www.ituring.com.cn/article/23)

[3] [MathJax让你爱上数学公式](http://zhiqiang.org/blog/it/mathjax-make-mathematics-beautiful.html)

[4] [显示公式](http://liuhongjiang.github.io/tech/blog/2012/11/21/math/)

[5] [kramdown Syntax](http://kramdown.rubyforge.org/syntax.html)

[linkid]: http://www.google.com/ "可选提示文本"
[^id]: 这是脚注