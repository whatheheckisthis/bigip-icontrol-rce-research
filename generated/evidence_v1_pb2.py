# Repository : bigip-icontrol-rce-research
# Path       : generated/evidence_v1_pb2.py
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

LOG=0
CONFIG=1
TEST_RESULT=2
TRACE=3
CROSSWALK=4
class EvidenceRecord(_M):
    def __init__(self, evidence_id="", artefact_type=LOG, source_service="", content_hash="", content_uri="", lineage=None, created_at=0, operator_id=""):
        super().__init__(evidence_id=evidence_id,artefact_type=artefact_type,source_service=source_service,content_hash=content_hash,content_uri=content_uri,lineage=lineage or [],created_at=created_at,operator_id=operator_id)
class RecordEvidenceRequest(_M):
    def __init__(self, record=None): super().__init__(record=record or EvidenceRecord())
class RecordEvidenceResponse(_M):
    def __init__(self, evidence_id=""): super().__init__(evidence_id=evidence_id)
class GetEvidenceRequest(_M):
    def __init__(self, evidence_id=""): super().__init__(evidence_id=evidence_id)
class ChainLineageRequest(_M):
    def __init__(self, evidence_id=""): super().__init__(evidence_id=evidence_id)
class ChainLineageResponse(_M):
    def __init__(self, lineage=None): super().__init__(lineage=lineage or [])
class ExportLedgerRequest(_M): pass
class ExportLedgerResponse(_M):
    def __init__(self, ledger_json=b""): super().__init__(ledger_json=ledger_json)
