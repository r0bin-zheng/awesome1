#编写web框架测试

from aiohttp import web
import asyncio
from web_app.webframe import add_routes,add_static
from web_app.middleware_factories import init_jinja2,datetime_filter,logger_factory,response_factory
import logging; logging.basicConfig(level=logging.INFO)

#初始化协程
async def init(loop): 
	#创建应用
    app = web.Application(loop=loop,middlewares=[logger_factory,response_factory]) 
    #初始化Jinja2，这里值得注意是设置文件路径的path参数
    init_jinja2(app,filters=dict(datetime=datetime_filter),path = r"E:\learningpython\web_app\templates")
    #add_route函数：用来注册一个URL处理函数，主要起验证函数是否有包含URL的响应方法与路径信息，以及将函数变为协程
    #add_routes函数：通常add_route()注册会调用很多次，而为了框架使用者更加方便，可以编写了一个可以批量注册的函数，
    #预期效果是：只需向这个函数提供要批量注册函数的文件路径，新编写的函数就会筛选，注册文件内所有符合注册条件的函数
    add_routes(app,'web_app.webframe_test_handler')
    #添加静态文件夹的路径：MVC中常用的就是Controller与View。但是我们常常会需要访问静态资源，如html,js,css，image等
    add_static(app)
    #创建服务器监听9000端口
    srv = await loop.create_server(app.make_handler(),'127.0.0.1',9000)
    logging.info('Server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()