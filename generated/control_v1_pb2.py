# Repository : bigip-icontrol-rce-research
# Path       : generated/control_v1_pb2.py
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

NOT_STARTED=0
IN_PROGRESS=1
IMPLEMENTED=2
VERIFIED=3
class ControlRecord(_M):
    def __init__(self, control_id="", owasp_category="", description="", status=NOT_STARTED, evidence_refs=None, last_verified_timestamp=0): super().__init__(control_id=control_id,owasp_category=owasp_category,description=description,status=status,evidence_refs=evidence_refs or [],last_verified_timestamp=last_verified_timestamp)
class RegisterControlRequest(_M):
    def __init__(self, record=None): super().__init__(record=record or ControlRecord())
class RegisterControlResponse(_M):
    def __init__(self, record=None, evidence_id=""): super().__init__(record=record or ControlRecord(), evidence_id=evidence_id)
class UpdateStatusRequest(_M):
    def __init__(self, control_id="", status=NOT_STARTED, evidence_ref="", verified_timestamp=0): super().__init__(control_id=control_id,status=status,evidence_ref=evidence_ref,verified_timestamp=verified_timestamp)
class UpdateStatusResponse(_M):
    def __init__(self, record=None, evidence_id=""): super().__init__(record=record or ControlRecord(), evidence_id=evidence_id)
class GetControlRequest(_M):
    def __init__(self, control_id=""): super().__init__(control_id=control_id)
class ListByOWASPRequest(_M):
    def __init__(self, owasp_category=""): super().__init__(owasp_category=owasp_category)
class ListByOWASPResponse(_M):
    def __init__(self, records=None): super().__init__(records=records or [])
class ExportControlMatrixRequest(_M): pass
class ExportControlMatrixResponse(_M):
    def __init__(self, csv_content=b""): super().__init__(csv_content=csv_content)
