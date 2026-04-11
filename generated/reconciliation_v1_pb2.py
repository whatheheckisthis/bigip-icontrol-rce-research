# Repository : bigip-icontrol-rce-research
# Path       : generated/reconciliation_v1_pb2.py
# Purpose    : Inline fallback protobuf stubs for offline build environments.
# Layer      : proto
# SDLC Phase : implementation
# ASVS Ref   : N/A
# OWASP Ref  : N/A
# Modified   : 2026-04-11
class _M:
    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            setattr(self,k,v)

LATEST_WINS=0
SOURCE_PRIORITY=1
MANUAL=2
class ConflictDetail(_M):
    def __init__(self, field_name="", existing_value="", incoming_value=""): super().__init__(field_name=field_name,existing_value=existing_value,incoming_value=incoming_value)
class ConflictRecord(_M):
    def __init__(self, record_id="", record_type="", conflicts=None, strategy=LATEST_WINS, resolved_at=0, resolved_by=""):
        super().__init__(record_id=record_id,record_type=record_type,conflicts=conflicts or {},strategy=strategy,resolved_at=resolved_at,resolved_by=resolved_by)
class SubmitConflictRequest(_M):
    def __init__(self, conflict=None): super().__init__(conflict=conflict or ConflictRecord())
class SubmitConflictResponse(_M):
    def __init__(self, conflict_id=""): super().__init__(conflict_id=conflict_id)
class ResolveConflictRequest(_M):
    def __init__(self, conflict_id="", strategy=LATEST_WINS, operator_id=""): super().__init__(conflict_id=conflict_id,strategy=strategy,operator_id=operator_id)
class ResolveConflictResponse(_M):
    def __init__(self, conflict=None): super().__init__(conflict=conflict or ConflictRecord())
class GetAuditTrailRequest(_M):
    def __init__(self, record_id=""): super().__init__(record_id=record_id)
class GetAuditTrailResponse(_M):
    def __init__(self, trail_rows=None): super().__init__(trail_rows=trail_rows or [])
class ListUnresolvedRequest(_M): pass
class ListUnresolvedResponse(_M):
    def __init__(self, conflicts=None): super().__init__(conflicts=conflicts or [])
