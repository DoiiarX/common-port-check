"""
端口数据定义

此模块定义各操作系统的常用端口列表。
数据模型定义位置：
- src/models.py - 数据模型定义
"""

from typing import Dict, Set

from models import SystemType


# Windows常用端口
WINDOWS_COMMON_PORTS: Set[int] = {
    135,   # RPC Endpoint Mapper
    139,   # NetBIOS Session Service
    445,   # Microsoft-DS (SMB)
    1433,  # SQL Server
    1434,  # SQL Server Browser
    3389,  # Remote Desktop Protocol (RDP)
    5985,  # WinRM HTTP
    5986,  # WinRM HTTPS
    49152, # Windows RPC动态端口起始
    49153,
    49154,
    49155,
    49156,
    49157,
}

# Linux常用端口
LINUX_COMMON_PORTS: Set[int] = {
    22,    # SSH
    23,    # Telnet
    25,    # SMTP
    53,    # DNS
    80,    # HTTP
    110,   # POP3
    143,   # IMAP
    443,   # HTTPS
    3306,  # MySQL
    5432,  # PostgreSQL
    6379,  # Redis
    8080,  # HTTP Alternate
    8443,  # HTTPS Alternate
    9000,  # SonarQube / 其他服务
}

# macOS常用端口
MACOS_COMMON_PORTS: Set[int] = {
    22,    # SSH
    25,    # SMTP
    53,    # DNS
    80,    # HTTP
    88,    # Kerberos
    443,   # HTTPS
    548,   # AFP (Apple Filing Protocol)
    631,   # IPP (Internet Printing Protocol)
    3283,  # Apple Remote Desktop
    5000,  # AirPlay 接收器 / Flask 等开发框架默认端口
    5353,  # mDNS/Bonjour 服务发现
    5900,  # VNC (Screen Sharing)
    7000,  # AirPlay 发送器
    8080,  # HTTP Alternate
    1024,  # macOS 动态端口起始范围
    1025,
    1026,
    1027,
    1028,
    1029,
    1030,
    1031,
    1032,
    1033,
    1034,
    1035,
}

# Unix通用常用端口（Linux和macOS都常用）
UNIX_COMMON_PORTS: Set[int] = {
    22,    # SSH
    23,    # Telnet
    25,    # SMTP
    53,    # DNS
    80,    # HTTP
    110,   # POP3
    143,   # IMAP
    443,   # HTTPS
    3306,  # MySQL
    5432,  # PostgreSQL
    8080,  # HTTP Alternate
}

# 所有系统通用端口
ALL_SYSTEMS_COMMON_PORTS: Set[int] = {
    80,    # HTTP
    443,   # HTTPS
    8080,  # HTTP Alternate
    8443,  # HTTPS Alternate
}

# 常用软件端口（跨平台）
COMMON_SOFTWARE_PORTS: Set[int] = {
    # 游戏平台
    27000,  # Steam (UDP 游戏客户端)
    27015,  # Steam (TCP/UDP 游戏服务器)
    27016,  # Steam (TCP/UDP 游戏服务器)
    27017,  # Steam (TCP/UDP 游戏服务器) / MongoDB
    27018,  # Steam (TCP/UDP 游戏服务器)
    27019,  # Steam (TCP/UDP 游戏服务器)
    27020,  # Steam (TCP/UDP 游戏服务器)
    27021,  # Steam (TCP/UDP 游戏服务器)
    27022,  # Steam (TCP/UDP 游戏服务器)
    27023,  # Steam (TCP/UDP 游戏服务器)
    27024,  # Steam (TCP/UDP 游戏服务器)
    27025,  # Steam (TCP/UDP 游戏服务器)
    27026,  # Steam (TCP/UDP 游戏服务器)
    27027,  # Steam (TCP/UDP 游戏服务器)
    27028,  # Steam (TCP/UDP 游戏服务器)
    27029,  # Steam (TCP/UDP 游戏服务器)
    27030,  # Steam (TCP/UDP 游戏服务器)
    27031,  # Steam (UDP 客户端)
    27036,  # Steam (TCP 客户端)
    27037,  # Steam (TCP 客户端)
    4380,   # Steam (UDP 客户端)
    3659,   # EA Origin / EA Games
    3724,   # World of Warcraft
    6112,   # Battle.net / Blizzard
    6113,   # Battle.net / Blizzard
    6114,   # Battle.net / Blizzard
    6115,   # Battle.net / Blizzard
    6116,   # Battle.net / Blizzard
    6117,   # Battle.net / Blizzard
    6118,   # Battle.net / Blizzard
    6119,   # Battle.net / Blizzard
    6881,   # BitTorrent
    6882,   # BitTorrent
    6883,   # BitTorrent
    6884,   # BitTorrent
    6885,   # BitTorrent
    6886,   # BitTorrent
    6887,   # BitTorrent
    6888,   # BitTorrent
    6889,   # BitTorrent
    7777,   # Epic Games Launcher / Unreal Tournament
    9999,   # Epic Games Launcher
    3000,   # 开发框架 (Node.js, React等)
    3001,   # 开发框架备用端口
    5000,   # Flask / AirPlay接收器
    5001,   # 开发框架备用端口
    8000,   # 开发框架 (Django等)
    8001,   # 开发框架备用端口
    9000,   # SonarQube / 其他服务
    9090,   # Prometheus / 其他服务
    30000,  # Kubernetes NodePort 范围起始
    30001,
    30002,
    30003,
    30004,
    30005,
    30006,
    30007,
    30008,
    30009,
    30010,
    32767,  # Kubernetes NodePort 范围结束
    # 文件同步和下载工具
    8384,   # Syncthing Web UI
    22000,  # Syncthing 文件同步
    # AI和开发工具
    11434,  # Ollama AI服务
    # 媒体服务器
    8096,   # Jellyfin 媒体服务器
    # 远程桌面和游戏串流
    47984,  # Moonlight 游戏串流 (TCP)
    47989,  # Moonlight 游戏串流 (UDP)
    47998,  # Moonlight 游戏串流 (UDP)
    47999,  # Moonlight 游戏串流 (UDP)
    48000,  # Moonlight 游戏串流 (UDP)
    8000,   # Parsec 远程桌面 (备用)
    8001,   # Parsec 远程桌面 (备用)
    5900,   # Parsec VNC (备用)
    # 密码管理器
    8080,   # 常用web 本地服务 (如果启用)
    # 下载工具 (已在BitTorrent部分包含6881-6889)
    # Discord 主要使用443和动态端口，不添加固定端口
}


def get_ports_by_system(system: SystemType) -> Set[int]:
    """
    根据系统类型获取常用端口集合
    
    Args:
        system: 系统类型
        
    Returns:
        该系统的常用端口集合
    """
    port_map: Dict[SystemType, Set[int]] = {
        SystemType.WINDOWS: WINDOWS_COMMON_PORTS,
        SystemType.LINUX: LINUX_COMMON_PORTS,
        SystemType.MACOS: MACOS_COMMON_PORTS,
        SystemType.UNIX: UNIX_COMMON_PORTS,
        SystemType.ALL: ALL_SYSTEMS_COMMON_PORTS,
        SystemType.COMMON_SOFTWARE: COMMON_SOFTWARE_PORTS,
    }
    
    return port_map.get(system, set())

