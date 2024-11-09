from pydantic import BaseModel, Field
from enum import Enum

class TileStatus(Enum):
    EMPTY = 0
    CIRCLE = 1
    CROSS = 2

class PlayerSymbol(Enum):
    NULL = 0
    Circle = 1
    Cross = 2

class TileLocation(BaseModel):
    row: int = Field(None, ge=0, le=2)
    column: int = Field(None, ge=0, le=2)


class BaseTile(BaseModel):
    location: TileLocation
    status: TileStatus

class Player(BaseModel):
    """BaseModel for Player class

    Args:
        num (int): Either 1 or 2
        symbol (PlayerSymbol):
        name (str): optional, defaults to num if not initialized
        has_turn (bool):
    """    
    num: int = Field(None, ge=1, le=2)
    symbol: PlayerSymbol
    name: str = Field(default=num)
    has_turn: bool = Field(default=False)