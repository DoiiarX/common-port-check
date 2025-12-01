# common-port-check

专业的Python库，用于检查端口是否是系统的常用端口。

## 功能特性

- ✅ 检查某个端口是否是本系统的常用端口
- ✅ 指定系统检查是否是该系统的常用端口
- ✅ 检查常用软件（游戏、开发工具等）的常用端口
- ✅ 自动检测当前操作系统类型
- ✅ 支持Windows、Linux、macOS等主流操作系统
- ✅ 类型安全，使用Pydantic进行数据验证

## 安装

```bash
uv pip install git+https://github.com/DoiiarsX/common-port-check
```

或

```bash
uv pip install -e .
```

或者从源码安装：

```bash
git clone https://github.com/DoiiarsX/common-port-check.git
cd common-port-check
uv pip install -e .
```

## 使用方法

### 基本用法

```python
from common_port_check import is_common_port, SystemType

# 检查端口是否是当前系统的常用端口（自动检测系统）
result = is_common_port(3389)  # Windows RDP端口
print(result)  # 在Windows系统上返回True

# 指定系统类型检查
result = is_common_port(22, SystemType.LINUX)  # Linux SSH端口
print(result)  # 返回True

result = is_common_port(3389, SystemType.LINUX)  # Windows RDP端口在Linux上
print(result)  # 返回False

# 检查常用软件端口（跨平台）
result = is_common_port(27015, SystemType.COMMON_SOFTWARE)  # Steam游戏端口
print(result)  # 返回True

result = is_common_port(3659, SystemType.COMMON_SOFTWARE)  # EA Origin端口
print(result)  # 返回True
```

### 获取所有常用端口

```python
from common_port_check import get_common_ports, SystemType

# 获取当前系统的所有常用端口
ports = get_common_ports()
print(ports)

# 获取指定系统的所有常用端口
linux_ports = get_common_ports(SystemType.LINUX)
windows_ports = get_common_ports(SystemType.WINDOWS)
```

### 系统类型

```python
from common_port_check import SystemType

# 支持的系统类型
SystemType.WINDOWS        # Windows系统
SystemType.LINUX          # Linux系统
SystemType.MACOS          # macOS系统
SystemType.UNIX           # 通用Unix系统
SystemType.ALL            # 所有系统通用
SystemType.COMMON_SOFTWARE  # 常用软件端口（跨平台）
```

## 支持的常用端口

### Windows常用端口
- 135: RPC Endpoint Mapper
- 139: NetBIOS Session Service
- 445: Microsoft-DS (SMB)
- 1433: SQL Server
- 3389: Remote Desktop Protocol (RDP)
- 5985/5986: WinRM
- 49152-49157: Windows RPC动态端口

### Linux常用端口
- 22: SSH
- 80: HTTP
- 443: HTTPS
- 3306: MySQL
- 5432: PostgreSQL
- 6379: Redis
- 8080: HTTP Alternate

### macOS常用端口
- 22: SSH
- 548: AFP (Apple Filing Protocol)
- 631: IPP (Internet Printing Protocol)
- 3283: Apple Remote Desktop
- 5000: AirPlay / Flask开发框架
- 5353: mDNS/Bonjour
- 5900: VNC
- 7000: AirPlay发送器

### 常用软件端口（跨平台）
- **游戏平台**:
  - 27000-27037: Steam (游戏客户端和服务器)
  - 4380: Steam客户端
  - 3659: EA Origin / EA Games
  - 3724: World of Warcraft
  - 6112-6119: Battle.net / Blizzard
  - 7777: Epic Games Launcher
  - 9999: Epic Games Launcher
- **开发框架**:
  - 3000-3001: Node.js / React
  - 5000-5001: Flask / AirPlay
  - 8000-8001: Django等
  - 9000: SonarQube
  - 9090: Prometheus
- **其他**:
  - 6881-6889: BitTorrent
  - 30000-32767: Kubernetes NodePort范围

## 开发

### 运行测试

```bash
uv pip install -r requirements-dev.txt
pytest
```

### 代码规范

- Python 3.11+
- 使用Pydantic进行数据验证
- 遵循PEP 257注释规范
- 类型注解完整

## 许可证

MIT License

