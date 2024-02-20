import { DashboardForm } from "@/components/formComponents/dashboardform";
import { fetchChatSummary } from "@/utils/api";



export default async function Chat() {
    
    const convos = await fetchChatSummary();
    
    return (
        <div className="flex w-full flex-col justify-center items-center p-10">
            <h1>Topics that you have created before:</h1>
            <DashboardForm convo={convos}/>
        </div>
    );
}