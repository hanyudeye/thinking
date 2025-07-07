import asyncio
# 根据上下文自动判断同步/异步
# 参考文章
# https://blog.est.im/2025/stdout-04
def sleep1():
    print("同步调用")
    asyncio.run(asyncio.sleep(1))

async def sleep2():
    print("异步调用")
    await asyncio.sleep(1)

# 同步调用
sleep1()

# 异步调用
asyncio.run(sleep2())