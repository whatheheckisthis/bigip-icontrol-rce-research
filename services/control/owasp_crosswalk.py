CROSSWALK = {
    "A01": ["V4.1.1"],
    "A02": ["V6.2.1"],
    "A03": ["V5.2.3"],
    "A04": ["V1.1.1"],
    "A05": ["V14.2.1"],
    "A06": ["V1.14.4"],
    "A07": ["V2.1.1"],
    "A08": ["V7.1.1"],
    "A09": ["V7.2.1"],
    "A10": ["V10.3.2"],
}


def get_controls_for_owasp(category: str) -> list[str]:
    return CROSSWALK.get(category, [])


def get_owasp_for_control(control_id: str) -> str:
    for category, controls in CROSSWALK.items():
        if control_id in controls:
            return category
    raise KeyError(control_id)
