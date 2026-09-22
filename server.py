from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "Simple Text MCP HTTP",
    stateless_http=True
)

@mcp.tool()
def echo_text(text: str) -> dict:
    return {
        "text": text
    }

app = mcp.streamable_http_app()
