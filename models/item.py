from datetime import datetime
from typing import Optional
import uuid
from pydantic import BaseModel, Field
from id_generator import IDGenerator

id_generator = IDGenerator()

class Item(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, editable=False)
    title: str
    checked: bool = Field(default=False, editable=False)
    created_at: datetime = Field(default_factory=lambda: datetime.now().isoformat(), editable=False)
    deleted_at: datetime = Field(default=None, editable=False)
    updated_at: datetime = Field(default=None, editable=False)
    position: int = Field(default_factory=id_generator.get_next_id, editable=False) 


class ItemUpdate(BaseModel):
    title: Optional[str] = Field(None)
    checked: Optional[bool] = Field(None)