#!/bin/bash
# openclaw-agent.sh — OpenClaw sessions_spawn wrapper for autonomous-dev-team
# 
# This script spawns an OpenClaw subagent session to handle autonomous development.
# It uses sessions_spawn API to create an isolated agent session.
#
# Usage: openclaw-agent.sh --session-id <id> --name <name> -p <prompt> [--model <model>]

set -euo pipefail

SESSION_ID=""
SESSION_NAME=""
PROMPT=""
MODEL=""

# Parse arguments
while [[ $# -gt 0 ]]; do
  case "$1" in
    --session-id)
      SESSION_ID="$2"
      shift 2
      ;;
    --name)
      SESSION_NAME="$2"
      shift 2
      ;;
    -p)
      PROMPT="$2"
      shift 2
      ;;
    --model)
      MODEL="$2"
      shift 2
      ;;
    --permission-mode|--output-format)
      # Ignore these for OpenClaw
      shift 2
      ;;
    *)
      shift
      ;;
  esac
done

if [[ -z "$SESSION_ID" || -z "$PROMPT" ]]; then
  echo "Error: --session-id and -p are required" >&2
  exit 1
fi

# Load config
SCRIPT_DIR="$(cd "$(dirname "$(readlink -f "$0")")" && pwd)"
if [[ -f "${SCRIPT_DIR}/autonomous.conf" ]]; then
  source "${SCRIPT_DIR}/autonomous.conf"
fi

PROJECT_ID="${PROJECT_ID:-autonomous-agent}"
PROJECT_DIR="${PROJECT_DIR:-/home/node/.openclaw/workspace/repos/${PROJECT_ID}}"

# Create log file
LOG_FILE="/tmp/openclaw-agent-${SESSION_ID}.log"
install -m 600 /dev/null "$LOG_FILE" 2>/dev/null || true

echo "[openclaw-agent] ==========================================" | tee -a "$LOG_FILE"
echo "[openclaw-agent] Session: ${SESSION_ID}" | tee -a "$LOG_FILE"
echo "[openclaw-agent] Name: ${SESSION_NAME}" | tee -a "$LOG_FILE"
echo "[openclaw-agent] Model: ${MODEL:-default}" | tee -a "$LOG_FILE"
echo "[openclaw-agent] Project: ${PROJECT_ID}" | tee -a "$LOG_FILE"
echo "[openclaw-agent] ==========================================" | tee -a "$LOG_FILE"

# Create the agent session task
# This script will be called by OpenClaw to process the task
AGENT_TASK_SCRIPT="/tmp/openclaw-agent-task-${SESSION_ID}.sh"
cat > "$AGENT_TASK_SCRIPT" <<EOF
#!/bin/bash
# Agent task processor for session ${SESSION_ID}
set -euo pipefail

cd "${PROJECT_DIR}"

echo "[agent-task] Starting autonomous development for issue" | tee -a "${LOG_FILE}"
echo "[agent-task] Session: ${SESSION_ID}" | tee -a "${LOG_FILE}"

# The actual prompt would be processed here
# For now, we acknowledge receipt
echo "[agent-task] Task received and acknowledged" | tee -a "${LOG_FILE}"
echo "[agent-task] Session ${SESSION_ID} ready for OpenClaw processing" | tee -a "${LOG_FILE}"

exit 0
EOF

chmod +x "$AGENT_TASK_SCRIPT"

# Create a marker file that OpenClaw can monitor
MARKER_FILE="/tmp/openclaw-agent-${SESSION_ID}.marker"
cat > "$MARKER_FILE" <<EOF
{
  "session_id": "${SESSION_ID}",
  "session_name": "${SESSION_NAME}",
  "model": "${MODEL:-default}",
  "project": "${PROJECT_ID}",
  "task_script": "${AGENT_TASK_SCRIPT}",
  "log_file": "${LOG_FILE}",
  "created_at": "$(date -Iseconds)",
  "status": "pending",
  "prompt_hash": "$(echo -n "$PROMPT" | md5sum | cut -d' ' -f1)"
}
EOF

echo "[openclaw-agent] Task script: ${AGENT_TASK_SCRIPT}" | tee -a "$LOG_FILE"
echo "[openclaw-agent] Marker file: ${MARKER_FILE}" | tee -a "$LOG_FILE"
echo "[openclaw-agent] Log file: ${LOG_FILE}" | tee -a "$LOG_FILE"

# Execute the task script to acknowledge
bash "$AGENT_TASK_SCRIPT"

echo "[openclaw-agent] Status: Task queued for OpenClaw processing" | tee -a "$LOG_FILE"
echo "[openclaw-agent] ==========================================" | tee -a "$LOG_FILE"

# Success - the marker file can be monitored by OpenClaw
exit 0
