#!/usr/bin/env node
// Repository : bigip-icontrol-rce-research
// Path       : scripts/verify_tools.js
// Purpose    : Verifies Node/NPM major versions for script pipeline compatibility.
// Layer      : scripts
// SDLC Phase : verification
// ASVS Ref   : V14.2.1
// OWASP Ref  : A06
// Modified   : 2026-04-11
const { execSync } = require("child_process");
const checks = [
  { cmd: "node --version", min: 20, name: "node" },
  { cmd: "npm  --version", min: 10, name: "npm" }
];
let failed = false;
for (const { cmd, min, name } of checks) {
  try {
    const raw = execSync(cmd, { encoding: "utf8" }).trim();
    const major = parseInt(raw.replace(/[^0-9.].*/, "").split(".")[0], 10);
    if (major < min) {
      console.error(`[FAIL] ${name} ${raw} < required ${min}.x`);
      failed = true;
    } else {
      console.log(`[OK]   ${name} ${raw}`);
    }
  } catch {
    console.error(`[FAIL] ${name} not found`);
    failed = true;
  }
}
process.exit(failed ? 1 : 0);
