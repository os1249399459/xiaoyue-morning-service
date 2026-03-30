#!/bin/bash
# 小月早安服务启动脚本

export TELEGRAM_BOT_TOKEN="${TELEGRAM_BOT_TOKEN:-}"

cd "$(dirname "$0")"
python3 main.py