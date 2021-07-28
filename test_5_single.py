import time
import logging
import tracemalloc

def write_file(i):
    with open(f'../../test_files/file_{i}.txt', 'w') as f:
        f.write('data')
        f.close()

    with open(f'../../test_files/file_{i}.txt', 'r') as f:
        _ = f.read()
        f.close()
    
if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    
    tracemalloc.start()
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())

    start = time.time()
    for i in range(10000):
        write_file(i)

    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
    
    print("time: ", time.time() - start)

       