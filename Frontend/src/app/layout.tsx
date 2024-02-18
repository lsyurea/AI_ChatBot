import type { Metadata } from "next";
import { MantineProvider } from "@mantine/core";
import { Inter } from "next/font/google";
import { Sidebar } from "@/components/sidebar/sidebar";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "AI Chatbot",
  description: "One stop solution for all your queries",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <MantineProvider>
          <div className="flex">
            <Sidebar />
            {children}
          </div>

        </MantineProvider>
      </body>
    </html>
  );
}
