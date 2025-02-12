from fastapi import FastAPI
from .routes import user, auth, task

#TaskTrackerAPI: Exercise app for roadmap.sh
app = FastAPI()

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(task.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the To-Dolister web application!"}