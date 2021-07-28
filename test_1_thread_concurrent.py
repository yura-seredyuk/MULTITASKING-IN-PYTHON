import logging
import time
import tracemalloc
import concurrent.futures
from data import RESPONSES as responses


def thread_function(response):
    logging.info("Thread %s: starting", response[0])
    time.sleep(response[1])
    logging.info("Thread %s: finishing", response[0])

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    start = time.time()
    tracemalloc.start()
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        executor.map(thread_function, responses)
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
    print('All done! {}'.format(time.time() - start))