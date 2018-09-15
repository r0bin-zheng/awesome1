import orm,asyncio
from models import User, Blog, Comment

async def test(loop):

    await orm.create_pool(loop=loop,user='root', password='root', db='awesome')
    u = User(name='Summous', email='Summous@example.com', passwd='123456', image='about:blank')
    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()