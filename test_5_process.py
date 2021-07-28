import time
from multiprocessing import Pool
import tracemalloc


def write_file(i):
    with open(f'../../test_files/file_{i}.txt', 'w') as f:
        f.write('data')

    with open(f'../../test_files/file_{i}.txt', 'r') as f:
        _ = f.read()
        
def pool_handler():
    p = Pool()
    p.map(write_file, range(10000))

if __name__ == '__main__':
    tracemalloc.start()
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
    
    start = time.time()

    pool_handler()
    
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())

    print("time: ", time.time() - start)
