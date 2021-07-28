import aiofiles
import asyncio
import itertools
import time
import logging
import tracemalloc

from data import RESPONSES as responses

loop = asyncio.get_event_loop()

async def write_file(item, count):
    async with aiofiles.open('file.txt', 'a') as f:
        for i in range(count * 1000):
            await f.write(item)

if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    
    tracemalloc.start()
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())

    start = time.time()
    tasks = itertools.starmap(write_file, responses)
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()

    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())

    print("time: ", time.time() - start)
