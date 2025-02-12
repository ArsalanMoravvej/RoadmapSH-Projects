from fastapi import FastAPI
from .routes import user, auth

#models.Base.metadata.create_all(bind = engine)

#TaskTrackerAPI: Exercise app for roadmap.sh
app = FastAPI()

app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI application!"}

# Another path example
@app.get("/anotherpath")
async def another_path():
    return {"message": "This is another example path!"}