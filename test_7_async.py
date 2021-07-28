import asyncio
import time
import aiofiles
from aiocsv import AsyncReader, AsyncDictReader, AsyncWriter, AsyncDictWriter

async def read_file():
    async with aiofiles.open("data.csv", "r", newline="") as f:
        async for row in AsyncReader(f):
            # print(row)
            pass
        f.close()

if __name__ == "__main__":
    start = time.time()

    loop = asyncio.get_event_loop()
    asyncio.run(read_file())
    loop.close()
    print("time: ", time.time() - start)
