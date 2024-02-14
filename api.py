from fastapi import FastAPI
from routers import customer_router

app = FastAPI()

app.include_router(customer_router)
# (
#     customer_router,
#     prefix="/api/v1",
#     tags=["Patient"],
#     responses={418: {"description": "I'm a Patient API"}},
# )


@app.get("/")
def ping():
    """ping func provides a health check

    Returns:
        [dict]: [success response for health check]
    """
    return {"response": "ping to datahub successful"}
