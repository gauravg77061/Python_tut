import asyncio
import threading
import time

def background_worker():
    while True:
        time.sleep(1)
        print("Logging the system every sec")

async def fetch__order():
    await asyncio.sleep(3)
    print("fetching order")

threading.Thread(target=background_worker,daemon=True).start()

asyncio.run(fetch__order())