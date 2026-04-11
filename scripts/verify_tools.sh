#!/usr/bin/env bash
# Repository : bigip-icontrol-rce-research
# Path       : scripts/verify_tools.sh
# Purpose    : Verifies local prerequisite toolchain versions before build tasks.
# Layer      : scripts
# SDLC Phase : verification
# ASVS Ref   : V14.2.1
# OWASP Ref  : A06
# Modified   : 2026-04-11
set -euo pipefail

check() {
  local tool=$1 flag=$2 min=$3
  if ! command -v "$tool" &>/dev/null; then
    echo "[FAIL] $tool not found"; return 1
  fi
  local ver
  ver=$("$tool" $flag 2>&1 | grep -oE '[0-9]+\.[0-9]+' | head -1)
  local major=${ver%%.*}
  if [[ "$major" -lt "$min" ]]; then
    echo "[FAIL] $tool $ver < required $min.x"; return 1
  fi
  echo "[OK]   $tool $ver"
}

check python3.12 --version 3
check docker     --version  24
check protoc     --version  25
check make       --version  4
docker compose version &>/dev/null || { echo "[FAIL] docker compose v2 not found"; exit 1; }
echo "[OK]   docker compose v2"
