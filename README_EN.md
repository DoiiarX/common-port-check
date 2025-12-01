[中文](README.md) | [English]

# common-port-check

A professional Python library for checking if a port is a common port for the system.

## Features

- ✅ Check if a port is a common port for the current system
- ✅ Check if a port is a common port for a specified system
- ✅ Check common ports for popular software (games, development tools, etc.)
- ✅ Automatically detect the current operating system type
- ✅ Support for Windows, Linux, macOS and other mainstream operating systems
- ✅ Type-safe with Pydantic data validation

## Installation

```bash
uv pip install git+https://github.com/DoiiarX/common-port-check
```

Or

```bash
uv pip install -e .
```

Or install from source:

```bash
git clone https://github.com/DoiiarX/common-port-check.git
cd common-port-check
uv pip install -e .
```

## Usage

### Basic Usage

```python
from common_port_check import is_common_port, SystemType

# Check if a port is a common port for the current system (auto-detect)
result = is_common_port(3389)  # Windows RDP port
print(result)  # Returns True on Windows systems

# Check for a specific system type
result = is_common_port(22, SystemType.LINUX)  # Linux SSH port
print(result)  # Returns True

result = is_common_port(3389, SystemType.LINUX)  # Windows RDP port on Linux
print(result)  # Returns False

# Check common software ports (cross-platform)
result = is_common_port(27015, SystemType.COMMON_SOFTWARE)  # Steam game port
print(result)  # Returns True

result = is_common_port(3659, SystemType.COMMON_SOFTWARE)  # EA Origin port
print(result)  # Returns True
```

### Get All Common Ports

```python
from common_port_check import get_common_ports, SystemType

# Get all common ports for the current system
ports = get_common_ports()
print(ports)

# Get all common ports for a specific system
linux_ports = get_common_ports(SystemType.LINUX)
windows_ports = get_common_ports(SystemType.WINDOWS)
```

### System Types

```python
from common_port_check import SystemType

# Supported system types
SystemType.WINDOWS        # Windows system
SystemType.LINUX          # Linux system
SystemType.MACOS          # macOS system
SystemType.UNIX           # Generic Unix system
SystemType.ALL            # All systems common
SystemType.COMMON_SOFTWARE  # Common software ports (cross-platform)
```

## Supported Common Ports

### Windows Common Ports
- 135: RPC Endpoint Mapper
- 139: NetBIOS Session Service
- 445: Microsoft-DS (SMB)
- 1433: SQL Server
- 3389: Remote Desktop Protocol (RDP)
- 5985/5986: WinRM
- 49152-49157: Windows RPC dynamic ports

### Linux Common Ports
- 22: SSH
- 80: HTTP
- 443: HTTPS
- 3306: MySQL
- 5432: PostgreSQL
- 6379: Redis
- 8080: HTTP Alternate

### macOS Common Ports
- 22: SSH
- 548: AFP (Apple Filing Protocol)
- 631: IPP (Internet Printing Protocol)
- 3283: Apple Remote Desktop
- 5000: AirPlay / Flask development framework
- 5353: mDNS/Bonjour
- 5900: VNC
- 7000: AirPlay sender

### Common Software Ports (Cross-platform)
- **Gaming Platforms**:
  - 27000-27037: Steam (game client and server)
  - 4380: Steam client
  - 3659: EA Origin / EA Games
  - 3724: World of Warcraft
  - 6112-6119: Battle.net / Blizzard
  - 7777: Epic Games Launcher
  - 9999: Epic Games Launcher
- **Development Frameworks**:
  - 3000-3001: Node.js / React
  - 5000-5001: Flask / AirPlay
  - 8000-8001: Django, etc.
  - 9000: SonarQube
  - 9090: Prometheus
- **File Sync and Download Tools**:
  - 6881-6889: BitTorrent / Aria2
  - 8384: Syncthing Web UI
  - 22000: Syncthing file sync
- **AI and Development Tools**:
  - 11434: Ollama AI service
- **Media Servers**:
  - 8096: Jellyfin media server
- **Remote Desktop and Game Streaming**:
  - 47984: Moonlight game streaming (TCP)
  - 47989-48000: Moonlight game streaming (UDP)
  - 8000-8001: Parsec remote desktop
  - 5900: Parsec VNC
- **Others**:
  - 30000-32767: Kubernetes NodePort range
  - 8080: Common web local services

## Development

### Running Tests

```bash
uv pip install -r requirements-dev.txt
pytest
```

### Code Standards

- Python 3.11+
- Uses Pydantic for data validation
- Follows PEP 257 docstring conventions
- Complete type annotations

## License

MIT License

