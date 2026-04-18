"""MoveIt2 配置测试"""

import pytest
from pathlib import Path

class TestMoveItConfig:
    """MoveIt2 配置测试"""
    
    def test_srdf_exists(self):
        """测试 SRDF 文件存在"""
        srdf_path = Path(__file__).parent.parent / "ur5_moveit_config" / "config" / "ur5.srdf"
        assert srdf_path.exists(), f"SRDF 文件不存在：{srdf_path}"
    
    def test_kinematics_yaml_exists(self):
        """测试运动学配置文件存在"""
        kinematics_path = Path(__file__).parent.parent / "ur5_moveit_config" / "config" / "kinematics.yaml"
        assert kinematics_path.exists(), f"运动学配置文件不存在：{kinematics_path}"
    
    def test_joint_limits_yaml_exists(self):
        """测试关节限位文件存在"""
        joint_limits_path = Path(__file__).parent.parent / "ur5_moveit_config" / "config" / "joint_limits.yaml"
        assert joint_limits_path.exists(), f"关节限位文件不存在：{joint_limits_path}"
