import { ChatForm } from "@/components/formComponents/chatform";
import { fetchChatHistory } from "@/utils/api";

export default async function Chat({params}: {params: {id: string}}) {
    const chatHistory = await fetchChatHistory(params.id);
    return (
        <ChatForm chatHistory={chatHistory}/>
    );
}