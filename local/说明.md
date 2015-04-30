# markdown文档转本地html

## 安装 markdown 解析器
找个简单的Python下的markdown解析器 [mistune][1]安装:  
`$ pip install mistune`。

## 运行脚本
利用 md2html.py 来解析成 html 文档, html 文件名自动生成：  
`python md2html.py XX.md YY.md ZZ.md  ...`

注意 html 需要一个本地的 css 文件、mathjax 可以本地化（目前还需要网络）、有返回顶部的功能、用到 font-awesome 网络图标（也可本地化）

默认html中自动生成目录

作者 [Leequangang][2]     
2015 年 4月 28日 

[1]: https://github.com/lepture/mistune
[2]: leequangang@gmail.com