import asyncio
async def value():
    print("Degree doesn't matter in securing a job.")
    await reason("Skillsets are more important when it comes to secure a job.")
    print("Companies have nothing to do with degree, it's just a piece of paper")


async def reason(Text):
    print(Text)
    await asyncio.sleep(4)


asyncio.run(value())