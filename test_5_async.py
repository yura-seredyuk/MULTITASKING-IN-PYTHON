import aiofiles
import asyncio
import time
import tracemalloc


loop = asyncio.get_event_loop()

async def write_file(i):      
    async with aiofiles.open(f'../../test_files/file_{i}.txt', 'w') as f:
        await f.write('async')
        f.close()

    async with aiofiles.open(f'../../test_files/file_{i}.txt', 'r') as f:
        _ = await f.read()
        f.close()

async def main():
    tasks = [asyncio.create_task(write_file(i)) for i in range(10000)]
    await asyncio.gather(*tasks)
    

if __name__ == '__main__':
    tracemalloc.start()
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())

    start = time.time()
    asyncio.run(main())
    loop.close()


    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())

    print("time: ", time.time() - start)
