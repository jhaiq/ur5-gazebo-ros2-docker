#!/bin/bash
# 运行所有测试

set -e

echo "=== 运行 UR5 测试套件 ==="

# 运行单元测试
echo "运行单元测试..."
cd $(dirname "$0")
python3 -m pytest -v --tb=short

echo "=== 测试完成 ==="
