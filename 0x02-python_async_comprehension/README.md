# 0x02-python_async_comprehension

Python has extensive support for synchronous comprehensions, allowing to produce lists, dicts, and sets with a simple and concise syntax. We propose implementing similar syntactic constructions for the asynchronous code.

## Documentation

[PEP 530 – Asynchronous Comprehensions](https://peps.python.org/pep-0530/)

[Asynchronous Comprehensions / Generators](https://www.blog.pythonlibrary.org/2017/02/14/whats-new-in-python-asynchronous-comprehensions-generators/)

[Documentation](https://stackoverflow.com/questions/42531143/how-to-type-hint-a-generator-in-python-3)


## Tasks

[0-async_generator.py](https://github.com/Mmaureeny/alx-backend-python/blob/main/0x02-python_async_comprehension/0-async_generator.py)

 A coroutine called async_generator that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the random module.

[1-async_comprehension.py ](https://github.com/Mmaureeny/alx-backend-python/blob/main/0x02-python_async_comprehension/1-async_comprehension.py)

 The coroutine will collect 10 random numbers using an async comprehensing over async_generator, then return the 10 random numbers.

 Import async_generator from the previous task and then write a coroutine called async_comprehension that takes no arguments.
 
 [2-measure_runtime.py ](https://github.com/Mmaureeny/alx-backend-python/blob/main/0x02-python_async_comprehension/2-measure_runtime.py)
 
 Import async_comprehension from the previous file and write a measure_runtime coroutine that will execute async_comprehension four times 
 in parallel using asyncio.gather.
 measure_runtime should measure the total runtime and return it.
