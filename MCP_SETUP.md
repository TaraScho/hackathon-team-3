# MCP Server Setup Guide

This project uses Model Context Protocol (MCP) servers to extend Claude Code's capabilities with specialized tools and integrations. This guide explains how to set up the required prerequisites and configure the MCP servers.

## Configured MCP Servers

The `.mcp.json` file in this project includes the following MCP servers:

1. **Datadog MCP** - Observability and monitoring tools
2. **Playwright MCP** - Browser automation and testing
3. **Terraform MCP** - Infrastructure as code management

## Prerequisites

### Required for All MCPs

- **Claude Code CLI** - Ensure you have Claude Code installed and configured
- **Git** - For version control (already installed based on project setup)

### Datadog MCP

**Type:** HTTP
**Prerequisites:** None - connects to Datadog's hosted MCP server

**Optional Setup:**
- Datadog account and API credentials may be required for full functionality
- Set environment variables if needed:
  ```bash
  export DD_API_KEY=your_api_key
  export DD_APP_KEY=your_app_key
  export DD_SITE=datadoghq.com  # or your specific Datadog site
  ```

### Playwright MCP

**Type:** stdio (Node.js)
**Prerequisites:**
- **Node.js** (v18 or later recommended)
- **npm** (comes with Node.js)

**Installation:**

1. Install Node.js if not already installed:
   ```bash
   # macOS (using Homebrew)
   brew install node

   # Ubuntu/Debian
   sudo apt update
   sudo apt install nodejs npm

   # Windows (using winget)
   winget install OpenJS.NodeJS
   ```

2. Verify installation:
   ```bash
   node --version
   npm --version
   ```

The Playwright MCP will automatically download when first used via `npx @playwright/mcp@latest`.

### Terraform MCP

**Type:** stdio (Docker)
**Prerequisites:**
- **Docker** (required - the MCP runs in a Docker container)

**Installation:**

1. Install Docker Desktop:

   **macOS:**
   ```bash
   # Using Homebrew
   brew install --cask docker

   # Or download from https://www.docker.com/products/docker-desktop
   ```

   **Linux:**
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER

   # Log out and back in for group changes to take effect
   ```

   **Windows:**
   - Download and install Docker Desktop from https://www.docker.com/products/docker-desktop

2. Verify Docker installation:
   ```bash
   docker --version
   docker run hello-world
   ```

3. Ensure Docker daemon is running:
   ```bash
   # macOS/Linux
   docker ps

   # If you see a list of containers (even if empty), Docker is running
   ```

4. Pull the Terraform MCP image (optional, will happen automatically on first use):
   ```bash
   docker pull hashicorp/terraform-mcp-server
   ```

**Optional Configuration:**

To use HCP Terraform/Terraform Enterprise features, set your token:
```bash
export TFE_TOKEN=your_terraform_token
```

To enable enterprise tools, configure in your Claude Code settings or environment.

## Verifying MCP Configuration

After ensuring prerequisites are installed, verify your MCP configuration:

1. Check that `.mcp.json` exists in the project root
2. Ensure the file is properly formatted (JSON)
3. Start Claude Code in this project directory

You can test each MCP by asking Claude to use their respective features:
- Datadog: "Search for error logs in Datadog"
- Playwright: "Take a screenshot of example.com"
- Terraform: "Get the latest version of the AWS provider"

## Troubleshooting

### General Issues

**MCP server not connecting:**
- Ensure all prerequisites for that MCP are installed
- Check that the `.mcp.json` file is in the project root
- Restart Claude Code after installing prerequisites

### Datadog MCP

**Connection errors:**
- Check your internet connection
- Verify Datadog API credentials if using authenticated features

### Playwright MCP

**npx command not found:**
- Install Node.js and npm
- Verify `npm` is in your PATH: `which npm` or `where npm`

**Playwright browser not installed:**
- Claude will prompt to install browsers when needed
- Manually install: `npx playwright install`

### Terraform MCP

**Docker command not found:**
- Install Docker Desktop for your platform
- Ensure Docker is in your PATH

**Docker daemon not running:**
- Start Docker Desktop application
- On Linux: `sudo systemctl start docker`

**Permission denied (Linux):**
- Add your user to docker group: `sudo usermod -aG docker $USER`
- Log out and back in
- Test: `docker run hello-world`

**Container fails to start:**
- Check Docker logs: `docker logs <container-id>`
- Ensure sufficient disk space
- Try pulling the image manually: `docker pull hashicorp/terraform-mcp-server`

## Environment Variables

Some MCP servers may require environment variables. You can set them:

**In your shell:**
```bash
export DD_API_KEY=your_key
export TFE_TOKEN=your_token
```

**Or in `.mcp.json` (not recommended for secrets):**
```json
{
  "mcpServers": {
    "terraform": {
      "type": "stdio",
      "command": "docker",
      "args": ["run", "-i", "--rm", "hashicorp/terraform-mcp-server"],
      "env": {
        "TFE_TOKEN": "your_token"
      }
    }
  }
}
```

**Best practice:** Use environment variables from your shell rather than hardcoding in `.mcp.json`.

## Additional Resources

- [Claude Code Documentation](https://github.com/anthropics/claude-code)
- [MCP Specification](https://modelcontextprotocol.io)
- [Datadog MCP Docs](https://docs.datadoghq.com/bits_ai/mcp_server/setup/)
- [Playwright MCP](https://github.com/microsoft/playwright-mcp)
- [Terraform MCP](https://github.com/hashicorp/terraform-mcp-server)

## Need Help?

If you encounter issues not covered in this guide:
1. Check the specific MCP server's documentation
2. Verify all prerequisites are correctly installed
3. Check Claude Code logs for error messages
4. Report issues at https://github.com/anthropics/claude-code/issues
