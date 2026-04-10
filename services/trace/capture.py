from __future__ import annotations

import re

FIXTURE_URL_PATTERN = re.compile(r"^https?://(localhost|127\.)")


def validate_fixture_url(target_fixture_url: str) -> bool:
    return bool(FIXTURE_URL_PATTERN.match(target_fixture_url))
