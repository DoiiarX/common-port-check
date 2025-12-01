"""
端口检查核心功能

此模块提供端口检查的核心功能实现。
数据模型定义位置：
- src/models.py - 数据模型定义
- src/ports_data.py - 端口数据定义
"""

import platform
from typing import Optional, Set

from models import SystemType
from ports_data import get_ports_by_system


def detect_system() -> SystemType:
    """
    自动检测当前操作系统类型
    
    Returns:
        检测到的系统类型
    """
    system_name: str = platform.system().lower()
    
    if system_name == "windows":
        return SystemType.WINDOWS
    elif system_name == "linux":
        return SystemType.LINUX
    elif system_name == "darwin":
        return SystemType.MACOS
    else:
        # 其他Unix系统
        return SystemType.UNIX


def is_common_port(port: int, system: Optional[SystemType] = None) -> bool:
    """
    检查指定端口是否是系统的常用端口
    
    Args:
        port: 要检查的端口号
        system: 系统类型，如果为None则自动检测当前系统
        
    Returns:
        如果是常用端口返回True，否则返回False
        
    Raises:
        ValueError: 当端口号不在有效范围内（0-65535）时
    """
    if not (0 <= port <= 65535):
        raise ValueError(f"端口号必须在0-65535范围内，当前值: {port}")
    
    if system is None:
        system = detect_system()
    
    common_ports: Set[int] = get_ports_by_system(system)
    return port in common_ports


def get_common_ports(system: Optional[SystemType] = None) -> Set[int]:
    """
    获取指定系统的所有常用端口
    
    Args:
        system: 系统类型，如果为None则自动检测当前系统
        
    Returns:
        该系统的常用端口集合
    """
    if system is None:
        system = detect_system()
    
    return get_ports_by_system(system)

