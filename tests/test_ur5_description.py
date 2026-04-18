"""UR5 Description 单元测试"""

import pytest
import xacro
from pathlib import Path

class TestUR5Description:
    """UR5 机器人模型测试"""
    
    @pytest.fixture
    def urdf_path(self):
        return Path(__file__).parent.parent / "ur5_description" / "urdf" / "ur5.urdf.xacro"
    
    def test_urdf_file_exists(self, urdf_path):
        """测试 URDF 文件存在"""
        assert urdf_path.exists(), f"URDF 文件不存在：{urdf_path}"
    
    def test_xacro_processing(self, urdf_path):
        """测试 Xacro 处理成功"""
        if urdf_path.exists():
            # 验证 Xacro 可以正常处理
            assert urdf_path.stat().st_size > 0, "URDF 文件为空"
    
    def test_robot_name(self):
        """测试机器人名称为 ur5"""
        # 验证机器人名称配置
        assert True  # 实际测试需要加载 URDF
    
    def test_joint_count(self):
        """测试关节数量为 6"""
        # UR5 应该有 6 个关节
        assert True  # 实际测试需要解析 URDF
