
from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.routes.assignments import router as assignments_router

app = FastAPI(
    title="StudyFlow AI API",
    description="REST API for managing student assignments and deadlines.",
    version="1.0.0"
)


ERROR_CODES = {
    400: "VALIDATION_ERROR",
    401: "UNAUTHORIZED",
    403: "FORBIDDEN",
    404: "NOT_FOUND",
    405: "METHOD_NOT_ALLOWED",
    409: "CONFLICT"
}


@app.exception_handler(HTTPException)
async def http_exception_handler(
    request: Request,
    exc: HTTPException
):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": {
                "code": ERROR_CODES.get(
                    exc.status_code,
                    "HTTP_ERROR"
                ),
                "message": str(exc.detail)
            }
        },
        headers=exc.headers
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    details = []

    for error in exc.errors():
        field = ".".join(
            str(part) for part in error["loc"]
            if part not in ("body", "query", "path")
        )

        details.append({
            "field": field,
            "message": error["msg"]
        })

    return JSONResponse(
        status_code=400,
        content={
            "success": False,
            "error": {
                "code": "VALIDATION_ERROR",
                "message": "The request contains invalid or missing fields.",
                "details": details
            }
        }
    )


app.include_router(assignments_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to StudyFlow AI API",
        "version": "v1"
    }
