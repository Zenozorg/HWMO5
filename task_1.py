import requests
import time
import aiohttp
import asyncio

urls = ["https://www.youtube.com/?app=desktop&hl=ru" for _ in range(100)]

def fetch_url(url):
    response = requests.get(url)
    return response.text

def fetch_all_urls_sequential(urls):
    results = []
    for url in urls:
        results.append(fetch_url(url))
    return results

async def fetch_url_async(session, url):
    async with session.get(url) as response:
        return await response.text()

async def fetch_all_urls_async(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url_async(session, url) for url in urls]
        return await asyncio.gather(*tasks)

start_time = time.time()
sequential_results = fetch_all_urls_sequential(urls)
sequential_duration = time.time() - start_time
print(f"Sequential duration: {sequential_duration} seconds")

start_time = time.time()
asyncio.run(fetch_all_urls_async(urls))
async_duration = time.time() - start_time
print(f"Async duration: {async_duration} seconds")
