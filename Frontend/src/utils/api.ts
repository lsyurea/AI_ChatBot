const backEndAPI: string = "http://ai_app:80";

// This function sends a POST request to the backend API with the user's input
export const fetchResponseFromUserInput = async (input: string, id: string) => {
    try {
        const queryParams = new URLSearchParams({ id: id });
        const res = await fetch(`${backEndAPI}/queries?${queryParams}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ 
                "role": "user", 
                "content": input
                
            }),
            cache: 'no-store' 
        });

        if (!res.ok) {
            throw new Error("Network response was not ok");
        }

        const data = await res.json();
        console.log(data)
        return data || "No response";
        
    } catch (error) {
        console.error("There was an error!", error);
    }
}

// This function retrieves the chat history from the backend API
export const fetchChatHistory = async (id: string) => {
    try {
        const res = await fetch(`${backEndAPI}/conversations/${id}`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
            cache: 'no-store' 
        });

        if (!res.ok) {
            throw new Error("Network response was not ok");
        }

        const data = await res.json();
        return data || "No response";
        
    } catch (error) {
        console.error("There was an error!", error);
    }
}

// This function retrieves the chat summary from the backend API
export const fetchChatSummary = async () => {
    try {
        const res = await fetch(`${backEndAPI}/conversations`, {
            method: "GET",
            cache: 'no-store' 
        });

        if (!res.ok) {
            throw new Error("Network response was not ok");
        }

        const data = await res.json();
        return data || "No response";
        
    } catch (error) {
        console.error("There was an error!", error);
    }
}

// This function creates new conversation in the backend API
export const createNewConversation = async (post: any) => {
    try {
        const res = await fetch(`${backEndAPI}/conversations/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(post),
            cache: 'no-store' 
        });

        if (!res.ok) {
            throw new Error("Network response was not ok");
        }

        const data = await res.json();
        return data || "No response";
        
    } catch (error) {
        console.error("There was an error!", error);
    }
}

// This function modifies the conversation in the backend API
export const modifyConversation = async (id: string, post: any) => {
    try {
        const res = await fetch(`${backEndAPI}/conversations/${id}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(post),
            cache: 'no-store' 
        });

        if (!res.ok) {
            throw new Error("Network response was not ok");
        }

        const data = await res.json();
        return data || "No response";
        
    } catch (error) {
        console.error("There was an error!", error);
    }
}

// This function deletes the conversation in the backend API
export const deleteConversation = async (id: string) => {
    try {
        const res = await fetch(`${backEndAPI}/conversations/${id}`, {
            method: "DELETE",
            cache: 'no-store' 
        });

        if (!res.ok) {
            throw new Error("Network response was not ok");
        }

        const data = await res.json();
        return data || "No response";
        
    } catch (error) {
        console.error("There was an error!", error);
    }
}

// do a status call
export const statusCheck = async () => {
    try {
        const res = await fetch(`${backEndAPI}/`, {
            method: "GET",
            cache: 'no-store' 
        });

        if (!res.ok) {
            throw new Error("Network response was not ok");
        }

        const data = await res.json();
        return data || "No response";
        
    } catch (error) {
        console.error("There was an error!", error);
    }
}