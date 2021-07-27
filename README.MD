# MULTITASKING IN PYTHON: SINGLE-THREADING VS MULTIPROCESSING VS MULTITHREADING VS ASYNCHRONY
![process_img](https://pythonworld.ru/m/img/python-3.png)


### Text content
1. [Basic concepts]()
2. [Single-threaded programming]
3. [Parallel (multiprocessing) programming]
4. [Multithreading programming]
5. [Asynchronous programming]
6. [Examples and tests]
7. [Conclusions and differences]

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
## Multiprocessing programming
## Multithreading programming
## Asynchronous programming
## Examples and tests
### Test methods
### Files
### Results
## Conclusions and differences



