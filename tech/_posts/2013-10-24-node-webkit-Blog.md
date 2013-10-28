---
layout: post
title: "利用node-webkit将Blog做成本地app"
tags: [node-webkit, upx, Blog]
published: ture
---


##利用node-webkit将Blog做成本地app

- This will become a table of contents (this text will be scraped).
{:toc}

###Blog打包

目的是把Blog用node-webkit打包成一个本地exe文件，不用在浏览器上运行。
1. 将Github上的Blog配置文件本地化，本地版的配置文件与网页版非常不同，主要是各种相对路径的设置，留言插件的删除等,很麻烦
2. jekyll编译博客生成本地化后的_site文件夹
3. 将_site文件夹中的内容拷到node-webkit的test下，再添加个logo.png和配置文件，就可以用node-webkit来打包本地化应用
	1. 将\test下的文件打包成zip，然后重命名成.nw，拖进nw.exe即可运行，或者cmd下运行nw test.nw
	2. cmd下copy /b nw.exe+test.nw test.exe将nw.exe与test.nw打包成一个exe文件，双击可运行；同时可以连同dll文件和nw.pak一起作为桌面应用发布。
4. 另外最好使用[本地化的mathjax](http://pan.baidu.com/s/19WddI)，主要是删除了一些图片格式的符号，体积大减。Blog里面的外部链接在联网时仍可用，按Backspace键返回。
5. 另外可以用图标替换工具来替换exe的图标
------------------------------------------------
###UPX压缩exe文件
[UPX](http://upx.sourceforge.net/)可以压缩exe、dll等格式的文件而不影响其正常使用，可视为压缩加壳。下载upx.exe即可使用，只有几百KB。

~~~~
压缩	upx  a.exe -o b.exe
解壳	upx -d a.exe -o b.exe
显示upx信息    upx -v
压缩软件       upx  -9   xxx.exe

附上UPX 命令解释
-1 快速压缩     -9 较好压缩  
-d 解压缩      -l 列出压缩文件  
-t 测试压缩文件     -V 显示版本号  
-h 更多帮助     -L 显示软件授权  
-q 安静方式     -v 冗长  
-oFILE 写入输出到文件   -f 强制压缩可疑文件  
-k 保留备份文件
~~~~

###References
[1] [google][r1]

[r1]: http://google.com "显示google主页"
