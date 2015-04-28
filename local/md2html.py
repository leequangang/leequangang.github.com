# -*- coding: utf-8 -*-  
import sys
import mistune

def md2html(file):

	list = file.strip().split('.')
	filename = list[0]

	inputfile = open(file)
	try:
		 context_md = inputfile.read( )
	finally:
		 inputfile.close( )

	context_html = mistune.markdown(context_md)


	html_head = """ 
	<head>
	<meta name="Leequangang" charset="utf-8">

	<link href="http://maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet">
	<link rel="stylesheet" type="text/css" href="https://leequangang.github.io/local/local.css">

	<!-- This is for Mathjax -->

	<script type="text/x-mathjax-config">
		MathJax.Hub.Config({
			TeX: {equationNumbers: {autoNumber: ["AMS"], useLabelIds: true}},
			"HTML-CSS": {linebreaks: {automatic: true}},
			SVG: {linebreaks: {automatic: true}}
		});
	</script>

	<script type="text/x-mathjax-config">
	  MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['$','$']]}});
	</script>

	<script type="text/javascript"
	  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
	</script>


	<title>LQG</title>
	</head>

	<body>

	"""


	html_footer = """ 

	<div class="go-top" style="display: block; right: 5%; position: fixed; bottom: 30px; ">
	<i class="pos-btn" onclick="window.scrollTo('0', '0')"><i class="fa fa-angle-double-up"></i></i>
	</div>

	<div id="footer">

	  <p> <i class="fa fa-envelope-o fa-1x"></i>:&nbsp leequangang@gmail.com &nbsp Published under<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh"> (CC) BY-NC-SA 3.0</a></p>

	  <p>&copy; 2013 Lee quangang &nbsp <a href="http://leequangang.github.io"><i class="fa fa-github fa-1x"></i>
	  </p>
	</div>

	</body>
	""" 


	outfile = open(filename+'.html', 'w')
	outfile.write(html_head)
	outfile.write(context_html)
	outfile.write(html_footer)
	outfile.close( )


if __name__=='__main__': 

	for i in range(1, len(sys.argv)):
		md2html(sys.argv[i])
		print sys.argv[i],"OK"


