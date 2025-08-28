import asyncio 
async def name():
    print("Pavan Kumar")
    task = asyncio.create_task(age(int(18)))
    print("You have entered into your adulthood")


async def age(Number):
    print(Number)
    await asyncio.sleep(5)

asyncio.run(name())