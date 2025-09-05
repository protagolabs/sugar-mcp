import json
from mcp.client.sse import sse_client
from mcp import ClientSession
import asyncio


url = "http://127.0.0.1:8000/sse"
# url = "https://mcp.netmind.ai/sse/4a8e68a6490342d3b1c7fbee0ad1b508/sugar-mcp/sse?SUGAR_PK=d3c9e669cca21d6d9cc186a4d710b7127bcc84ed0184d94ee42766f8d63c8df9"

async def main():
    async with sse_client(url) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            try:
                response = await session.call_tool(
                    "get_all_tokens",
                    {
                        "limit": 2,
                        "offset": 0,
                        "chain_id": "8453"
                    }
                )

                data = json.loads(response.content[0].text)
                print(json.dumps(data, indent=2, ensure_ascii=False))

                response = await session.call_tool(
                    "get_token_prices",
                    {
                        "token_address": "0x4200000000000000000000000000000000000006",
                        "chain_id": "8453"
                    }
                )

                data = json.loads(response.content[0].text)
                print(json.dumps(data, indent=2, ensure_ascii=False))

                response = await session.call_tool(
                    "get_prices",
                    {
                        "limit": 2,
                        "offset": 0,
                        "listed_only": False,
                        "chain_id": "8453"
                    }
                )

                data = json.loads(response.content[0].text)
                print(json.dumps(data, indent=2, ensure_ascii=False))

                response = await session.call_tool(
                    "get_pools",
                    {
                        "limit": 2,
                        "offset": 0,
                        "chain_id": "8453"
                    }
                )

                data = json.loads(response.content[0].text)
                print(json.dumps(data, indent=2, ensure_ascii=False))

                response = await session.call_tool(
                    "get_pools_for_swaps",
                    {
                        "limit": 2,
                        "offset": 0,
                        "chain_id": "8453"
                    }
                )

                data = json.loads(response.content[0].text)
                print(json.dumps(data, indent=2, ensure_ascii=False))


                response = await session.call_tool(
                    "get_latest_pool_epochs",
                    {
                        "offset": 0,
                        "limit": 10,
                        "chain_id": "8453"
                    }
                )

                data = json.loads(response.content[0].text)
                print(json.dumps(data, indent=2, ensure_ascii=False))


                response = await session.call_tool(
                    "get_pool_epochs",
                    {
                        "lp": "0x2722C8f9B5E2aC72D1f225f8e8c990E449ba0078",
                        "offset": 0,
                        "limit": 10,
                        "chain_id": "8453"
                    }
                )

                data = json.loads(response.content[0].text)
                print(json.dumps(data, indent=2, ensure_ascii=False))

            except Exception as e:
                print(f"Error listing tools: {e}")


if __name__ == "__main__":
    asyncio.run(main())