
from datetime import date
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class AssignmentCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=1, max_length=500)
    course: str = Field(min_length=2, max_length=100)
    deadline: date
    priority: Literal["low", "medium", "high"]
    status: Literal["pending", "in_progress", "completed"] = "pending"


class AssignmentUpdate(AssignmentCreate):
    pass
