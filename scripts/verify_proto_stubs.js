#!/usr/bin/env node
// Repository : bigip-icontrol-rce-research
// Path       : scripts/verify_proto_stubs.js
// Purpose    : Asserts generated Python gRPC stub files exist for each contract.
// Layer      : scripts
// SDLC Phase : verification
// ASVS Ref   : V14.2.1
// OWASP Ref  : A06
// Modified   : 2026-04-11
const fs = require("fs");
const path = require("path");
const protos = ["vulnerability_v1", "exploit_trace_v1", "control_v1", "evidence_v1", "reconciliation_v1"];
const missing = [];
for (const p of protos) {
  for (const suffix of ["_pb2.py", "_pb2_grpc.py"]) {
    const f = path.join("generated", p + suffix);
    if (!fs.existsSync(f)) missing.push(f);
  }
}
if (missing.length) {
  console.error(`[FAIL] missing stubs:\n${missing.join("\n")}`);
  process.exit(1);
}
console.log("[OK] all proto stubs present");
