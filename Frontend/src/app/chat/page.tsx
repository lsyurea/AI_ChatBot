import { CreateChatForm } from "@/components/formComponents/createchatform";
import { statusCheck } from "@/utils/api";


export default async function Chat() {
    return (
        <div className="flex w-full flex-col justify-center items-center p-10">
            <h1>Please create a new Chat</h1>
            <CreateChatForm />
        </div>
    );
}