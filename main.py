from pathlib import Path

from am.mcp.install import install as install_am
from ow.mcp.install import install as install_ow
from tc.mcp.install import install as install_tc


def main():
    print("Installing MCP Servers")
    path = Path(__file__).parent
    install_am(path, client="claude-code")
    install_ow(path, client="claude-code")
    install_tc(path, client="claude-code")


if __name__ == "__main__":
    main()

