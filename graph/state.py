from typing import TypedDict, Optional, List
from typing_extensions import NotRequired


class ErrorDetail(TypedDict):
    type: str
    reason: str


class MetaInfo(TypedDict, total=False):
    run_id: str
    ts_start: str
    ts_end: str


class ResultInfo(TypedDict):
    entity_id: Optional[str]
    entity_name: Optional[str]
    entity_detected: bool


class State(TypedDict, total=False):
    # input
    url: str

    # work
    entity_id: Optional[str]

    # control
    errors: List[ErrorDetail]
    meta: MetaInfo

    # output
    result: ResultInfo
