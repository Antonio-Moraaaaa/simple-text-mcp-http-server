from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Simple Text MCP HTTP")

@mcp.tool()
def echo_text(text: str) -> dict:
    """
    Return the submitted text.
    """
    return {"text": text}


app = FastAPI()


@app.get("/")
def home():
    return {
        "status": "Simple Text MCP HTTP running"
    }


# MCP Streamable HTTP endpoint
app.mount("/mcp", mcp.streamable_http_app())