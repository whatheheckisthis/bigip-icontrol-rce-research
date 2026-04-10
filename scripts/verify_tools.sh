#!/usr/bin/env bash
# ============================================================
# Repository : bigip-icontrol-rce-research
# Path       : scripts/verify_tools.sh
# Purpose    : Validates required CLI tools for build and release workflows
# Layer      : sdlc
# SDLC Phase : implementation
# ASVS Ref   : V14.2
# OWASP Ref  : A06
# Modified   : 2026-04-10
# ============================================================
set -euo pipefail
for tool in python3 docker; do
  command -v "$tool" >/dev/null || { echo "missing tool: $tool"; exit 1; }
done
echo "toolchain check passed"
