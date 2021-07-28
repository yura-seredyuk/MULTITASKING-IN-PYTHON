import concurrent.futures
import time
from multiprocessing import Pool
import logging
import tracemalloc

def power(x):
    return x ** x

def main():
    p = Pool()
    p.map(power, [i for i in range(1000000, 1000016)])  

if __name__ == "__main__":
    # pow_list = [i for i in range(1000000, 1000016)]

    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     futures = [executor.submit(pow, i, i) for i in pow_list]
    tracemalloc.start()
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
    start_time = time.time()
    response = main()
    # for f in concurrent.futures.as_completed(futures):
    #     print('okay')
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
    print("time: ", time.time() - start_time)

