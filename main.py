import uvicorn
from api_gateway.routes import app

if __name__ == "__main__":
    # Running FastAPI app with Uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
