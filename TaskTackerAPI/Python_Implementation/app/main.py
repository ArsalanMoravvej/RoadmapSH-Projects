from fastapi import FastAPI



#TaskTrackerAPI: Exercise app for roadmap.sh
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI application!"}

# Another path example
@app.get("/anotherpath")
async def another_path():
    return {"message": "This is another example path!"}