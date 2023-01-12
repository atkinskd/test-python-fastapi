import uvicorn
from fastapi import FastAPI

from .routers import health

app = FastAPI(
    title="appsec-ken-test-api",
    description="A test FastAPI Project",
    version="0.1.0",
)

app.include_router(health.router)

if __name__ == "__main__":
    uvicorn.run(app)
