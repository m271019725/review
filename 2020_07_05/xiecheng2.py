"""
协程技术
asyncio.py
"""
import asyncio


# 第一种
# @asyncio.coroutine
# def get_body(i):
#     print(f"start-{i}")
#     yield from asyncio.sleep(1)
#     print(f"end-{i}")


async def get_body(i):
    print(f"start-{i}")
    await asyncio.sleep(1)
    print(f"end-{i}")


loop = asyncio.get_event_loop()
tasks = [get_body(i) for i in range(5)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
