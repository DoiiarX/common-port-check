"""
common_port_check - 专业的端口常用端口检查库

此模块提供检查端口是否是系统常用端口的功能。
数据模型定义位置：
- src/common_port_check/models.py - 数据模型定义
- src/common_port_check/ports_data.py - 端口数据定义
"""

from .checker import is_common_port, get_common_ports
from .models import SystemType

__all__ = [
    "is_common_port",
    "get_common_ports",
    "SystemType",
]

__version__ = "0.1.0"

