import time
import tracemalloc
import threading

def power(x):
    return x ** x


if __name__ == "__main__":
    threads = list()
    tracemalloc.start()
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
    start_time = time.time()
    for item in range(1000000, 1000016):
        thread = threading.Thread(target=power, args=(item,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
    print("time: ", time.time() - start_time)

