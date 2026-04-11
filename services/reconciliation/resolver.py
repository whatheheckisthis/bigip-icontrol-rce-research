# Repository : bigip-icontrol-rce-research
# Path       : services/reconciliation/resolver.py
# Purpose    : Implements conflict resolution strategy helpers.
# Layer      : service
# SDLC Phase : implementation
# ASVS Ref   : V7.1.1
# OWASP Ref  : A09
# Modified   : 2026-04-11
class ManualResolutionRequired(Exception):
    pass


def resolve_latest_wins(a, b, conflicts):
    winner = a if a.ingestion_timestamp >= b.ingestion_timestamp else b
    for field_name in conflicts:
        setattr(a, field_name, getattr(winner, field_name))
    return a


def resolve_source_priority(a, b, conflicts, priority_order=["nvd", "vendor", "third-party"]):
    left_i = priority_order.index(a.source_uri) if a.source_uri in priority_order else len(priority_order)
    right_i = priority_order.index(b.source_uri) if b.source_uri in priority_order else len(priority_order)
    winner = a if left_i <= right_i else b
    for field_name in conflicts:
        setattr(a, field_name, getattr(winner, field_name))
    return a


def resolve_manual(conflict_id: str):
    raise ManualResolutionRequired(conflict_id)
