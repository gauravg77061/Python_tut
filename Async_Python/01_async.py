import asyncio

async def brew_chai():
    print("Brewing chai")
    await asyncio.sleep(2)
    print("chai is raedy")

asyncio.run(brew_chai())
