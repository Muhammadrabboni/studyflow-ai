
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer(auto_error=False)

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
    credentials: HTTPAuthorizationCredentials | None = Depends(security)
):
    if credentials is None:
        raise HTTPException(
            status_code=401,
            detail="Authentication token is required.",
            headers={"WWW-Authenticate": "Bearer"}
        )

    user = MOCK_USERS.get(credentials.credentials)

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication token.",
            headers={"WWW-Authenticate": "Bearer"}
        )

    return user
