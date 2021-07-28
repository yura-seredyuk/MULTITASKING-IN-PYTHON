import time
import logging
import tracemalloc

from data import RESPONSES as responses

def write_file(item, count):
    with open('file.txt', 'a') as f:
        for i in range(count * 1000):
            f.write(item)

if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    
    tracemalloc.start()
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())

    start = time.time()
    for item in responses:
        write_file(item[0], item[1])
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
    
    print("time: ", time.time() - start)

    