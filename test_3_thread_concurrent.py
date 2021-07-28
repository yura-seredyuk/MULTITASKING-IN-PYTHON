import time
import concurrent.futures
import logging
import tracemalloc

from data import RESPONSES as responses


def write_file(response):
    with open('file.txt', 'a') as f:
        for i in range(response[1] * 1000):
            f.write(response[0])


if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    tracemalloc.start()
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
    
    start = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        executor.map(write_file, responses)
    
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())

    print("time: ", time.time() - start)
