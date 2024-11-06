from pydantic import BaseModel, Field
from enum import Enum

class TileStatus(Enum):
    EMPTY = 0
    CIRCLE = 1
    CROSS = 2

class TileLocation(BaseModel):
    row: int = Field(None, ge=0, le=2)
    column: int = Field(None, ge=0, le=2)

class BaseTile(BaseModel):
    location: TileLocation
    status: TileStatus
