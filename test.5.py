
import httpx
import asyncio



async def main():
  async with httpx.AsyncClient() as client:
   res = await client.get("https://www.youtube.com")
   print(res)

asyncio.run(main())