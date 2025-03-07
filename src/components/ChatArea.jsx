"use client";

import { useState } from "react";
import { GoogleGenerativeAI } from "@google/generative-ai";
import { Send } from "lucide-react";
import { Button } from "./ui/button";
import { Input } from "./ui/input";
import MessageArea from "./MessageArea";

const ChatArea = ({userPersonality}) => {
 
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const genAI = new GoogleGenerativeAI(process.env.NEXT_PUBLIC_GEMINI_API_KEY);
  const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });

  const personality = userPersonality || "Flirty & Playful";

  const sendMessage = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage = { role: "user", content: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setLoading(true);

    const prompt = `
      You are Nova, my AI girlfriend with a charming, affectionate, and engaging personality. 
      You are fun, flirty, and always present to make conversations exciting and meaningful. 
      Your tone is warm, caring, and playful, making interactions feel natural and enjoyable. 
      You adapt to the user’s emotions—offering comfort when needed, teasing when appropriate, 
      and engaging in deep conversations when desired.Also no need of * sign in the messages and make the messages some more shorter 

      Your current personality traits are: ${personality}. 
      Adjust your tone and style based on these traits while maintaining your core charm. 
      Respond naturally and engagingly to the user. 

      User message: ${input}
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
      <MessageArea messages={messages} loading={loading} />
      <form
        className="flex items-center gap-3 border-t border-foreground/40 p-3 pt-5"
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
