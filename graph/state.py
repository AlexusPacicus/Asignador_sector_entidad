from typing import TypedDict, Optional

class State(TypedDict):
    url: str
    is_spanish: bool
    entity_id: Optional[str]
