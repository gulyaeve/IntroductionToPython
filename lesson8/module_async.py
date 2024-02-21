import asyncio


async def f1():
    print("Функция 1")
    await asyncio.sleep(15)
    print("Функция 1 завершена")


async def f2():
    print("Функция 2")
    await asyncio.sleep(10)
    print("Функция 2 завершена")


async def f3():
    print("Функция 3")
    await asyncio.sleep(3)
    print("Функция 3 завершена")


async def main():
    # task1 = asyncio.create_task(f1())
    # task2 = asyncio.create_task(f2())
    # task3 = asyncio.create_task(f3())
    #
    # await asyncio.gather(task1, task2, task3)

    async with asyncio.TaskGroup() as tg:
        tg.create_task(f1())
        tg.create_task(f2())

        # for i in range(10):
        #     tg.create_task(f3())


if __name__ == '__main__':
    asyncio.run(main())
