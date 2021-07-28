import csv
import time
import tracemalloc
import threading


def read_file(_):
    with open('data.csv', 'r', newline='') as file:
        filereader = csv.DictReader(file)
        for row in filereader:
            # print(row)
            pass
        file.close()


if __name__ == "__main__":
    threads = list()
    tracemalloc.start()
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
    start_time = time.time()
    for item in range(1000000, 1000016):
        thread = threading.Thread(target=read_file, args=(item,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
    print("time: ", time.time() - start_time)
