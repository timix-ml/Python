"""
# 1
Запускает 10 процессов

# 2
Запускает 10 потоков в каждом процессе

# 3 
Запускает в каждом потоке по 10 задача с worker()

В итоге worker(), выполниться 1000 раз в много процессорно-поточно-задачном режиме :)
"""

from asyncio import TaskGroup, run, sleep
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from os import getpid, getppid
from threading import get_native_id
from time import monotonic


async def worker(i: int):
    await sleep(1)
    print(f"Process: {getpid()} > Thread: {get_native_id()} > Task {i}")


# 3
async def task_start():
    async with TaskGroup() as pool:
        for i in range(10):
            pool.create_task(worker(i))


# 2
def thread_for():
    with ThreadPoolExecutor() as pool:
        for _ in range(10):
            pool.submit(run(task_start()))


# 1
def process_for():
    with ProcessPoolExecutor() as pool:
        for _ in range(10):
            pool.submit(thread_for)


if __name__ == "__main__":
    started_at = monotonic()
    print(process_for())
    print(monotonic() - started_at)
