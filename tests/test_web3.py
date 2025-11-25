import json
import traceback
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
        'SUGAR_RPC_URI_8453': 'https://lb.drpc.live/base/',
        'POOLS_COUNT_UPPER_BOUND_8453': '25000',   #扩展pools的数量上限，默认2500，默认值无法探测到CL_Pools
    }
)


async def main():
    async with stdio_client(server) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            #response = await session.list_tools()
            #tools = [dict(t) for t in response.tools]
            #print(json.dumps(tools, indent=4, ensure_ascii=False))
            tools_to_call = [
                    ('get_pool_list', 
                     #
                     {
                        'tokens': ['0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913','0x4200000000000000000000000000000000000006'],
                        'pool_type': 'v2', 
                        'sort_by': 'tvl', 
                        'limit': 10, 
                        'offset': 0, 
                        'chainId': '8453'
                     }
                    ),
                    ('get_pools_by_token',
                        {
                            'token_address': '0x4200000000000000000000000000000000000006',
                            'pool_type': 'v3',
                            'chainId': '8453'
                        }
                    ),
                    ('get_pools_by_pair',
                        {
                            'token0_address': '0x4200000000000000000000000000000000000006',
                            'token1_address': '0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913',
                            'chainId': '8453'
                        }
                    )            
                ]
            
            for tool_name, args in tools_to_call:
                print(f"\n🛠️ 正在调用工具: {tool_name}")
                try:
                    response = await session.call_tool(tool_name, arguments=args)
                    
                    print("✅ 调用成功!")
                    for content in response.content:
                        print(json.dumps(json.loads(content.text), indent=1, ensure_ascii=False))
                    print(f"📊 结果数量: {len(response.content)}")
                    
                except Exception as e:
                    print(f"❌ 调用工具 {tool_name} 失败: {e}")
                    print(f"详细错误信息: {traceback.format_exc()}")
                    continue


if __name__ == "__main__":
    asyncio.run(main())
