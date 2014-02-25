---
layout: post
title: "node-webkit:开发桌面应用"
tags: [node.js, html, JavaScript]
published: ture
---

##node-webkit:开发桌面应用

- This will become a table of contents (this text will be scraped).
{:toc}

###node-webkit
node-webkit是基于node.js和chromium的应用程序实时运行环境，可采用前端技术（HTML，CSS，JavaScript）开发桌面应用软件的跨平台解决方案，见[Github页面](https://github.com/rogerwang/node-webkit)。就是说可以用html+css编写应用界面，用javascript做些执行处理并结合node.js的本地化操作，最终打包成为一个本地的应用。（其实就是编写一个web应用在一个本地版的chromium浏览器上运行）

官方提供的[一些成品](https://github.com/rogerwang/node-webkit/wiki/List-of-apps-and-companies-using-node-webkit)，其中Haroopad就是一个markdown的写作工具，跟markdownpad2一样

####使用方法
1. 下载node-webkit的zip文件，解压，主要有4个dll文件，一个nw.exe程序，一个nw.pak，还有一个nwsnapshot.exe（不知有何作用）；在里面新建一个项目文件夹，如\test;
2. 最简单的nw应用，只需要有index.html和package.json文件，前者是app的入口也是界面，后者是配置文件。其中，main和name是必选字段，更多配置字段，可参考[官方地址](https://github.com/rogerwang/node-webkit/wiki/Manifest-Format);
3. 运行（windows下）：  
a、在cmd下运行`nw test`  
b、将\test下的文件打包成zip，然后重命名成.nw，拖进nw.exe即可运行，或者cmd下运行`nw test.nw`  
**c、cmd下`copy /b nw.exe+test.nw test.exe`将nw.exe与test.nw打包成一个exe文件，双击可运行；同时可以连同dll文件和nw.pak一起作为桌面应用发布。其他平台下具体见[官网方法](https://github.com/rogerwang/node-webkit/wiki/How-to-package-and-distribute-your-apps) ** 。另外最后一段提到，可用Enigma Virtual Box将exe与dll还有nw.pak文件一起打包，生成一个新的exe文件，就可独立运行。另外可以用UPX.exe来压缩生成的exe文件以及dll文件来减少文件占用的空间。
4. 关于Logo，窗体设置等简单见如下配置文件

~~~~
{
    "main": "index.html",                              /* APP的主入口，文件名任意；必选 */
    "name": "nw-demo",                                /* APP的名称，必须具备唯一性，且符合正常变量命名；必选 */
    "description": "demo app of node-webkit",         /* APP的简单描述 */
    "version": "0.1.0",                               /* APP的版本号 */
    "keywords": [ "demo", "node-webkit" ],            /* APP的关键字，搜索APP时用到 */
    "window": {                                       /* APP的窗口属性 */
        "icon": "logo.png",                           /* APP图标（windows下，状态栏上可见） */
        "toolbar": false,                              /* 是否显示工具栏 */
        "width": 800,                                 /* 窗口初始化大小 */
        "height": 500,
        "frame": true                                 /* 是否显示外窗体，如最大化、最小化、关闭按钮 */
    },
    "user-agent": "%name %ver %nwver %webkit_ver %osinfo" /* 可自定义APP的UA */
}
~~~~

一定记住，除了test.exe， 还需要附带一系列的插件。
在 windows 下，nw.pak以及icudt.dll是必须的。前者提供了重要的JavaScript库，后者提供了一些重要的网络库。带上 ffmpegsumo.dll 用来提供对 <video> 和 <audio> 标签的支持。libEGL.dll 以及 libGLESv2.dll 提供 WebGL 以及 GPU 加速的支持。


###heX
heX是有道做的一个跟node-webkit很类似的工具，用处是一样的，新版的有道词典号称是用它来做的，可以看以下，用起来也很方便。  
[hex主页](http://hex.youdao.com/)跟[一个相关介绍博客](http://techblog.youdao.com/?p=685)

###References
[1] [Node.js][r1]

[r1]: http://nodejs.org/ "node.js主页"

[2] [用node-webkit开发多平台的桌面客户端](http://www.baidufe.com/item/1fd388d6246c29c1368c.html)

[3] [heX：用HTML5和Node.JS开发桌面应用](http://techblog.youdao.com/?p=685)
