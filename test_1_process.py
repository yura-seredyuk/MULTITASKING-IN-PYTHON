
from multiprocessing import Pool
import time
import tracemalloc
import logging
from data import RESPONSES as responses


def process_function(response):
    # logging.info("Process %s: starting", response[0])
    print("{}: Process {}: starting".format(time.strftime("%H:%M:%S", time.localtime()) ,response[0]))
    time.sleep(response[1])
    print("{}: Process {}: finishing".format(time.strftime("%H:%M:%S", time.localtime()), response[0]))

    # logging.info("Process %s: finishing", response[0])


def pool_handler():
    p = Pool()
    # format = "%(asctime)s: %(message)s"
    # logging.basicConfig(format=format, level=logging.INFO,
    #                     datefmt="%H:%M:%S")
    p.map(process_function, responses)


if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    start = time.time()
    tracemalloc.start()
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())

    pool_handler()
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
    print("time: ", time.time() - start)

 


