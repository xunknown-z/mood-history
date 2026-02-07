from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 프론트엔드 주소 허용 (Vite 기본값은 5173)
origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # 모든 방식(GET, POST 등) 허용
    allow_headers=["*"], # 모든 헤더 허용
)

@app.get("/")
def reat_root():
    return {"message": "안녕! 나는 백엔드 서버야."}