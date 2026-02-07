# 데이터의 규칙 정하기
# pydantic이라는 라이브러리에서 BaseModel을 가져옵니다. 
# 이것은 데이터의 "틀"을 만드는 도구입니다.
from pydantic import BaseModel

# 사용자가 기분을 보낼 때 지켜야 할 규칙입니다.
class MoodCreate(BaseModel):
    name: str   # 이름은 문자열(String)이어야 함
    mood: str   # 기분 내용도 문자열이어야 함

# 서버가 사용자에게 데이터를 보여줄 때의 규칙입니다.
class MoodResponse(BaseModel):
    id: int     # 각 기분 데이터의 고유 번호
    name: str
    mood: str
