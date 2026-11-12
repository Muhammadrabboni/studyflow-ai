
from datetime import date

assignments = [
    {
        "id": "assignment_101",
        "title": "Complete Python Assignment",
        "description": "Implement functions using NumPy.",
        "course": "Machine Learning",
        "deadline": "2026-11-20",
        "priority": "high",
        "status": "pending",
        "ownerId": "user-a"
    },
    {
        "id": "assignment_102",
        "title": "Prepare Database Project",
        "description": "Design an SQL database and write queries.",
        "course": "Database Systems",
        "deadline": "2026-11-25",
        "priority": "medium",
        "status": "in_progress",
        "ownerId": "user-a"
    },
    {
        "id": "assignment_103",
        "title": "Software Engineering Report",
        "description": "Prepare the software engineering report.",
        "course": "Software Engineering",
        "deadline": "2026-11-22",
        "priority": "high",
        "status": "pending",
        "ownerId": "user-b"
    },
    {
        "id": "assignment_104",
        "title": "Network Security Exercises",
        "description": "Complete the cryptography exercises.",
        "course": "Network Security",
        "deadline": "2026-11-28",
        "priority": "low",
        "status": "completed",
        "ownerId": "user-b"
    }
]

def get_next_assignment_id():
    existing_ids = [
        int(assignment["id"].split("_")[1])
        for assignment in assignments
    ]

    next_id = max(existing_ids, default=100) + 1
    return f"assignment_{next_id}"
