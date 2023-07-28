from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from routes import crawler

app = FastAPI()
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(crawler)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="localhost",
        port=8000,
        reload=1,
        server_header=0
    )