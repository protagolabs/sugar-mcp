import json

from mcp.client.stdio import stdio_client, StdioServerParameters
from mcp import ClientSession
import asyncio

server = StdioServerParameters(
    command='python',
    args=['/Users/yanrujing/Desktop/workspace/code/Sugar-MCP/src/sugar_mcp/server.py'],
    env={
        'http_proxy': 'http://127.0.0.1:1087',
        'https_proxy': 'http://127.0.0.1:1087',
        'SUGAR_PK': 'xxx',
        # 'SUGAR_RPC_URI_10': 'https://myrpc.com'
    }
)


async def main():
    async with stdio_client(server) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            response = await session.list_tools()
            tools = [dict(t) for t in response.tools]
            print(json.dumps(tools, indent=4, ensure_ascii=False))

            response = await session.call_tool(
                'swap',
                arguments={
                    'from_token': 'velo',
                    'to_token': 'eth',
                    'amount': 10
                }
            )
            epochs = json.loads(response.content[0].text)
            print(len(epochs))

            response = await session.call_tool(
                'get_quote',
                arguments={
                    'from_token': 'velo',
                    'to_token': 'eth',
                    'amount': 10
                }
            )
            epochs = json.loads(response.content[0].text)
            print(len(epochs))

            response = await session.call_tool(
                'get_pool_by_address',
                arguments={
                    'address': '0x904f14F9ED81d0b0a40D8169B28592aac5687158'
                }
            )
            epochs = json.loads(response.content[0].text)
            print(len(epochs))

            response = await session.call_tool(
                'get_pools_for_swaps',
            )
            epochs = json.loads(response.content[0].text)
            print(len(epochs))

            response = await session.call_tool(
                'get_pool_epochs',
                arguments={
                    'lp': '0x7A7f1187c4710010DB17d0a9ad3fcE85e6ecD90a'
                }
            )
            epochs = json.loads(response.content[0].text)
            print(len(epochs))

            response = await session.call_tool(
                'get_latest_pool_epochs'
            )
            epochs = json.loads(response.content[0].text)
            print(len(epochs))

            response = await session.call_tool(
                'get_pools'
            )
            pools = json.loads(response.content[0].text)
            print(len(pools))

            response = await session.call_tool(
                "get_all_tokens",
            )
            tokens = json.loads(response.content[0].text)
            print(len(tokens))

            response = await session.call_tool(
                "get_prices",
            )
            prices = json.loads(response.content[0].text)
            print(len(prices))


if __name__ == "__main__":
    asyncio.run(main())
