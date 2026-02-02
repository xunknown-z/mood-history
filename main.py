from fastapi import FastAPI

app = FastAPI()

# 기분을 저장할 빈 리스트
mood_list = []

@app.get("/")
def home():
    return {"message": "나의 기분 기록기에 오신 것을 환영합니다!"}

@app.get("/moods")
def get_moods():
    return mood_list

@app.post("/add-mood")
def add_mood(name: str, mood: str):
    entry = {"name": name, "mood": mood}
    mood_list.append(entry)
    return {"message": "저장 완료!", "data": entry}