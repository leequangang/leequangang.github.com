---
layout: post
title: "tex与pdf之间搜索与反向搜索关联"
tags: [jekyll, github, markdown]
published: ture
---


##tex与pdf之间正反向搜索

- This will become a table of contents (this text will be scraped).
{:toc}

  正反向搜索意思是双击一段tex代码可以定位到对应到的pdf段落，同样双击一段pdf文本可以定位到相应的tex代码。学习了[“常用编辑器正反向搜索的配置”][r1]中的方法，挺复杂的，下面简单记一下自己的测试结果。默认已经将需要用到的命令写入环境变量。
  
###所需条件

1. 编译tex时要生成扩展名为synctex的索引文件

2. pdf阅读器支持读取该索引文件

既然如此我们就先搞定这两个条件。  

首先是生成索引文件：

- 用命令行编译：可以在pdflatex、latex等命令后加上参数`-synctex=-1` ，  
如`pdflatex -synctex=-1 my.tex`

- Ctex下编译：Ctex的winedt下设置`Options -> Executions Modes -> PDF Viewer`在`Use --synctex`处打勾，synctex的值改成1、-1或0试一下，我的本来是-1改成1后就能搜索了。1是把文件压缩了，不知道为何这样就起作用了。

(注意千万不要让clean.bat等自己写的批处理把生成的索引文件给删除了！)  

其次选择合适的pdf阅读器，此处选择SumatraPDF。

一般情况下安装完Ctex后用自带的SumatraPDF就能使用正反向搜索，如果失败就按上面说的修改一下synctex的值。pdf阅读器的选择余地不大，但是tex编辑器有很多种，想要pdf定位到tex就在pdf阅读器中设置，想tex定位到pdf就在编辑器中设置。

接下来主要讲一下notepad++与pdf间的正反向搜索。

###pdf-->tex
**pdf-->tex需要配置pdf阅读器**  

- notepad++:下载SumatraPDF，在"选项-设置-反向搜索命令行"中填入`notepad++.exe -n%l "%f"`,默认notepad++已经加入环境变量。打开具有同名synctex索引文件的pdf时会出现以上选项，否则没有，如果没有该选项就在高级选项中加入一行`InverseSearchCmdLine = notepad++.exe -n%l "%f"`  

- winedt编辑器就是`InverseSearchCmdLine = "C:\CTEX\WinEdt\WinEdt.exe" "[Open(|%f|);SelPar(%l,8);]"`  

使用时双击pdf的文字即可，基本上是按行定位的，如果有一段话没有换行则定位到该段落，如果每句话在tex中占一行则可定位到该行。

###tex-->pdf
这个感觉用处不大，有兴趣的可以试试[“常用编辑器正反向搜索的配置”][r1]中的方法


###References
[1] [常用编辑器正反向搜索的配置][r1]

[r1]: http://bbs.ctex.org/forum.php?mod=viewthread&tid=49386&extra=&page=1

[^id]: 这是脚注