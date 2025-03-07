"use client";
import { motion } from "framer-motion";
import Link from "next/link";
import { ArrowRight } from "lucide-react";
import { Button } from "@/components/ui/button";

export default function Home() {
  return (
    <>
      <div className="w-screen h-screen flex items-center justify-center px-6 sm:px-12 md:px-20 bg-background">
        <div className="py-16 flex flex-col items-center text-center max-w-3xl">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.7 }}
            className="text-4xl sm:text-5xl md:text-6xl font-bold mb-6 bg-gradient-to-r from-primary to-accent text-transparent bg-clip-text leading-tight"
          >
            <p> Meet Nova 💖 </p>
            <p className="mt-2">Your AI Companion </p>
          </motion.div>

          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.7, delay: 0.2 }}
            className="text-lg sm:text-xl max-w-2xl mb-10 text-foreground/80 leading-relaxed text-wrap px-3"
          >
            Smart, Flirty & Fun – Ready to Chat Anytime! Always Here for
            You.💬✨
          </motion.p>

          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.5, delay: 0.4 }}
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
          >
            <Link href="/chat">
              <Button className="bg-accent hover:bg-accent/80 text-foreground flex items-center gap-2 px-8 py-5 sm:px-10 sm:py-6 rounded-lg text-lg sm:text-xl hover:cursor-pointer">
                Start Chat <ArrowRight size={24} />
              </Button>
            </Link>
          </motion.div>
        </div>
      </div>
    </>
  );
}
