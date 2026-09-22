from fastapi import FastAPI
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

app = FastAPI()

@app.get("/")
def home():
    return {
        "status": "Simple Text MCP HTTP running"
    }

app.mount("/mcp", mcp.streamable_http_app())
