# 0x02-python_async_comprehension

Python has extensive support for synchronous comprehensions, allowing to produce lists, dicts, and sets with a simple and concise syntax. We propose implementing similar syntactic constructions for the asynchronous code.

[0-async_generator.py](https://github.com/Mmaureeny/alx-backend-python/blob/main/0x02-python_async_comprehension/0-async_generator.py)

 A coroutine called async_generator that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the random module.
