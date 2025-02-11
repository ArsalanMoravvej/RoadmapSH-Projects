from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI application!"}

# Another path example
@app.get("/anotherpath")
async def another_path():
    return {"message": "This is another example path!"}