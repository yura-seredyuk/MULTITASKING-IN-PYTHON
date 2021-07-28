import logging
import threading
import tracemalloc
import time
from data import RESPONSES as responses


def thread_function(name, delay):
    logging.info("Thread %s: starting", name)
    time.sleep(delay)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    threads = list()
    tracemalloc.start()
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())

    start = time.time()
    for item in responses:
        thread = threading.Thread(target=thread_function, args=(item[0], item[1],))
        threads.append(thread)
        thread.start()

    for index, thread in enumerate(threads):
        thread.join()
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())

    print('All done! {}'.format(time.time() - start))