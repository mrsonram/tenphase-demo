#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
echo "Starting TENPHASE VILLAIN client pitch server..."

PY=""
for cmd in python python3 py; do
  if command -v "$cmd" >/dev/null 2>&1 && "$cmd" -c "import sys" >/dev/null 2>&1; then
    PY="$cmd"
    break
  fi
done

if [ -z "$PY" ]; then
  echo "Python not found. Install it from https://www.python.org/downloads/" >&2
  exit 1
fi

exec "$PY" serve.py
