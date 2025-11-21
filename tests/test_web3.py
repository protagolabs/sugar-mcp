import json

from mcp.client.stdio import stdio_client, StdioServerParameters
from mcp import ClientSession
import asyncio

server = StdioServerParameters(
    # 设置本地运行环境
    # command='python',
    # args=['/Users/yanrujing/Desktop/workspace/code/Sugar-MCP/src/sugar_mcp/server.py'],

    command='python3',
    args=['/Users/ming/project/python/sugar-mcp/src/sugar_mcp/server.py'],
    
    # 设置Sugar-SDK环境变量
    env={
        #'http_proxy': 'http://127.0.0.1:1087',
        #'https_proxy': 'http://127.0.0.1:1087',
        'SUGAR_PK': 'xxx',
        'SUGAR_RPC_URI_8453': 'https://lb.drpc.org/base/',
        'pools_count_upper_bound': '25000',   #扩展pools的数量上限，默认2500，默认值无法探测到CL_Pools
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
                'get_pool_list',
                arguments={
                    'tokens': ['0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913','0x4200000000000000000000000000000000000006'],
                    'chainId': '8453',
                    'sort_by': 'tvl'
                }
            )

         
            print('=========================')
            print('total pools:', len(response.content))
            for content in response.content:
                print(json.dumps(json.loads(content.text), indent=4, ensure_ascii=False))
          
          
if __name__ == "__main__":
    asyncio.run(main())
