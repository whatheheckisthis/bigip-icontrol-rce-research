#!/usr/bin/env bash
set -euo pipefail

fail=0

check_tool() {
  local tool="$1" cmd="$2" min_major="$3"
  if ! out=$(eval "$cmd" 2>/dev/null); then
    echo "[FAIL] $tool not found / below minimum"
    fail=1
    return
  fi
  local version
  version=$(echo "$out" | head -n1 | grep -oE '[0-9]+(\.[0-9]+)+' | head -n1 || true)
  local major=${version%%.*}
  if [[ -z "$major" || "$major" -lt "$min_major" ]]; then
    echo "[FAIL] $tool $out"
    fail=1
  else
    echo "[OK] $tool $out"
  fi
}

check_tool "python3.12" "python3.12 --version" 3
check_tool "docker" "docker --version" 24
check_tool "docker compose" "docker compose version" 2
check_tool "protoc" "protoc --version" 25
check_tool "make" "make --version" 4

exit $fail
