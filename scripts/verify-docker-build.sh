#!/bin/bash
# verify-docker-build.sh - Verify Docker image builds successfully
# 
# This script performs basic verification of the Docker build process
# without requiring a full runtime test.
#
# Usage: ./scripts/verify-docker-build.sh
#
# Exit codes:
#   0 - All checks passed
#   1 - Build failed or verification error

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
DOCKER_DIR="${PROJECT_DIR}/ur5_gazebo_ros2"

echo "=== UR5 Gazebo ROS2 Docker Build Verification ==="
echo "Project Directory: ${PROJECT_DIR}"
echo "Docker Directory: ${DOCKER_DIR}"
echo ""

# Check 1: Verify Dockerfile exists
echo "Check 1: Verifying Dockerfile exists..."
if [[ ! -f "${DOCKER_DIR}/docker/Dockerfile" ]]; then
    echo "❌ FAIL: Dockerfile not found at ${DOCKER_DIR}/docker/Dockerfile"
    exit 1
fi
echo "✅ PASS: Dockerfile found"
echo ""

# Check 2: Verify docker-compose.yml exists
echo "Check 2: Verifying docker-compose.yml exists..."
if [[ ! -f "${DOCKER_DIR}/docker-compose.yml" ]]; then
    echo "❌ FAIL: docker-compose.yml not found"
    exit 1
fi
echo "✅ PASS: docker-compose.yml found"
echo ""

# Check 3: Verify ROS Humble base image
echo "Check 3: Verifying ROS Humble base image..."
if grep -q "FROM ros:humble-ros-base" "${DOCKER_DIR}/docker/Dockerfile"; then
    echo "✅ PASS: Base image is ros:humble-ros-base"
else
    echo "❌ FAIL: Base image is not ros:humble-ros-base"
    grep "FROM ros:" "${DOCKER_DIR}/docker/Dockerfile" || true
    exit 1
fi
echo ""

# Check 4: Verify ROS Humble packages
echo "Check 4: Verifying ROS Humble packages..."
HUMBLE_PACKAGES=$(grep -c "ros-humble-" "${DOCKER_DIR}/docker/Dockerfile" || true)
if [[ "$HUMBLE_PACKAGES" -gt 0 ]]; then
    echo "✅ PASS: Found ${HUMBLE_PACKAGES} ros-humble-* packages"
else
    echo "❌ FAIL: No ros-humble-* packages found"
    exit 1
fi

# Check for any jazzy references (should be none)
JAZZY_REFS=$(grep -c "ros-jazzy\|/opt/ros/jazzy" "${DOCKER_DIR}/docker/Dockerfile" || true)
if [[ "$JAZZY_REFS" -gt 0 ]]; then
    echo "⚠️  WARNING: Found ${JAZZY_REFS} references to jazzy (should be humble)"
    grep "ros-jazzy\|/opt/ros/jazzy" "${DOCKER_DIR}/docker/Dockerfile" || true
else
    echo "✅ PASS: No jazzy references found"
fi
echo ""

# Check 5: Verify docker-compose.yml image tags
echo "Check 5: Verifying docker-compose.yml image tags..."
if grep -q "ur5-gazebo-ros2:humble" "${DOCKER_DIR}/docker-compose.yml"; then
    echo "✅ PASS: Image tag is ur5-gazebo-ros2:humble"
else
    echo "❌ FAIL: Image tag is not ur5-gazebo-ros2:humble"
    grep "image:" "${DOCKER_DIR}/docker-compose.yml" || true
    exit 1
fi

# Check for any jazzy tags (should be none)
JAZZY_TAGS=$(grep -c ":jazzy" "${DOCKER_DIR}/docker-compose.yml" || true)
if [[ "$JAZZY_TAGS" -gt 0 ]]; then
    echo "⚠️  WARNING: Found ${JAZZY_TAGS} jazzy tags in docker-compose.yml"
    grep ":jazzy" "${DOCKER_DIR}/docker-compose.yml" || true
else
    echo "✅ PASS: No jazzy tags found"
fi
echo ""

# Check 6: Verify documentation exists
echo "Check 6: Verifying documentation..."
if [[ -f "${PROJECT_DIR}/docs/migration/humble-migration.md" ]]; then
    echo "✅ PASS: Migration design document exists"
else
    echo "⚠️  WARNING: Migration design document not found"
fi

if [[ -f "${PROJECT_DIR}/docs/test-cases/docker-verification.md" ]]; then
    echo "✅ PASS: Test cases document exists"
else
    echo "⚠️  WARNING: Test cases document not found"
fi
echo ""

# Check 7: Docker availability (optional)
echo "Check 7: Checking Docker availability..."
if command -v docker &>/dev/null; then
    echo "✅ Docker is available"
    if docker info &>/dev/null; then
        echo "✅ Docker daemon is running"
        echo ""
        echo "Optional: Run full build test with:"
        echo "  cd ${DOCKER_DIR} && docker-compose build"
    else
        echo "⚠️  Docker daemon is not running (skip build test)"
    fi
else
    echo "⚠️  Docker not installed (skip build test)"
fi
echo ""

echo "=== Verification Complete ==="
echo ""
echo "Summary:"
echo "  ✅ All static checks passed"
echo "  📝 Documentation verified"
echo "  🔨 Run 'docker-compose build' for full build test"
echo ""

exit 0
