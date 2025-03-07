import { ArrowLeft, Sparkles, Settings } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Avatar } from "@/components/ui/avatar";
import { AvatarImage, AvatarFallback } from "@/components/ui/avatar";
import Link from "next/link";
const Navbar = () => {
  return (
    <>
      <header className="w-screen border-b border-muted p-4 bg-background">
        <div className="mx-auto flex justify-between items-center">
          <div className="flex items-center gap-3">
            <Link href="/" className="sm:block hidden" >
              <Button
                variant="ghost"
                size="icon"
                className="text-foreground  hover:bg-foreground/20 hover:cursor-pointer"
              >
                <ArrowLeft className="h-5 w-5" />
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
          <Button
            variant="ghost"
            size="icon"
            className="text-foreground hover:bg-foreground/20 hover:cursor-pointer"
          >
            <Settings className="h-7 w-7" />
          </Button>
        </div>
      </header>
    </>
  );
};

export default Navbar;
