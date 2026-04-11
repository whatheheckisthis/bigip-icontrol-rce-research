#!/usr/bin/env node
// Repository : bigip-icontrol-rce-research
// Path       : scripts/verify_versions.js
// Purpose    : Prints runtime versions used by Node pipeline verification.
// Layer      : scripts
// SDLC Phase : verification
// ASVS Ref   : N/A
// OWASP Ref  : N/A
// Modified   : 2026-04-11
console.log(JSON.stringify({ node: process.version }, null, 2));
