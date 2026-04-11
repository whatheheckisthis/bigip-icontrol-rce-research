#!/usr/bin/env node
const fs = require('node:fs');
const path = require('node:path');
const repo = process.cwd();
const protoDir = path.join(repo, 'proto');
const genDir = path.join(repo, 'generated');
const protos = fs.readdirSync(protoDir).filter(f => f.endsWith('.proto'));
const missing = [];
for (const proto of protos) {
  const base = proto.replace('.proto', '');
  for (const suffix of ['_pb2.py','_pb2_grpc.py']) {
    const expected = path.join(genDir, `${base}${suffix}`);
    if (!fs.existsSync(expected)) missing.push(path.relative(repo, expected));
  }
}
if (missing.length) {
  console.error('Missing generated stubs:');
  for (const m of missing) console.error(` - ${m}`);
  process.exit(1);
}
console.log('[OK] proto stubs are present');
