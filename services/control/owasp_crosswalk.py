# Repository : bigip-icontrol-rce-research
# Path       : services/control/owasp_crosswalk.py
# Purpose    : Maps OWASP categories to ASVS controls and performs reverse lookup.
# Layer      : service
# SDLC Phase : design
# ASVS Ref   : V1.1.1
# OWASP Ref  : A01,A10
# Modified   : 2026-04-11
CROSSWALK = {
    "A01": ["V4.1.1"],
    "A02": ["V9.2.1"],
    "A03": ["V5.2.3"],
    "A04": ["V1.1.1"],
    "A05": ["V14.4.1"],
    "A06": ["V14.2.1"],
    "A07": ["V2.1.1"],
    "A08": ["V10.2.1"],
    "A09": ["V7.1.1"],
    "A10": ["V10.3.2"],
}


def get_controls_for_owasp(category: str) -> list[str]:
    return CROSSWALK.get(category, [])


def get_owasp_for_control(control_id: str) -> str:
    for cat, controls in CROSSWALK.items():
        if control_id in controls:
            return cat
    raise KeyError(control_id)
