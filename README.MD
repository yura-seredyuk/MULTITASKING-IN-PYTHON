# MULTITASKING IN PYTHON: SINGLE-THREADING VS MULTIPROCESSING VS MULTITHREADING VS ASYNCHRONY
![process_img](https://pythonworld.ru/m/img/python-3.png)


### Text content
1. [Basic concepts](https://github.com/yura-seredyuk/MULTITASKING-IN-PYTHON/blob/master/README.MD#basic-concepts)
2. [Single-threaded programming](https://github.com/yura-seredyuk/MULTITASKING-IN-PYTHON/blob/master/README.MD#single-threaded-programming)
3. [Parallel (multiprocessing) programming](https://github.com/yura-seredyuk/MULTITASKING-IN-PYTHON/blob/master/README.MD#multiprocessing-programming)
4. [Multithreading programming](https://github.com/yura-seredyuk/MULTITASKING-IN-PYTHON/blob/master/README.MD#multithreading-programming)
5. [Asynchronous programming](https://github.com/yura-seredyuk/MULTITASKING-IN-PYTHON/blob/master/README.MD#asynchronous-programming)
6. [Examples and tests](https://github.com/yura-seredyuk/MULTITASKING-IN-PYTHON/blob/master/README.MD#examples-and-tests)
7. [Conclusions and differences](https://github.com/yura-seredyuk/MULTITASKING-IN-PYTHON/blob/master/README.MD#conclusions-and-differences)

## Basic concepts:

#### A funny but clear example
You need to dig a pool in the yard.<br/> 
You take a shovel and dig. This is a single-threaded job<br/> 
<img src="https://github.com/yura-seredyuk/MULTITASKING-IN-PYTHON/blob/master/prezent_pictures/pic_1.png" width="300"><br/> 

You invited your friend Vasya and dig together, periodically hitting each other with shovels. This is multi-threaded work<br/> 
<img src="https://github.com/yura-seredyuk/MULTITASKING-IN-PYTHON/blob/master/prezent_pictures/pic_2.png" width="300"><br/> 

While you are digging the pool, Vasya is digging a ditch for the water supply. Nobody bothers anyone. This is parallel (multiprocessing) work<br/> 
<img src="https://github.com/yura-seredyuk/MULTITASKING-IN-PYTHON/blob/master/prezent_pictures/pic_3.png" width="300"><br/> 

You invited a team of excavators, and you and Vasya went to drink beer. When the brigade has done everything, they will come to you for money. This is an asynchronous job.<br/> 
<img src="https://github.com/yura-seredyuk/MULTITASKING-IN-PYTHON/blob/master/prezent_pictures/pic_4.png" width="300"><br/> 

The number of shovels on the farm is the number of cores in the system



### Processes
What is a process? Each process as being a separate program. Each process runs independently from all the others, so in a typical Python program, you will write many processes which are all running at the same time.<br/> 
Process has its own memory space.<br/> 
<img src="https://github.com/yura-seredyuk/MULTITASKING-IN-PYTHON/blob/master/prezent_pictures/pic_5.png" width="300">

### Threads
A thread is the unit of execution within a process. A process can have multiple threads running as a part of it, where each thread uses the process’s memory space and shares it with other threads.<br/>
In Python, by default programs run as a single process with a single thread of execution; this uses just a single CPU.<br/>
A thread is a light-weight process that does not require much memory overhead, they are cheaper than processes.<br/>
<img src="https://github.com/yura-seredyuk/MULTITASKING-IN-PYTHON/blob/master/prezent_pictures/pic_6.png" width="300">

### Coroutines
Coroutines are a more generalized form of subroutines. Subroutines are entered at one point and exited at another point. Coroutines can be entered, exited, and resumed at many different points.<br/>
```python
import asyncio 

async def count_to_three(): 
  print(" Counting down. 1") 
  await asyncio.sleep(0) 
  print(" Counting down. 2") 
  await asyncio.sleep(0) 
  print(" Counting down. 3") 
  await asyncio.sleep(0)
  
coroutine_counter = count_to_three() 
print(coroutine_counter) # <coroutine object count_to_three at 0x7f5a58486a98> 
coroutine_counter.send(None) # output " Counting down. 1" coroutine_counter.send(None) # output " Counting down. 2" coroutine_counter.send(None) # output " Counting down. 3
coroutine_counter.send(None) # will throw an error StopIteration
```
<img src="https://github.com/yura-seredyuk/MULTITASKING-IN-PYTHON/blob/master/prezent_pictures/pic_7.png" width="300">

## Single-threaded programming

<img src="https://github.com/yura-seredyuk/MULTITASKING-IN-PYTHON/blob/master/prezent_pictures/pic_8.png" width="300">  <img src="https://github.com/yura-seredyuk/MULTITASKING-IN-PYTHON/blob/master/prezent_pictures/pic_9.png" width="300">

## Multiprocessing programming

**Multiprocessing** is a technique where parallelism in its truest form is achieved. Multiple processes are run across multiple CPU cores, which do not share the resources among them. Each process can have many threads running in its own memory space. In Python, each process has its own instance of Python interpreter doing the job of executing the instructions.<br/>
<img src="https://github.com/yura-seredyuk/MULTITASKING-IN-PYTHON/blob/master/prezent_pictures/pic_10.png" width="300">
<img src="https://github.com/yura-seredyuk/MULTITASKING-IN-PYTHON/blob/master/prezent_pictures/pic_11.png" width="300"><br/>

Needed library: [multiprocessing](https://docs.python.org/3/library/multiprocessing.html) (internal library) 
```python
from multiprocessing import Pool
```
A prime example of this is the Pool object which offers a convenient means of parallelizing the execution of a function across multiple input values, distributing the input data across processes (data parallelism).
```python
from multiprocessing import Pool 


def f(x): 
	return x*x 
if __name__ == '__main__’: 
	with Pool(5) as p: 
		print(p.map(f, [1, 2, 3]))

```
In multiprocessing, processes are spawned by creating a Process object and then calling its start() method. Process follows the API of threading.Thread. A trivial example of a multiprocess program is
```python
from multiprocessing import Process 


def f(name): 
	print('hello', name) 

if __name__ == '__main__’: 
	p = Process(target=f, args=('bob’,))
	p.start() 
	p.join()

```

## Multithreading programming

**Multithreading** is a technique where multiple threads are spawned by a process to do different tasks, at about the same time, just one after the other. This gives you the illusion that the threads are running in parallel, but they are actually run in a concurrent manner. In Python, the Global Interpreter Lock (GIL) prevents the threads from running simultaneously.<br >

<img src="https://github.com/yura-seredyuk/MULTITASKING-IN-PYTHON/blob/master/prezent_pictures/pic_12.png" width="300">
<img src="https://github.com/yura-seredyuk/MULTITASKING-IN-PYTHON/blob/master/prezent_pictures/pic_13.png" width="300"><br/>

Needed library: [threading](https://docs.python.org/3/library/threading.html#module-threading) (internal library) 

```python
import threading
```
The **Thread** class represents an activity that is run in a separate thread of control. There are two ways to specify the activity: by passing a callable object to the constructor, or by overriding the **run()** method in a subclass. <br/>
Once a thread object is created, its activity must be started by calling the thread’s **start()** method. This invokes the run() method in a separate thread of control.<br/>
Other threads can call a thread’s **join()** method. This blocks the calling thread until the thread whose _join()_ method is called is terminated.
```python
import threading 

def doubler(number): 
	print(threading.currentThread().getName() + '\n’) 	
	print(number * 2)
if __name__ == '__main__’: 
	for i in range(5): 
	my_thread = threading.Thread(target=doubler, args=(i,)) 	 	
  my_thread.start()
	my_thread.join()

```

## Asynchronous programming

**AsyncIO** is a single thread single process cooperative multitasking. An asyncio task has exclusive use of CPU until it wishes to give it up to the coordinator or event loop.<br/>

<img src="https://github.com/yura-seredyuk/MULTITASKING-IN-PYTHON/blob/master/prezent_pictures/pic_14.png" width="300"><br/>
Needed library: [asyncio](https://docs.python.org/3/library/asyncio.html?highlight=asyncio) (pip install asyncio) 
```python
import asyncio
```
**asyncio** is a library to write concurrent code using the **async/await** syntax.
```python
import asyncio

async def main(): 
	print('Hello ...’) 
	await asyncio.sleep(1) 
	print('... World!’) 

# Python 3.7+ 
asyncio.run(main())
```
**asyncio.get_event_loop()** - Get the current event loop.<br/>
**loop.run_until_complete(future)** - Run until the future (an instance of Future) has completed.<br/>
**loop.close()** - Close the event loop.<br/>
<img src="https://github.com/yura-seredyuk/MULTITASKING-IN-PYTHON/blob/master/prezent_pictures/pic_15.png" width="300"><br/>

## Examples and tests
### Test methods
Time
```python
import time

#calculate full work time
start = time.time()
…
print('All done! {}'.format(time.time() - start)) 
```
Logging
```python
import logging
#logging start and finishing time of tasks
format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
…
logging.info("Response %s: starting", name)
…
logging.info("Response %s: finishing", name)
```
Memory
```python
import tracemalloc
#calculate using memory
tracemalloc.start()
print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
…
print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
```
### Files

### Best results by the time for all tests
 | params | Single-threaded | Multiprocessing | Multithreading | Asynchronous 
|:------------:|:------------:|:---------------:|:---------------:|:---------------:|:---------------:|
TEST 1
sleep |

TEST 2
fetch URL 
1 000 times

TEST 3
multiple writing into one local file

TEST 4
heavy operations 

TEST 5
IO operations (multiple files – 10k)

TEST 6
reading from API and writing to the local file 100 times


memory | 
Current: 20 282, 
Peak 25 563 | 
Current: 1 022 389, 
Peak 1 051 123 | 
Current: 154 908, 
Peak 166 532 | 
Current: 66 280, 
Peak 95 110 | 
time
178.10015487670898
27.14326310157776
10.008656024932861
10.002372026443481
memory
Current: 1 675 405, 
Peak 1 810 874
Current: 641 498, 
Peak 3 579 588
Current: 2 162 746, 
Peak 14 674 889
Current: 5 127 574, 
Peak 22 147 351
time
243.5635371208191
81.55517721176147
6.851548910140991
9.241158246994019
memory
Current: 675, 
Peak 81 117
Current: 1 025 853, 
Peak 1 053 928
Current: 84 790, 
Peak 169 612
Current: 272 825, 
Peak 1 529 655
time
0.04591989517211914
0.11201786994934082
0.05333209037780762
8.34945011138916
memory
Current: 28, 
Peak 11958404
Current: 1025991, Peak 46066981
Current: 53555, 
Peak 22619938
Current: 30838, 
Peak 51858706
time
78.15798282623291
14.848083972930908
77.25872468948364
78.71868419647217
memory
Current: 1 493, 
Peak 7 493
Current: 1 157 226, Peak 1 269 901
Current: 26 445 306, 
Peak 28 063 475
Current: 1 300 008, 
Peak 118 920 105
time
1.0173640251159668
0.8301951885223389
1.4301888942718506
5.764318943023682
memory
Current: 254 820, 
Peak 311 684
Current: 614 687, 
Peak 643 421
Current: 790 740, 
Peak 4 814 464
Current: 974 525, 
Peak 3 735 296
time
43.93997097015381
11.277347087860107
9.835943937301636
9.256136894226074


## Conclusions and differences
```python

```



