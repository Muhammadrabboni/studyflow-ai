
from datetime import date
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status

from app.auth import get_current_user
from app.data import assignments, get_next_assignment_id
from app.schemas import AssignmentCreate, AssignmentUpdate

router = APIRouter(
    prefix="/api/v1/assignments",
    tags=["Assignments"]
)


def success_response(message, data, meta=None):
    response = {
        "success": True,
        "message": message,
        "data": data
    }

    if meta is not None:
        response["meta"] = meta

    return response


def find_assignment(assignment_id):
    return next(
        (
            assignment for assignment in assignments
            if assignment["id"] == assignment_id
        ),
        None
    )


def check_ownership(assignment, current_user):
    if (
        current_user["role"] != "admin"
        and assignment["ownerId"] != current_user["id"]
    ):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Assignment not found."
        )


@router.get("")
def list_assignments(
    course: Optional[str] = None,
    assignment_status: Optional[str] = Query(
        default=None,
        alias="status"
    ),
    deadline_before: Optional[date] = None,
    page: int = Query(default=1, ge=1),
    per_page: int = Query(default=10, ge=1, le=100),
    current_user: dict = Depends(get_current_user)
):
    # Regular users see only their own assignments.
    if current_user["role"] == "admin":
        results = assignments.copy()
    else:
        results = [
            item for item in assignments
            if item["ownerId"] == current_user["id"]
        ]

    # Apply filters.
    if course:
        results = [
            item for item in results
            if item["course"].lower() == course.lower()
        ]

    if assignment_status:
        results = [
            item for item in results
            if item["status"] == assignment_status
        ]

    if deadline_before:
        results = [
            item for item in results
            if date.fromisoformat(item["deadline"]) <= deadline_before
        ]

    total = len(results)

    start = (page - 1) * per_page
    end = start + per_page

    return success_response(
        "Assignments retrieved successfully.",
        results[start:end],
        {
            "total": total,
            "page": page,
            "perPage": per_page
        }
    )


@router.get("/{assignment_id}")
def get_assignment(
    assignment_id: str,
    current_user: dict = Depends(get_current_user)
):
    assignment = find_assignment(assignment_id)

    if assignment is None:
        raise HTTPException(
            status_code=404,
            detail="Assignment not found."
        )

    check_ownership(assignment, current_user)

    return success_response(
        "Assignment retrieved successfully.",
        assignment
    )


@router.post("", status_code=status.HTTP_201_CREATED)
def create_assignment(
    assignment_data: AssignmentCreate,
    current_user: dict = Depends(get_current_user)
):
    new_assignment = assignment_data.model_dump(mode="json")

    new_assignment["id"] = get_next_assignment_id()
    new_assignment["ownerId"] = current_user["id"]

    assignments.append(new_assignment)

    return success_response(
        "Assignment created successfully.",
        new_assignment
    )


@router.put("/{assignment_id}")
def update_assignment(
    assignment_id: str,
    assignment_data: AssignmentUpdate,
    current_user: dict = Depends(get_current_user)
):
    assignment = find_assignment(assignment_id)

    if assignment is None:
        raise HTTPException(
            status_code=404,
            detail="Assignment not found."
        )

    check_ownership(assignment, current_user)

    updated_data = assignment_data.model_dump(mode="json")

    # Preserve the original ID and owner.
    assignment.update(updated_data)

    return success_response(
        "Assignment updated successfully.",
        assignment
    )


@router.delete("/{assignment_id}")
def delete_assignment(
    assignment_id: str,
    current_user: dict = Depends(get_current_user)
):
    assignment = find_assignment(assignment_id)

    if assignment is None:
        raise HTTPException(
            status_code=404,
            detail="Assignment not found."
        )

    check_ownership(assignment, current_user)

    assignments.remove(assignment)

    return success_response(
        "Assignment deleted successfully.",
        None
    )
