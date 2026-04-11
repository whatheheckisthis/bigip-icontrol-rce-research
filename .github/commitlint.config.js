// ============================================================
// Repository : bigip-icontrol-rce-research
// Path       : .github/commitlint.config.js
// Purpose    : Conventional Commits enforcement for PR commits
// Layer      : config
// SDLC Phase : implementation
// ASVS Ref   : N/A
// OWASP Ref  : N/A
// Modified   : 2026-04-12
// ============================================================

module.exports = {
  extends: ['@commitlint/config-conventional'],
  rules: {
    'type-enum': [2, 'always', ['feat', 'fix', 'chore', 'sdlc', 'gap', 'test', 'refactor']],
    'scope-enum': [
      2,
      'always',
      [
        'proto',
        'ingestion',
        'trace',
        'control',
        'evidence',
        'reconcile',
        'tests',
        'asvs',
        'scripts',
        'ci',
        'deps',
        'docs',
      ],
    ],
    'subject-case': [2, 'always', 'sentence-case'],
    'subject-max-length': [2, 'always', 72],
    'subject-full-stop': [2, 'never', '.'],
    'body-max-line-length': [1, 'always', 100],
    'footer-max-line-length': [0],
  },
};
