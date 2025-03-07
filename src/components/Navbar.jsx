"use client"

import { ArrowLeft, Sparkles, Settings } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Avatar, AvatarFallback } from "@/components/ui/avatar";
import Link from "next/link";
import { motion } from "framer-motion";
const Navbar = ({ setUserPersonality }) => {
  return (
    <>
      <header className="w-screen border-b border-muted p-4 bg-background">
        <div className="mx-auto flex justify-between items-center">
          <div className="flex items-center gap-3">
            <Link href="/" className="sm:block hidden">
              <Button
                variant="ghost"
                size="icon"
                className="text-foreground hover:bg-foreground/20 hover:cursor-pointer"
              >
                <ArrowLeft size={30} />
              </Button>
            </Link>
            <div className="flex items-center gap-2">
              <Avatar className="h-8 w-8 border-2 border-primary">
                <AvatarFallback className="bg-muted">
                  <Sparkles className="h-6 w-6 text-primary" />
                </AvatarFallback>
              </Avatar>
              <span className="font-medium text-xl text-foreground">Nova</span>
            </div>
          </div>

          <div className="flex items-center gap-4">
            <div className="relative flex items-center justify-center gap-3 text-foreground">
              <p className="hidden sm:block">Personality : </p>
              <motion.select
                onChange={(e) => setUserPersonality(e.target.value)}
                className="bg-gray-800 text-foreground border border-gray-600 rounded-lg px-3 py-1 pr-8 min-w-[180px] md:min-w-[200px] focus:outline-none cursor-pointer appearance-none"
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
              >
                <option value="Flirty & Playful">Flirty & Playful</option>
                <option value="Sarcastic & Sassy">Sarcastic & Sassy</option>
                <option value="Sweet & Caring">Sweet & Caring</option>
                <option value="Mysterious & Enigmatic">Mysterious</option>
                <option value="Supportive & Encouraging">Supportive</option>
              </motion.select>
              <Settings
                size={20}
                className="absolute top-1/2 ml-6 right-3 transform -translate-y-1/2 text-foreground pointer-events-none"
              />
            </div>
          </div>
        </div>
      </header>
    </>
  );
};

export default Navbar;
