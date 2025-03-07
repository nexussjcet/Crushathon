"use client";
import { easeInOut, motion } from "framer-motion";
import Link from "next/link";
import { ArrowRight, MessageCircle, Sparkles, Shield } from "lucide-react";
import { Button } from "@/components/ui/button";

export default function Home() {
  return (
    <>
      <div className="w-screen h-screen flex items-center justify-center flex-wrap bg-background">
        <div className="py-20 flex flex-col items-center text-center">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.7 }}
            className="text-4xl sm:text-5xl md:text-6xl px-2 font-bold mb-6 bg-gradient-to-r from-primary to-accent text-transparent bg-clip-text"
          >
            <p> Meet Nova 💖 </p> <div className="flex items-center justify-center gap-2">
            <p>Your AI Companion</p> <p className="hidden sm:block">, Always Here for You.</p>
            </div>
          </motion.div>

          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.7, delay: 0.2 }}
            className="text-xl max-w-2xl mb-10 text-foreground/80"
          >
            Smart, Flirty & Fun-Ready to Chat Anytime! 💬✨
          </motion.p>

          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.5, delay: 0.4 }}
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
          >
            <Link href="/chat">
              <Button className="bg-accent hover:bg-accent/80 hover:cursor-pointer text-foreground flex items-center justify-center gap-2 px-10 py-6 rounded-lg text-lg">
                Start Chat <ArrowRight size={30} />
              </Button>
            </Link>
          </motion.div>
        </div>
      </div>
    </>
  );
}
