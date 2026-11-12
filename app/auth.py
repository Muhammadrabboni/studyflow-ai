
from fastapi import Header, HTTPException, status

# Predefined mock users
MOCK_USERS = {
    "user-a-token": {
        "id": "user-a",
        "name": "Student A",
        "role": "user"
    },
    "user-b-token": {
        "id": "user-b",
        "name": "Student B",
        "role": "user"
    },
    "admin-token": {
        "id": "admin",
        "name": "Administrator",
        "role": "admin"
    }
}


def get_current_user(
    authorization: str | None = Header(default=None)
):
    # Check whether the Authorization header exists
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication token is required."
        )

    # Check Bearer token format
    parts = authorization.split()

    if len(parts) != 2 or parts[0].lower() != "bearer":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authorization format."
        )

    token = parts[1]

    # Validate token
    user = MOCK_USERS.get(token)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token."
        )

    return user
