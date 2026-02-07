import { useEffect, useState } from 'react'
import './App.css'

function App() {
  const [message, setMessage] = useState('')

  useEffect(() => {
    // 백엔드 주소로 요청 보내기
    fetch('http://127.0.0.1:8000/')
      .then(res => res.json())
      .then(data => setMessage(data.message))
  }, [])

  return (
    <div>
      <h1>프론트엔드 화면</h1>
      <p>백엔드에서 온 메시지: {message}</p>
    </div>
  )
}

export default App
