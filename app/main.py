from fastapi import FastAPI
from app.routes import task

app = FastAPI(
    title="To-Do List API",
    description="API REST para administrar tareas (To-Do List)",
    version="1.0.0"
)


app.include_router(task.router)
