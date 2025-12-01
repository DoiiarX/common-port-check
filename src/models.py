"""
数据模型定义

此模块定义端口检查相关的数据模型。
数据模型定义位置：
- src/models.py - 数据模型定义
"""

from enum import Enum
from typing import Set


class SystemType(str, Enum):
    """系统类型枚举"""
    
    WINDOWS = "windows"
    LINUX = "linux"
    MACOS = "macos"
    UNIX = "unix"  # 通用Unix系统
    ALL = "all"  # 所有系统
    COMMON_SOFTWARE = "common_software"  # 常用软件端口（跨平台）


class PortInfo:
    """端口信息类"""
    
    def __init__(self, port: int, description: str, system: SystemType):
        """
        初始化端口信息
        
        Args:
            port: 端口号
            description: 端口描述
            system: 所属系统类型
        """
        self.port: int = port
        self.description: str = description
        self.system: SystemType = system
    
    def __repr__(self) -> str:
        return f"PortInfo(port={self.port}, description='{self.description}', system={self.system.value})"

