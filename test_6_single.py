import requests
import time
import tracemalloc


def write_genre(file_name):
    response = requests.get("https://binaryjazz.us/wp-json/genrenator/v1/genre/")
    genre = response.json()

    with open(file_name, "a") as new_file:
        # print(f'Written "{genre}" to a file "{file_name}"...')
        new_file.write(f'{genre}\n')

count = 100
tracemalloc.start()
print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
start = time.time()
for i in range(1,count):
    write_genre('generate.txt')
print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
print("time: ", time.time() - start)