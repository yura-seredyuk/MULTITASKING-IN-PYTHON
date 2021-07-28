import logging
import time
import tracemalloc
from data import RESPONSES as responses


def single_function(name, delay):
    logging.info("Response %s: starting", name)
    time.sleep(delay)
    logging.info("Response %s: finishing", name)

if __name__ == "__main__":

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    tracemalloc.start()
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())

    start = time.time()
    for item in responses:
        single_function(item[0], item[1])
    
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())

    print('All done! {}'.format(time.time() - start))