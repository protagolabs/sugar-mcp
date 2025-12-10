import json
from mcp.client.sse import sse_client
from mcp import ClientSession
import asyncio


url = "http://127.0.0.1:8089/sse"

async def main():
    async with sse_client(url) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools_to_call = [
                      ('get_pool_list', 
                            {
                                'token_address_list': ['0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913','0xcbB7C0000aB88B473b1f5aFd9ef808440eed33Bf'],
                                'pool_type': 'all', 
                                'sort_by': 'tvl', 
                                'chainId': '8453'
                            }
                      ),
                    # ('get_pools_by_token',
                    #     {
                    #         'token_address': '0x940181a94A35A4569E4529A3CDfB74e38FD98631',
                    #         'limit': 5,
                    #         'offset': 0,
                    #         'chainId': '8453'
                    #     }
                    # ),
                    # ('get_pools_by_pair',
                    #     {
                    #         'token0_address': '0x4200000000000000000000000000000000000006',
                    #         'token1_address': '0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913',
                    #         'limit': 5,
                    #         'offset': 0,
                    #         'chainId': '8453'
                    #     }
                    # ),
                   
                               
                ]
            
            for tool_name, args in tools_to_call:
                print(f"\n🛠️ 正在调用工具: {tool_name}")
                try:
                    response = await session.call_tool(tool_name, arguments=args)
                    # print("response:", response)
                    
                    print("✅ 调用成功!")
                    for content in response.content:
                        # print("Raw content:", content.text)
                        print("--------------------------------")
                        try:
                            data = json.loads(content.text)
                            print("LP Address:", data['lp'])
                            print("LP type:", data['type'])
                            print("is_stable:", data['is_stable'])
                            print("is_cl:", data['is_cl'])
                            print("LP token0:", data['token0']['symbol'], "address:", data['token0']['token_address'])
                            print("LP token1:", data['token1']['symbol'], "address:", data['token1']['token_address'])
                            print("TVL:", data['tvl'])
                            print("APR:", data['apr'])
                            print("volume:", data['volume'])
                            print("fee:", data['pool_fee'])
                            print("total fees:", data['total_fees'])

                        except json.JSONDecodeError:
                            print("Non-JSON response:", content.text)
               

                    print(f"📊 结果数量: {len(response.content)}")
                    
                except Exception as e:
                    print(f"❌ 调用工具 {tool_name} 失败: {e}")
                    print(f"详细错误信息: {traceback.format_exc()}")
                    continue



if __name__ == "__main__":
    asyncio.run(main())