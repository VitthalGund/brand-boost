from fastapi import FastAPI
from mangum import Mangum
from app.route.generator import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
handler = Mangum(app=app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=router)
