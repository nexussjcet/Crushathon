"use client";

import { useEffect, useRef } from "react";
import { motion } from "framer-motion";
import { Sparkles } from "lucide-react";
import MessageCard from "./MessageCard";
import { getTime } from "@/lib/getTime";

const MessageArea = ({ messages, loading }) => {
  const scrollRef = useRef(null);

  useEffect(() => {
    scrollRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  return (
    <div className="h-[540px] w-full overflow-y-auto p-2 space-y-3">
      {!messages.length && (
        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.5 }}
          className="text-center text-foreground/90"
        >
          No messages to show
        </motion.p>
      )}

      {messages.map((msg, index) => {
        const isUser = msg.role === "user";
        const time = getTime();

        return (
          <motion.div
            key={index}
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.4, delay: index * 0.1 }}
          >
            <MessageCard msg={msg} isUser={isUser} time={time} />
          </motion.div>
        );
      })}

      {loading && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{
            duration: 0.5,
            repeat: Infinity,
            repeatType: "reverse",
          }}
          className="text-foreground/40 flex items-start justify-start gap-3"
        >
          <Sparkles size={30} className="text-primary" />{" "}
          <p>Nova is typing...</p>
        </motion.div>
      )}

      <div ref={scrollRef} />
    </div>
  );
};

export default MessageArea;
