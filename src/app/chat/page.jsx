import {motion} from 'framer-motion'
import Navbar from '@/components/Navbar'
import ChatArea from '@/components/ChatArea'
const Chat = () => {
  return (
    <div className='w-screen h-screen bg-background max-h-screen'>
      <Navbar/>
      <ChatArea/>
    </div>
  )
}

export default Chat
