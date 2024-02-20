"use client";
import { deleteConversation, fetchChatSummary } from "@/utils/api"
import { useRouter } from 'next/navigation';
import Link from "next/link"
import { useState } from "react"

interface DashboardFormProps {
    convo: {
        id: string
        name: string
        params: []
        tokens: number
    }[]
}

export const DashboardForm = ({convo} : DashboardFormProps) => {
    const router = useRouter();
    const [convos, setConvos] = useState(convo);
    async function deleteChat(id: string) {
        router.push('/dashboard')
        await deleteConversation(id);
        const newConvo = await fetchChatSummary();
        setConvos(newConvo);
        router.push('/dashboard')
    }

    return (
        <div className="w-full min-h-[300px] max-h-[600px] justify-center items-center p-10 overflow-auto border-cyan-900 border-2 rounded-xl gap-4">
            {
                convos?.map((c) => {
                    return (
                        <Link key={c.id} 
                            href={`/chat/${c.id}`}
                            className="flex w-full relative flex-col justify-center items-center p-10 border-cyan-900 border-2 rounded-xl hover:bg-cyan-900"
                            replace
                            >
                            <div className="absolute left-0 top-0 p-2 border-red-300 border-2 rounded-tl-xl rounded-br-xl hover:bg-red-600"
                                onClick={() => deleteChat(c.id)}
                            >
                                X
                            </div>
                            <h1>{c.name}</h1>
                            <p>Number of tokens: {c.tokens}</p>
                        </Link>
                    );
                })
            }
        </div>
    );
}