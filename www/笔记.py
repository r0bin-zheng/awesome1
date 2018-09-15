#笔记
#
##20180906
#函数处理函数的作用：
#1 url处理
#将url即用户在浏览器输入的网址映射为对应的函数，
#比如'/'为主页，对应的函数为index()，'/like'对应收藏页，对应的函数为like()
#
#2 get与post
#有时用户的请求不一定是请求网页，还可能是提交表单，这时候就需要函数会识别get与post，
#当函数识别到位post时，要会对表单的字段做出正确的处理
#
#3 多个url处理函数的管理
#当url处理函数多起来后，可以单独设置一个py文件存放url函数，
#并定义一个可以注册一个文件中所有url处理函数的函数add_routes；
#更多时：可以按功能将url处理函数分装在不同文件
#-+- controllers/
#|  |
#|  +- login.js <-- 处理login相关URL
#|  |
#|  +- users.js <-- 处理用户管理相关URL
#|
#
##20180907
#“Day12：编写日志列表页”代码的逻辑
#->handlers.py（跳转到日志列表界面）
#	@get('/manage/blogs')
#	def manage_blogs(*, page='1'):
#    	return {
#        	'__template__': 'manage_blogs.html', #载入manage_blogs.html
#        	'page_index': get_page_index(page)} 
#->manage_blogs.html（viewmodel，需要载入/api/blogs）
#->handlers.py->api_blogs （controler，返回博客列表和Page类，需要引用class Page）
#->apis.py->classPage