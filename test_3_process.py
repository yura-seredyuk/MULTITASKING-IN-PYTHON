import time
from multiprocessing import Pool
import logging
import tracemalloc

from data import RESPONSES as responses

def write_file(response):
    with open('file.txt', 'a') as f:
        for i in range(response[1] * 1000):
            f.write(response[0])

def pool_handler():
    p = Pool()
    p.map(write_file, responses)

if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    tracemalloc.start()
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
    
    start = time.time()

    pool_handler()
    
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())

    print("time: ", time.time() - start)
