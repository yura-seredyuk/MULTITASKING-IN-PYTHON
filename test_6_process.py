import requests
import time
from multiprocessing import Pool
import logging
import tracemalloc

def write_genre(_):
    response = requests.get("https://binaryjazz.us/wp-json/genrenator/v1/genre/")
    genre = response.json()

    with open('generate.txt', "a") as new_file:
        # print(f'Written "{genre}" to a file genetate.txt...')
        new_file.write(f'{genre}\n')

def main(count):
    p = Pool()
    p.map(write_genre, range(1,count))       
    

if __name__=='__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    tracemalloc.start()
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
    count = 100
    start_time = time.time()
    responses = main(count)

    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
    print("time: ", time.time() - start_time)
