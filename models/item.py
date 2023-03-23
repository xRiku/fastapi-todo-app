from datetime import datetime
import uuid
from pydantic import BaseModel, Field
from id_generator import IDGenerator

id_generator = IDGenerator()

class Item(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, editable=False)
    title: str
    checked: bool = Field(default=False, editable=False)
    created_at: str = Field(default_factory=lambda: datetime.now().isoformat(), editable=False)
    deleted_at: str = Field(default=None, editable=False)
    updated_at: str = Field(default=None, editable=False)
    position: int = Field(default_factory=id_generator.get_next_id, editable=False) 