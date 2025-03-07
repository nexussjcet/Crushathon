import React from "react";
import { User, Sparkles } from "lucide-react";

const MessageCard = ({msg , isUser , time}) => {
  return (
    <div
      className={`flex w-full items-center ${
        isUser ? "justify-end" : "justify-start"
      }`}
    >
      <div
        className={`flex items-start  justify-center gap-2  ${
          isUser ? "flex-row-reverse" : "flex-row"
        }`}
      >
        {!isUser ? (
          <Sparkles size={25} className=" text-primary " />
        ) : (
          <User size={25} className=" text-foreground " />
        )}
        <div
          className={`p-3 rounded-lg max-w-[200px] md:max-w-[320px] relative ${
            isUser
              ? "bg-pink-600 text-foreground self-end"
              : "bg-muted text-white self-start"
          }`}
        >
          {msg.content}
          <span
            className={`block text-xs ${
              !isUser ? "text-foreground/60" : "text-foreground/70"
            } mt-1`}
          >
            {time}
          </span>
        </div>
      </div>
    </div>
  );
};

export default MessageCard;
