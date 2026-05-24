import asyncio
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "app", "agents"))

from tool_definitions import get_tools_for_agent_oneshot

async def main():
    print("Connecting to MCP server for 'cora'...")
    try:
        tools = await asyncio.wait_for(
            get_tools_for_agent_oneshot("cora"),
            timeout=30
        )
        print(f"SUCCESS: got {len(tools)} tools")
    except asyncio.TimeoutError:
        print("TIMEOUT: MCP server connection hung (>30s)")
    except Exception as e:
        print(f"ERROR: {type(e).__name__}: {e}")

asyncio.run(main())