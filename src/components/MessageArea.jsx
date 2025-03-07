"use client";

import { useEffect, useRef } from "react";
import { User, Sparkles } from "lucide-react";
import MessageCard from "./MessageCard";

const MessageArea = ({ messages, loading }) => {
  const scrollRef = useRef(null);

  useEffect(() => {
    scrollRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  return (
    <div className="h-[540px] w-full overflow-y-auto p-2 space-y-3">
      {!messages && (
        <p className="text-center text-foreground/90 ">No messages to show</p>
      )}
      {messages.map((msg, index) => {
        const isUser = msg.role === "user";
        const time = new Date().toLocaleTimeString([], {
          hour: "2-digit",
          minute: "2-digit",
        });

        return (
          <MessageCard key={index} msg={msg} isUser={isUser} time={time} />
        );
      })}

      {loading && (
        <div className="text-foreground/40 flex items-start justify-start gap-3">
          <Sparkles size={30} className="text-primary" />{" "}
          <p>Nova is typing...</p>
        </div>
      )}
      <div ref={scrollRef} />
    </div>
  );
};

export default MessageArea;
