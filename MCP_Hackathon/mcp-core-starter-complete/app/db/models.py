from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    role: str = 'child'

class Problem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    statement: str
    solution: str

class Attempt(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int
    problem_id: int
    score: float
    created_at: datetime = Field(default_factory=datetime.utcnow)
