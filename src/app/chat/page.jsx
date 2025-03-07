"use client"

import Navbar from '@/components/Navbar'
import ChatArea from '@/components/ChatArea'
import { useState } from 'react'
const Chat = () => {
  const [userPersonality , setUserPersonality] = useState()
  return (
    <div className='w-screen h-screen bg-background max-h-screen'>
      <Navbar setUserPersonality={setUserPersonality}/>
      <ChatArea userPersonality={userPersonality}/>
    </div>
  )
}

export default Chat
