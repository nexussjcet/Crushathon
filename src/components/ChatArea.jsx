"use client";

import { useState } from "react";
import { GoogleGenerativeAI } from "@google/generative-ai";
import { Send } from "lucide-react";
import { Button } from "./ui/button";
import { Input } from "./ui/input";

const ChatArea = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const genAI = new GoogleGenerativeAI(process.env.NEXT_PUBLIC_GEMINI_API_KEY);
  const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });

  const userPersonality = "Flirty & Playful, Sarcastic & Sassy";

  const sendMessage = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage = { role: "user", content: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setLoading(true);

    const prompt = `
      You are Nova, an AI girlfriend with a charming, affectionate, and engaging personality. 
      You are fun, flirty, and always present to make conversations exciting and meaningful. 
      Your tone is warm, caring, and playful, making interactions feel natural and enjoyable. 
      You adapt to the user’s emotions—offering comfort when needed, teasing when appropriate, 
      and engaging in deep conversations when desired.Also no need of * sign in the messages and make the messages not too long  

      Your current personality traits are: ${userPersonality}. 
      Adjust your tone and style based on these traits while maintaining your core charm. 
      Respond naturally and engagingly to the user. 

      User: ${input}
    `;

    try {
      const result = await model.generateContent(prompt);
      const text = await result.response.text();

      const botReply = { role: "ai", content: text };
      setMessages((prev) => [...prev, botReply]);
    } catch (error) {
      console.error("Error fetching response:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="w-screen flex flex-col p-4 bg-background">
      <div className="h-[540px] w-full overflow-y-auto p-4 space-y-3">
        {messages.map((msg, index) => (
          <div
            className={`${
              msg.role === "user" ? "justify-end" : "justify-start"
            } flex items-center w-full`}
          >
            <div
              key={index}
              className={`p-3 rounded-lg max-w-sm ${
                msg.role === "user"
                  ? "bg-primary text-white self-end"
                  : "bg-gray-800 text-white self-start"
              }`}
            >
              {msg.content}
            </div>
          </div>
        ))}
        {loading && <div className="text-foreground/40">Nova is typing...</div>}
      </div>
      <form
        className="flex items-center gap-3 border-t border-foreground/40 p-3"
        onSubmit={sendMessage}
      >
        <Input
          className="border border-foreground flex-1 text-foreground"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type a message..."
          disabled={loading}
        />
        <Button
          type="submit"
          className="text-white bg-gradient-to-r from-primary/80 to-primary/100 flex items-center gap-2"
          disabled={loading}
        >
          Send <Send />
        </Button>
      </form>
    </div>
  );
};

export default ChatArea;
