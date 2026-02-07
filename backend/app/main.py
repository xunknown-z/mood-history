from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.schemas.mood import MoodCreate

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

# 임시 데이터 저장소 (데이터베이스 대신 메모리에 저장합니다)
# 서버를 껐다 켜면 초기화되지만, 연습용으로 딱 좋습니다!
mood_db = []

# 1. 기분 목록 가져오기 (GET)
@app.get("/moods")
def get_moods():
    # 저장된 모든 기분 리스트를 그대로 보내줍니다.
    return mood_db

# 2. 새로운 기분 추가하기 (POST)
@app.post("/moods")
def create_mood(data: MoodCreate):
    # 새로운 고유 번호를 생성합니다 (리스트 길이에 +1)
    new_id = len(mood_db) + 1

    # 받은 데이터에 ID를 붙여서 새로운 딕셔너리를 만듭니다.
    new_mood = {
        "id": new_id,
        "name": data.name,
        "mood": data.mood
    }

    # 리스트에 추가합니다.
    mood_db.append(new_mood)

    # 저장된 결과를 다시 확인시켜줍니다.
    return new_mood