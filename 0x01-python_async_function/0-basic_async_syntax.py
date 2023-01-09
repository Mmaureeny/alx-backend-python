#!/usr/bin/env python3

import asyncio
import random

async def wait_random(max_delay=10):
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def main():
    delay = await wait_random()
    print(f"Waited for {delay} seconds")

asyncio.run(main())
