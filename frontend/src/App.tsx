import React, { useEffect, useState } from 'react'
import './App.css'

// 기분 데이터의 형태를 정의합니다
interface Mood {
  id: number
  name: string
  mood: string
}

function App() {
  // 상태(State) 관리: 화면에 변하는 데이터를 담는 상자들입니다.
  const [moods, setMoods] = useState<Mood[]>([])  // 기분 목록 저장
  const [name, setName] = useState('')  // 입력 중인 이름
  const [mood, setMood] = useState('')  // 입력 중인 기분

  // 1. 서버에서 기분 목록을 가져오는 함수
  const fetchMoods = () => {
    fetch('http://127.0.0.1:8000/moods')
      .then(res => res.json())
      .then(data => setMoods(data))
  }

  // 앱이 처음 켜질 때 목록을 가져옵니다.
  useEffect(() => {
    fetchMoods()
  }, [])

  // 2. 새로운 기분을 서버에 보내는 함수
  const handleSubmit = async (e: React.SubmitEvent) => {
    e.preventDefault(); // 페이지 새로고침 방지

    await fetch('http://127.0.0.1:8000/moods', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, mood })  // 입력한 이름과 기분을 JSON으로 변환  
    })

    setName('')
    setMood('')
    fetchMoods()
  }

  return (
    <div style={{ padding: '20px', fontFamily: 'sans-serif' }}>
      <h1>🌈 오늘의 기분 기록기</h1>
      
      {/* 입력 양식 */}
      <form onSubmit={handleSubmit} style={{ marginBottom: '20px' }}>
        <input 
          placeholder="이름" 
          value={name} 
          onChange={(e) => setName(e.target.value)} 
        />
        <input
          placeholder="지금 기분은?" 
          value={mood} 
          onChange={(e) => setMood(e.target.value)} 
        />
        <button type="submit">기록하기</button>
      </form>

      {/* 목록 출력 */}
      <ul>
        {moods.map((item) => (
          <li key={item.id}>
            <strong>{item.name}</strong>님은 지금 <strong>{item.mood}</strong>
          </li>
        ))}
      </ul>
    </div>
  )
}

export default App
