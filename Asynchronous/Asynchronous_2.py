import asyncio
async def txt():
    print("Hi this is asyncio ")
    #This output returns the string value 'Hi this is asyncio'
    await msg("Asyncio is taling to you")
    #this output runs as soon as the above string value is returned 
    print("Asyncio is pleased to meet you")
    #this output waits for 4 seconds as it is been mentioned below

async def msg(Sentence):
    print(Sentence)
    await asyncio.sleep(4)

asyncio.run(txt())