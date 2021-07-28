import aiofiles
import asyncio
import itertools
import time
import logging
import tracemalloc
from pathlib import Path


directory = '../../test_files'



async def write_file(i):
    async with aiofiles.open(f'../../test_files/file_{i}_write.txt', 'r') as f:
        data = await f.read()
        f.close()
        
    async with aiofiles.open(f'../../test_files/file_{i}_write.txt', 'w') as f:
        await f.write('async')
        f.close()

# async def main():
#     tasks = [asyncio.create_task(write_file(i)) for i in range(1,1001)]
#     await asyncio.gather(*tasks)
    
tasks = [write_file(i) for i in range(1,1001)]

if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    tracemalloc.start()
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())

    start = time.time()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    # asyncio.run(main())
    loop.close()


    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())

    print("time: ", time.time() - start)
