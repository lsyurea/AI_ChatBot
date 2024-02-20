import Link from "next/link"

interface DashboardFormProps {
    convo: {
        id: string
        name: string
        params: []
        tokens: number
    }[]
}

export const DashboardForm = ({convo} : DashboardFormProps) => {
    return (
        <div className="w-full min-h-[300px] max-h-[600px] justify-center items-center p-10 overflow-auto border-cyan-900 border-2 rounded-xl gap-4">
            {
                convo?.map((c) => {
                    return (
                        <Link key={c.id} 
                            href={`/chat/${c.id}`}
                            className="flex w-full flex-col justify-center items-center p-10 border-cyan-900 border-2 rounded-xl hover:bg-cyan-900"
                            >
                            <h1>{c.name}</h1>
                            <p>Number of tokens: {c.tokens}</p>
                        </Link>
                    );
                })
            }
        </div>
    );
}