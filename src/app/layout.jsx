import { Arimo } from "next/font/google";
import "./globals.css";

const arimo = Arimo({
  subsets: ["latin"], // ✅ Added subset to fix the font error
  variable: "--font-arimo",
});

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <title>Nova</title>
        <meta name="description" content="Your AI girlfriend" />
        <link rel="icon" href="/sparkles.png" />
      </head>
      <body className={`${arimo.variable} antialiased`}>
        {children}
      </body>
    </html>
  );
}
