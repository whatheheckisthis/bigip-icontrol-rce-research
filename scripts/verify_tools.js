#!/usr/bin/env node
const {execSync} = require('node:child_process');

const checks = [
  ['node', '--version', 20],
  ['npm', '--version', 10],
];
let failed = false;
for (const [tool,arg,minMajor] of checks) {
  try {
    const out = execSync(`${tool} ${arg}`, {encoding:'utf8'}).trim();
    const major = Number(out.replace(/^v/, '').split('.')[0]);
    if (major >= minMajor) {
      console.log(`[OK] ${tool} ${out}`);
    } else {
      failed = true;
      console.log(`[FAIL] ${tool} ${out} < ${minMajor}`);
    }
  } catch {
    failed = true;
    console.log(`[FAIL] ${tool} not found / below minimum`);
  }
}
process.exit(failed ? 1 : 0);
