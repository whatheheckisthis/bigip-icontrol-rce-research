from services.ingestion.dedup import CanonicalVulnerability, build_fingerprint


def test_build_fingerprint_stable_sorting() -> None:
    a = CanonicalVulnerability("CVE-2021-22986", "AV:N/AC:L", ["16.1", "15.1"])
    b = CanonicalVulnerability("CVE-2021-22986", "AV:N/AC:L", ["15.1", "16.1"])
    assert build_fingerprint(a) == build_fingerprint(b)
