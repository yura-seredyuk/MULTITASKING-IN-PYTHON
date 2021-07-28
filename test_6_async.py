import asyncio
import time
import aiofiles
import aiohttp
import tracemalloc


async def write_genre(file_name):
    async with aiohttp.ClientSession() as session:
        async with session.get(
                "https://binaryjazz.us/wp-json/genrenator/v1/genre/"
            ) as response:
            genre = await response.json()

    async with aiofiles.open(file_name, "a") as new_file:
        # print(f'Written "{genre}" to a file "{file_name}"...')
        await new_file.write(f'{genre}\n')

async def main(count):
    tasks = [asyncio.create_task(write_genre('generate.txt')) for i in range(1,count)]
    await asyncio.gather(*tasks)
count = 100
tracemalloc.start()
print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
start = time.time()
asyncio.run(main(count))
print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
print("time: ", time.time() - start)
