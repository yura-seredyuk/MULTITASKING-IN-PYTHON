import time
import threading
import tracemalloc


def write_file(i):
    with open(f'../../test_files/file_{i}.txt', 'w') as f:
        f.write('data')

    with open(f'../../test_files/file_{i}.txt', 'r') as f:
        _ = f.read()
        

if __name__ == '__main__':    
    threads = list()
    tracemalloc.start()
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())

    start = time.time()
    for item in range(10000):
        thread = threading.Thread(target=write_file, args=(item,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())

    print("time: ", time.time() - start)
