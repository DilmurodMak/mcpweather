# MCP Weather Server

A weather application demonstrating the Model Context Protocol (MCP) using FastMCP framework.

## What is MCP (Model Context Protocol)?

**Model Context Protocol (MCP)** is an open standard that enables AI assistants to securely connect to external data sources and tools. Think of it as a universal "plugin system" for AI models that allows them to:

- **Access Real-time Data**: Connect to databases, APIs, and live systems
- **Execute Actions**: Perform operations like file management, system commands, or API calls
- **Maintain Security**: Controlled access with proper authentication and permissions
- **Stay Updated**: Always work with the latest information rather than static training data

MCP bridges the gap between AI models and the real world by providing a standardized way for models to interact with external systems while maintaining security and reliability.

### Key Benefits of MCP:
- **Standardized Interface**: Consistent protocol across different tools and services
- **Security First**: Built-in authentication and permission controls
- **Real-time Access**: Live data instead of stale training information
- **Extensible**: Easy to add new tools and data sources
- **Cross-platform**: Works across different AI models and platforms

## What is FastMCP?

**FastMCP** is a Python framework that simplifies building MCP servers. It's designed to make creating MCP-compliant servers as easy as building a REST API with FastAPI.

### Key Features:
- **Decorator-based**: Simple `@mcp.tool()` decorators to expose functions
- **Type Safety**: Full TypeScript-like type hints and validation
- **Automatic Documentation**: Self-documenting APIs with schema generation
- **Built-in Server**: Ready-to-use server implementation
- **Development Tools**: Hot reloading and debugging support

## Why Use FastMCP vs Core Python MCP SDK?

| Feature | FastMCP | Core MCP SDK |
|---------|---------|--------------|
| **Ease of Use** | ✅ Simple decorators, minimal boilerplate | ❌ More verbose, manual setup required |
| **Development Speed** | ✅ Rapid prototyping and development | ⚠️ Slower initial setup |
| **Type Safety** | ✅ Built-in validation and type checking | ⚠️ Manual type validation needed |
| **Documentation** | ✅ Auto-generated from code | ❌ Manual documentation required |
| **Learning Curve** | ✅ Familiar FastAPI-like syntax | ❌ Steeper learning curve |
| **Flexibility** | ⚠️ Some conventions enforced | ✅ Full control over implementation |
| **Performance** | ✅ Optimized for common use cases | ✅ Can be optimized for specific needs |

### When to Choose FastMCP:
- 🚀 **Rapid Development**: Need to get a server up quickly
- 🔰 **Learning MCP**: First time building MCP servers
- 🛠️ **Standard Use Cases**: Common patterns like API wrappers, data access
- 👥 **Team Development**: Want consistent, maintainable code

### When to Choose Core SDK:
- 🎯 **Specific Requirements**: Need custom protocol handling
- ⚡ **Performance Critical**: Require maximum optimization
- 🔧 **Advanced Features**: Need low-level protocol control
- 🏗️ **Custom Architecture**: Building complex, multi-component systems

## Current Weather API Example

This repository demonstrates a weather MCP server built with FastMCP that provides real-time weather information.

### Features

- **Weather Lookup**: Get current weather for any location
- **Location-based**: Smart location parsing and validation
- **Error Handling**: Graceful handling of invalid locations or API failures
- **Type Safe**: Full type validation for inputs and outputs

### Implementation

The weather server exposes a single tool:

```python
@mcp.tool()
def get_weather_info(location: str) -> str:
    """
    Get Weather information for a given location.
    
    Args:
        location (str): The location for which to get the weather information.
                       The location needs to be a proper city name like London, Tokyo etc.
    """
```

### Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/MCP_WEATHER.git
   cd MCP_WEATHER
   ```
2. **Create a Virtual Environment**:
   ```bash
   uv venv weather_mcp_env
   source weather_mcp_env/bin/activate
   ```  

3. **Install Dependencies**:
   ```bash
   uv sync or uv pip install -r requirements.txt
   ```
4. **Configuration**:

.vscode/mcp.json
```json
{
  "mcpServers": {
    "weather": {
      "command": "path/to/python",
      "args": ["path/to/weather_server.py"]
    }
  }
}
```

Open the vscode chat agent mode and ask a weather question 

```
what is the weather in Jersey City?
```

you should see the agent using the MCP server to get the weather information.