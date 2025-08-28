import asyncio
async def ref():
    print("You need a strong network in college.")
    await reason("You can use it after your undergraduation")
    #this output runs as soon as the above string value is returned 
    print("It assists you to secure a job.")
    #this output waits for 4 seconds as it is been mentioned below



async def reason(text):
    print(text)
    await asyncio.sleep(5)

asyncio.run(ref())

