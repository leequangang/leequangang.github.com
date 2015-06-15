#coding=utf-8  

"""
用mistune来解析md文件，自带目录，不需要设置[TOC]

python  md2html.py  XX.md   YY.md ....


输出：XX.html  YY.html ...

返回的html文件中用到自己定义的信息，如css，mathjax等详情见 html_head、html_footer部分

"""


import mistune
import sys

reload(sys)
sys.setdefaultencoding('utf-8')#解决字符串乱码问题

top_level = 1
header_info = []


html_head = """ 
<head>
<meta name="Leequangang" charset="utf-8">

<link href="http://maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet">
<link rel="stylesheet" type="text/css" href="http:leequangang.github.io/local/local_light.css">

<!-- This is for Mathjax -->

<script type="text/x-mathjax-config">
	MathJax.Hub.Config({
		tex2jax: {
			inlineMath: [ ['$','$'], ["$","$"] ],
			displayMath: [ ['$$','$$'], ["$$","$$"] ],
			processEscapes: true
			},
		TeX: {equationNumbers: {autoNumber: ["AMS"], useLabelIds: true}},
		"HTML-CSS": {linebreaks: {automatic: true}},
		SVG: {linebreaks: {automatic: true}}
	});
</script>

<script type="text/javascript"
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>


<title>LQG</title>
</head>

<body>

"""


html_footer = """ 

<div class="go-top" >
<i class="pos-btn" onclick="window.scrollTo('0', '0')"><i class="fa fa-angle-double-up"></i></i>
</div>

<div id="footer">

  <p> <i class="fa fa-envelope-o fa-1x"></i>:&nbsp leequangang@gmail.com &nbsp Published under<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh"> (CC) BY-NC-SA 3.0</a></p>

  <p>&copy; 2013 Lee quangang &nbsp <a href="http://leequangang.github.io"><i class="fa fa-github fa-1x"></i>
  </p>
</div>

</body>
""" 


class headerRenderer(mistune.Renderer):#更换mistune中header输出，添加id属性
    def header(self, text, level, raw=None):
		global top_level, header_info
		header_info.append([level, raw, text])
		top_level = level if level < top_level else top_level
		return '<h%d id="%s">%s</h%d>\n' % (level, raw, text, level)


def header_md():#输出md形式的header列表
	global top_level, header_info
	toc_md = '# Table of contents \n'
	for i in range(len(header_info)):
		toc_md += '%s- [%s](#%s)\n' %( (header_info[i][0]-top_level)*'    ', header_info[i][2], header_info[i][1])#按header等级的缩进量写成md列表

	top_level = 1 #重新设定
	header_info = []
	return toc_md


def md2html(context_md):
	renderer = headerRenderer()
	md = mistune.Markdown(renderer=renderer)
	context_html = md.render(context_md) #解析md文件正文，修改mistune中header输出，添加id

	toc_html = mistune.markdown(header_md())#解析md形式的目录列表

	return html_head + toc_html + context_html + html_footer


if __name__=='__main__': 

	for i in range(1, len(sys.argv)):

		f = open( sys.argv[i], 'r')#打开文件
		context_md = f.read()

		list = sys.argv[i].strip().split('.')
		filename = list[0]#文件名
		outfile = open(filename+'.html', 'w')#创建html
		outfile.write(md2html(context_md))#解析输出
		f.close( )
		outfile.close( )

		print sys.argv[i],"OK"