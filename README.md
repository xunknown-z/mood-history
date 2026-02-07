# 기분 기록기(moon history) 프로젝트

## 프로젝트 구조
```text
moon-history/
├── .gitignore
├── README.md
├── docker-compose.yml         # (선택) 컨테이너 실행용
│
├── backend/                   # FastAPI 프로젝트 루트
│   ├── app/
│   │   ├── main.py            # FastAPI 실행 엔트리포인트
│   │   ├── api/               # API 라우터 (v1, v2 등)
│   │   ├── core/              # 설정(config), 보안(auth)
│   │   ├── models/            # DB 테이블 정의 (SQLAlchemy/SQLModel)
│   │   ├── schemas/           # Pydantic 모델 (Request/Response)
│   │   └── crud/              # DB 조작 로직
│   ├── tests/                 # 백엔드 테스트 코드
│   ├── .env                   # 백엔드 환경변수
│   └── requirements.txt       # 의존성 관리
│
└── frontend/                  # React 프로젝트 루트 (Vite 사용 권장)
    ├── src/
    │   ├── api/               # Axios/Fetch 등 백엔드 호출 로직
    │   ├── components/        # 재사용 가능한 UI 컴포넌트
    │   ├── pages/             # 페이지 단위 컴포넌트
    │   └── App.tsx
    ├── public/
    ├── .env                   # 프론트엔드 환경변수 (API 주소 등)
    ├── package.json
    └── vite.config.ts
```

## frontend
### React + TS / Vite 사용

Vite를 사용하여 frontend 폴더 생성
**질문이 나오면 순서대로: React 선택 -> TypeScript 선택 (또는 JavaScript)**
```bash
npm create vite@latest frontend -- --template react-ts
```