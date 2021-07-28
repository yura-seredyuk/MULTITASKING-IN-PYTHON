import time
import requests
import logging
from concurrent import futures
import tracemalloc


logging.getLogger().setLevel(logging.INFO)

def fetch_url(im_url):
    try:
        resp = requests.get(im_url)
    except Exception as e:
        logging.info("could not fetch {}".format(im_url))
    else:
        return resp.content
        

def fetch_all(url_list):
    with futures.ThreadPoolExecutor() as executor:
        responses = executor.map(fetch_url, url_list)
    return responses
    

if __name__=='__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
                        
    url = "https://www.google.com/"
    tracemalloc.start()
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
    for ntimes in [1, 10, 100, 500, 1000]:
        start_time = time.time()
        responses = fetch_all([url] * ntimes)
        logging.info('Fetch %s urls takes %s seconds', ntimes, time.time() - start_time)
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
