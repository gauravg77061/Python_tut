import asyncio

async def brew(name):
    print(f"Brewing {name} chai ...")
    await asyncio.sleep(3)
    print(f"{name} is ready")

async def main():
    await asyncio.gather(
        brew('Masala chai'),
        brew('Green chaii'),
        brew('Ginger chai'),
    )

asyncio.run(main())