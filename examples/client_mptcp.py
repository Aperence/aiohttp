import aiohttp
from aiohttp import TCPConnector
import asyncio

async def fetch(client):
    async with client.get('http://127.0.0.1:8080') as resp:
        assert resp.status == 200
        return await resp.text()

async def main():
    connector = TCPConnector(enable_mptcp=True)
    async with aiohttp.ClientSession(connector=connector) as client:
        html = await fetch(client)
        print(html)

asyncio.run(main())
