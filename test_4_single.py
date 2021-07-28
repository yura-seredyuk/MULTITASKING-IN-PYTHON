import time
import tracemalloc

def power(x):
    return x ** x

if __name__ == "__main__":
    tracemalloc.start()
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
    start_time = time.time()
    for i in range(1000000, 1000016):
        power(i)
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
    print("time: ", time.time() - start_time)

