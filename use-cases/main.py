from datetime import date, datetime, timezone
from enum import Enum
from itertools import count
from typing import Dict, List, Optional

from fastapi import FastAPI, HTTPException, Path, Query, Response, status
from pydantic import BaseModel, Field, field_validator

app = FastAPI(
    title="To-Do API",
    description="A simple API for managing a to-do list.",
    version="1.0.0",
)


# --------------------------------------------------------------------------
# Models
# --------------------------------------------------------------------------
class TodoStatus(str, Enum):
    completed = "completed"
    pending = "pending"


class TodoCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, examples=["Buy groceries"])
    description: Optional[str] = Field(
        None, max_length=500, examples=["Milk, eggs, bread"]
    )
    due_date: Optional[date] = Field(None, examples=["2030-01-31"])

    @field_validator("title")
    @classmethod
    def title_not_blank(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("title must not be blank")
        return v

    @field_validator("due_date")
    @classmethod
    def due_date_not_in_past(cls, v: Optional[date]) -> Optional[date]:
        if v is not None and v < date.today():
            raise ValueError("due_date cannot be in the past")
        return v


class Todo(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    due_date: Optional[date] = None
    completed: bool = False
    created_at: datetime
    completed_at: Optional[datetime] = None


# --------------------------------------------------------------------------
# In-memory storage (swap for a real database in production)
# --------------------------------------------------------------------------
db: Dict[int, Todo] = {}
id_counter = count(1)

def get_todo_or_404(todo_id: int) -> Todo:
    todo = db.get(todo_id)
    if todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"To-do item with id {todo_id} not found",
        )
    return todo


# --------------------------------------------------------------------------
# Endpoints
# --------------------------------------------------------------------------
@app.post(
    "/todos",
    response_model=Todo,
    status_code=status.HTTP_201_CREATED,
    summary="Create a to-do item",
    tags=["todos"],
)
def create_todo(payload: TodoCreate) -> Todo:
    """Create a new to-do item with a title, optional description and optional due date."""
    todo = Todo(
        id=next(id_counter),
        created_at=datetime.now(timezone.utc),
        **payload.model_dump(),
    )
    db[todo.id] = todo
    return todo


@app.get(
    "/todos",
    response_model=List[Todo],
    summary="List to-do items",
    tags=["todos"],
)
def list_todos(
    status_filter: Optional[TodoStatus] = Query(
        None,
        alias="status",
        description="Filter by status: `completed` or `pending`. Omit for all items.",
    ),
) -> List[Todo]:
    """Return all to-do items, optionally filtered by status."""
    todos = list(db.values())
    if status_filter == TodoStatus.completed:
        todos = [t for t in todos if t.completed]
    elif status_filter == TodoStatus.pending:
        todos = [t for t in todos if not t.completed]
    return todos


@app.get(
    "/todos/{todo_id}",
    response_model=Todo,
    summary="Get a single to-do item",
    tags=["todos"],
    responses={404: {"description": "To-do item not found"}},
)
def get_todo(todo_id: int = Path(..., ge=1, description="The ID of the to-do item")) -> Todo:
    return get_todo_or_404(todo_id)


@app.patch(
    "/todos/{todo_id}/complete",
    response_model=Todo,
    summary="Mark a to-do item as completed",
    tags=["todos"],
    responses={404: {"description": "To-do item not found"}},
)
def complete_todo(todo_id: int = Path(..., ge=1, description="The ID of the to-do item")) -> Todo:
    """Mark the item as completed. Calling this on an already-completed item is harmless."""
    todo = get_todo_or_404(todo_id)
    if not todo.completed:
        todo.completed = True
        todo.completed_at = datetime.now(timezone.utc)
    return todo


@app.delete(
    "/todos/{todo_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a to-do item",
    tags=["todos"],
    responses={404: {"description": "To-do item not found"}},
)
def delete_todo(todo_id: int = Path(..., ge=1, description="The ID of the to-do item")) -> Response:
    get_todo_or_404(todo_id)
    del db[todo_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)