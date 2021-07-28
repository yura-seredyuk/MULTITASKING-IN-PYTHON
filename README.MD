# MULTITASKING IN PYTHON: SINGLE-THREADING VS MULTIPROCESSING VS MULTITHREADING VS ASYNCHRONY

### Text content
1. [Basic concepts](https://github.com/yura-seredyuk/MULTITASKING-IN-PYTHON/blob/master/README.MD#basic-concepts)
2. [Single-threaded programming](https://github.com/yura-seredyuk/MULTITASKING-IN-PYTHON/blob/master/README.MD#single-threaded-programming)
3. [Parallel (multiprocessing) programming](https://github.com/yura-seredyuk/MULTITASKING-IN-PYTHON/blob/master/README.MD#multiprocessing-programming)
4. [Multithreading programming](https://github.com/yura-seredyuk/MULTITASKING-IN-PYTHON/blob/master/README.MD#multithreading-programming)
5. [Asynchronous programming](https://github.com/yura-seredyuk/MULTITASKING-IN-PYTHON/blob/master/README.MD#asynchronous-programming)
6. [Examples and tests](https://github.com/yura-seredyuk/MULTITASKING-IN-PYTHON/blob/master/README.MD#examples-and-tests)
7. [Conclusions and differences](https://github.com/yura-seredyuk/MULTITASKING-IN-PYTHON/blob/master/README.MD#conclusions-and-differences)
8. [Sources](https://github.com/yura-seredyuk/MULTITASKING-IN-PYTHON/blob/master/README.MD#sources)

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
```
TEST 1: sleep
- test_1_single.py
- test_1_process.py
- test_1_thtead.py
- test_1_async.py

TEST 2: fetch URL 1 000 times
- test_2_single.py
- test_2_process.py
- test_2_thtead.py
- test_2_async.py

TEST 3: multiple writing into one local file
- test_3_single.py
- test_3_process.py
- test_3_thtead.py
- test_3_async.py

TEST 4: heavy operations 
- test_4_single.py
- test_4_process.py
- test_4_thtead.py
- test_4_async.py

TEST 5: IO operations (multiple files – 10k)
- test_5_single.py
- test_5_process.py
- test_5_thtead.py
- test_5_async.py

TEST 6: reading from API and writing to the local file 100 times
- test_6_single.py
- test_6_process.py
- test_6_thtead.py
- test_6_async.py

TEST 7: reading big CSV file (~10Mb)
- test_7_single.py

Support files:
- generate_messages.py - generate data into data.py file for the TEST 1
- delete_files.py - delete files after TEST 5
- data_generator.py - generate CSV file data.csv 

```
### Best results by the time for all tests

		
		

<table>
	<thead>
		<tr>
			<th></th>
			<th>params</th>
			<th>Single-threaded</th>
			<th>Multiprocessing</th>
			<th>Multithreading</th>
			<th>Asynchronous</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td rowspan=2>TEST 1 sleep </td>
			<td>memory</td>
			<td>Current: 20 282, Peak 25 563</td>
			<td>Current: 1 022 389, Peak 1 051 123</td>
			<td>Current: 154 908, Peak 166 532</td>
			<td>Current: 66 280, Peak 95 110</td>
		</tr>
		<tr>
	    		<td>time</td>
			<td>178.10015487670898</td>
			<td>27.14326310157776</td>
			<td>10.008656024932861</td>
			<td>10.002372026443481</td>
		</tr>
		<tr>
			<td rowspan=2>TEST 2 fetch URL 1 000 times</td>
			<td>memory</td>
			<td>Current: 1 675 405, Peak 1 810 874</td>
			<td>Current: 641 498, Peak 3 579 588</td>
			<td>Current: 2 162 746, Peak 14 674 889</td>
			<td>Current: 5 127 574, Peak 22 147 351</td>
		</tr>
		<tr>
	    		<td>time</td>
			<td>243.5635371208191</td>
			<td>81.55517721176147</td>
			<td>6.851548910140991</td>
			<td>9.241158246994019</td>
		</tr>
		<tr>
			<td rowspan=2>TEST 3 multiple writing into one local file</td>
			<td>memory</td>
			<td>Current: 675, Peak 81 117</td>
			<td>Current: 1 025 853, Peak 1 053 928</td>
			<td>Current: 84 790, Peak 169 612</td>
			<td>Current: 272 825, Peak 1 529 655</td>
		</tr>
		<tr>
	    		<td>time</td>
			<td>0.04591989517211914</td>
			<td>0.11201786994934082</td>
			<td>0.05333209037780762</td>
			<td>8.34945011138916</td>
		</tr>		
		<tr>
			<td rowspan=2>TEST 4 heavy operations</td>
			<td>memory</td>
			<td>Current: 28, Peak 11958404</td>
			<td>Current: 1025991, Peak 46066981</td>
			<td>Current: 53555, Peak 22619938</td>
			<td>Current: 30838, Peak 51858706</td>
		</tr>
		<tr>
	    		<td>time</td>
			<td>78.15798282623291</td>
			<td>14.848083972930908</td>
			<td>77.25872468948364</td>
			<td>78.71868419647217</td>
		</tr>
		<tr>
			<td rowspan=2>TEST 5 IO operations (multiple files – 10k)</td>
			<td>memory</td>
			<td>Current: 1 493, Peak 7 493</td>
			<td>Current: 1 157 226, Peak 1 269 901</td>
			<td>Current: 26 445 306, Peak 28 063 475</td>
			<td>Current: 1 300 008, Peak 118 920 105</td>
		</tr>
		<tr>
	    		<td>time</td>
			<td>1.0173640251159668</td>
			<td>0.8301951885223389</td>
			<td>1.4301888942718506</td>
			<td>5.764318943023682</td>
		</tr>
		<tr>
			<td rowspan=2>TEST 6 reading from API and writing to the local file 100 times</td>
			<td>memory</td>
			<td>Current: 254 820, Peak 311 684</td>
			<td>Current: 614 687, Peak 643 421</td>
			<td>Current: 790 740, Peak 4 814 464</td>
			<td>Current: 974 525, Peak 3 735 296</td>
		</tr>
		<tr>
	    		<td>time</td>
			<td>43.93997097015381</td>
			<td>11.277347087860107</td>
			<td>9.835943937301636</td>
			<td>9.256136894226074</td>
		</tr>
	</tbody>
</table>


## Conclusions and differences
**Threading**
- Thread: shared memory (easier communication between threads)
- Need a lock for non atomic function like increment counter
- To avoid lock, use thread-safe atomic message queue
- Utilize single core: concurrent execution, subject to GIL (Global Interpreter Lock)
- Task switching handled by OS
- Very hard to write and maintain correct code

**Multiprocessing**
- Utilize multiple CPU cores: good for CPU bound task, bypass GIL limitation, parallel execution
- Process: separate and larger memory footprint
- IPC (Inter Process Communications) more complicated and overheads than threads
- Spawn process is slower than launch thread
- You can kill a process (but not a thread)

**Asyncio**
- Faster than threads
- Replace callbacks with await
- Good for IO bound
- Harder to write than threading, but easier to get it right than threading.
- Utilize single core only: concurrent but not parallel execution

- Mix asyncio with multiprocessing to utilize multi core: [aiomultiprocess](https://github.com/omnilib/aiomultiprocess)

**where used**
Synchronous, not CPU Bound, Only local files I/O Bound => **Single trading**<br/>
CPU Bound =>** Multi Processing**<br/>
I/O Bound, Fast I/O, Limited Number of Connections => **Multi Threading**<br/>
I/O Bound, Slow I/O, Many connections => **Asyncio**<br/>


```python
if io_bound: 
	if io_very_slow: 
		print("Use Asyncio") 	
	else: 
		print("Use Threads") 
	else: 
		print("Multi Processing")
```
<img src="https://github.com/yura-seredyuk/MULTITASKING-IN-PYTHON/blob/master/prezent_pictures/pic_16.png" width="300"><br/>

## Sources
- [Python’s GIL — A Hurdle to Multithreaded Program](https://medium.com/python-features/pythons-gil-a-hurdle-to-multithreaded-program-d04ad9c1a63)
- [Асинхронный ввод-вывод с Python 3](https://code.tutsplus.com/ru/tutorials/asynchronous-io-with-python-3--cms-29045)
- [Socket Programming with Multi-threading in Python](https://www.geeksforgeeks.org/socket-programming-multi-threading-python/)
- [Difference Between Multithreading vs Multiprocessing in Python](https://www.geeksforgeeks.org/difference-between-multithreading-vs-multiprocessing-in-python/?ref=rp)
- [A better way for asynchronous programming: asyncio over multi-threading](https://towardsdatascience.com/a-better-way-for-asynchronous-programming-asyncio-over-multi-threading-3457d82b3295)
- [Parallel, Asynchronous, Multithreading programming](https://stefaniuk.website/all/parallel-asynchronous-multithreading-programming/)
- [Intro to Threads and Processes in Python](https://medium.com/@bfortuner/python-multithreading-vs-multiprocessing-73072ce5600b)


