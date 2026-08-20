from fastapi import FastAPI

app = FastAPI(
    title="Production DevOps API",
    version="1.0.0"
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/")
def root():
    return {
        "message": "Production DevOps API"
    }
