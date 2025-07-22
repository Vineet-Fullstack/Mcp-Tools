# Mcp-Tools

## Configuring MCP Servers in VS Code

To configure MCP servers in VS Code, add the following configuration to your settings (e.g., in `.vscode/settings.json`):

```json
"mcp": {
  "servers": {
    "local-mcp": {
      "command": "python",
      "args": ["C:\\Workspace\\Projects\\mcp server 1\\calculator.py"]
    },
    "time-tool": {
      "command": "python",
      "args": ["C:\\Workspace\\Projects\\mcp server 1\\time_tool.py"]
    },
    "json-tool": {
      "command": "python",
      "args": ["C:\\Workspace\\Projects\\mcp server 1\\joke_tool.py"]
    }
  }
}
```

> **Note:** The path (e.g., `C:\Workspace\Projects\mcp server 1\`) will vary depending on each developer's local setup. Update the configuration to match the location of your MCP server scripts on your machine.

### Example for Local Running

This configuration allows you to run MCP tools locally by specifying the Python command and the path to each tool script. Make sure the paths are correct and point to your MCP tool scripts.

For more details, see the documentation in the `docs/` folder.