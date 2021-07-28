import asyncio
import itertools
import time
import logging
import tracemalloc
from data import RESPONSES as responses

loop = asyncio.get_event_loop()



async def asinc_function(name, delay):
    logging.info("Response %s: starting", name)
    await asyncio.sleep(delay)
    logging.info("Response %s: finishing", name)


if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    
    tracemalloc.start()
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())

    start = time.time()
    tasks = itertools.starmap(asinc_function, responses)
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()

    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())

    print('All done! {}'.format(time.time() - start))