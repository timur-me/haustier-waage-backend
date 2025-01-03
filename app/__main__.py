# app/__main__.py
from fastapi import FastAPI

# Initialize FastAPI app instance
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "paperclips."}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
