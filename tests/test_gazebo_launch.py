"""Gazebo 启动集成测试"""

import pytest
import subprocess
import time

class TestGazeboLaunch:
    """Gazebo 仿真启动测试"""
    
    def test_gazebo_config_exists(self):
        """测试 Gazebo 配置文件存在"""
        from pathlib import Path
        gazebo_path = Path(__file__).parent.parent / "ur5_gazebo" / "worlds"
        assert gazebo_path.exists(), f"Gazebo 配置目录不存在：{gazebo_path}"
    
    def test_world_file_exists(self):
        """测试世界文件存在"""
        from pathlib import Path
        world_file = Path(__file__).parent.parent / "ur5_gazebo" / "worlds" / "ur5_world.world"
        assert world_file.exists(), f"世界文件不存在：{world_file}"
