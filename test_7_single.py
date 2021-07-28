import csv
import time
import tracemalloc


def read_file():
    with open('data.csv', 'r', newline='') as file:
        filereader = csv.DictReader(file)
        for row in filereader:
            # print(row)
            pass
        file.close()

if __name__ == "__main__":
    tracemalloc.start()
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
    start = time.time()
    read_file()
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
    print("time: ", time.time() - start)
