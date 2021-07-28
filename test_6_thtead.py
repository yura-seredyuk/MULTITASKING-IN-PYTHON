import requests
import time
import tracemalloc
import threading


def write_genre(file_name):
    response = requests.get("https://binaryjazz.us/wp-json/genrenator/v1/genre/")
    genre = response.json()

    with open(file_name, "a") as new_file:
        # print(f'Written "{genre}" to a file "{file_name}"...')
        new_file.write(f'{genre}\n')

if __name__ == '__main__':
    count = 100
    threads = list()
    tracemalloc.start()
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
    start = time.time()
    for item in range(1,count):
            thread = threading.Thread(target=write_genre, args=('genetate.txt',))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
    print("time: ", time.time() - start)