"""
端口检查功能测试

此模块测试端口检查的核心功能。
数据模型定义位置：
- src/models.py - 数据模型定义
"""

import pytest

import sys
import os
from pathlib import Path

project_root = Path(__file__).parent.parent / "src"
sys.path.append(str(project_root))

from checker import is_common_port, get_common_ports
from models import SystemType


class TestIsCommonPort:
    """测试is_common_port函数"""
    
    def test_windows_common_port(self):
        """测试Windows常用端口"""
        assert is_common_port(3389, SystemType.WINDOWS) is True
        assert is_common_port(445, SystemType.WINDOWS) is True
        assert is_common_port(135, SystemType.WINDOWS) is True
    
    def test_linux_common_port(self):
        """测试Linux常用端口"""
        assert is_common_port(22, SystemType.LINUX) is True
        assert is_common_port(80, SystemType.LINUX) is True
        assert is_common_port(443, SystemType.LINUX) is True
    
    def test_macos_common_port(self):
        """测试macOS常用端口"""
        assert is_common_port(548, SystemType.MACOS) is True
        assert is_common_port(631, SystemType.MACOS) is True
        assert is_common_port(5000, SystemType.MACOS) is True  # AirPlay/开发框架
        assert is_common_port(5353, SystemType.MACOS) is True  # mDNS/Bonjour
        assert is_common_port(7000, SystemType.MACOS) is True  # AirPlay
        assert is_common_port(22, SystemType.MACOS) is True  # SSH
        assert is_common_port(53, SystemType.MACOS) is True  # DNS
    
    def test_common_software_port(self):
        """测试常用软件端口"""
        # Steam端口
        assert is_common_port(27015, SystemType.COMMON_SOFTWARE) is True
        assert is_common_port(27016, SystemType.COMMON_SOFTWARE) is True
        assert is_common_port(4380, SystemType.COMMON_SOFTWARE) is True
        # EA Origin端口
        assert is_common_port(3659, SystemType.COMMON_SOFTWARE) is True
        # Battle.net端口
        assert is_common_port(6112, SystemType.COMMON_SOFTWARE) is True
        # Epic Games端口
        assert is_common_port(7777, SystemType.COMMON_SOFTWARE) is True
        # 开发框架端口
        assert is_common_port(3000, SystemType.COMMON_SOFTWARE) is True
        assert is_common_port(5000, SystemType.COMMON_SOFTWARE) is True
        assert is_common_port(8000, SystemType.COMMON_SOFTWARE) is True
        # BitTorrent端口
        assert is_common_port(6881, SystemType.COMMON_SOFTWARE) is True
    
    def test_non_common_port(self):
        """测试非常用端口"""
        assert is_common_port(9999, SystemType.WINDOWS) is False
        assert is_common_port(9999, SystemType.LINUX) is False
        assert is_common_port(9999, SystemType.MACOS) is False
    
    def test_cross_system_port(self):
        """测试跨系统端口检查"""
        # Windows RDP端口在Linux上不是常用端口
        assert is_common_port(3389, SystemType.LINUX) is False
        # Linux SSH端口在Windows上不是常用端口
        assert is_common_port(22, SystemType.WINDOWS) is False
    
    def test_invalid_port_range(self):
        """测试无效端口范围"""
        with pytest.raises(ValueError):
            is_common_port(-1, SystemType.WINDOWS)
        
        with pytest.raises(ValueError):
            is_common_port(65536, SystemType.LINUX)
    
    def test_auto_detect_system(self):
        """测试自动检测系统"""
        # 这个测试依赖于运行环境，所以只测试函数能正常调用
        result = is_common_port(80)  # HTTP端口，大多数系统都有
        assert isinstance(result, bool)


class TestGetCommonPorts:
    """测试get_common_ports函数"""
    
    def test_get_windows_ports(self):
        """测试获取Windows常用端口"""
        ports = get_common_ports(SystemType.WINDOWS)
        assert isinstance(ports, set)
        assert 3389 in ports
        assert 445 in ports
        assert 135 in ports
    
    def test_get_linux_ports(self):
        """测试获取Linux常用端口"""
        ports = get_common_ports(SystemType.LINUX)
        assert isinstance(ports, set)
        assert 22 in ports
        assert 80 in ports
        assert 443 in ports
    
    def test_get_macos_ports(self):
        """测试获取macOS常用端口"""
        ports = get_common_ports(SystemType.MACOS)
        assert isinstance(ports, set)
        assert 548 in ports
        assert 631 in ports
        assert 5000 in ports  # AirPlay/开发框架
        assert 5353 in ports  # mDNS/Bonjour
        assert 7000 in ports  # AirPlay
        assert 22 in ports  # SSH
        assert 53 in ports  # DNS
    
    def test_get_common_software_ports(self):
        """测试获取常用软件端口"""
        ports = get_common_ports(SystemType.COMMON_SOFTWARE)
        assert isinstance(ports, set)
        assert 27015 in ports  # Steam
        assert 3659 in ports  # EA Origin
        assert 6112 in ports  # Battle.net
        assert 7777 in ports  # Epic Games
        assert 3000 in ports  # 开发框架
        assert 5000 in ports  # Flask
        assert 8000 in ports  # Django
        assert 6881 in ports  # BitTorrent
    
    def test_get_all_systems_ports(self):
        """测试获取所有系统通用端口"""
        ports = get_common_ports(SystemType.ALL)
        assert isinstance(ports, set)
        assert 80 in ports
        assert 443 in ports
    
    def test_auto_detect_system_ports(self):
        """测试自动检测系统并获取端口"""
        ports = get_common_ports()
        assert isinstance(ports, set)
        assert len(ports) > 0

