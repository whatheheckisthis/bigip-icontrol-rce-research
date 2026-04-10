from __future__ import annotations


class ControlRegistryService:
    def __init__(self) -> None:
        self._controls: dict[str, dict] = {}

    def register(self, control: dict) -> str:
        control_id = control["control_id"]
        self._controls[control_id] = control
        return control_id
