# CVE-2021-22986 Technical Analysis

<!--
Repository : bigip-icontrol-rce-research
Path       : docs/cve_technical_analysis.md
Purpose    : Provides technical analysis of CVE-2021-22986 exploit characteristics and impact
Layer      : docs
SDLC Phase : requirements
ASVS Ref   : V1.1.1
OWASP Ref  : A03
Modified   : 2026-04-10
-->

CVE-2021-22986 allows unauthenticated request crafting against BIG-IP iControl REST endpoints under vulnerable configurations. This repository models observable request/response behavior for defensive validation and does not execute shell commands.
