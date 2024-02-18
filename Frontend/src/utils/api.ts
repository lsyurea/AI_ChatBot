const backEndAPI: string = "http://localhost:8000";

export const fetchResponseFromUserInput = async (input: string) => {
    try {
        console.log(input)
        const res = await fetch(`${backEndAPI}/queries/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ 
                "id": "550e8400-e29b-41d4-a716-446655440000",
                "name": "test",
                "params": {
                    "param1": "value1"
                },
                "tokens": 100,
                "messages": [
                    {"role": "user", "content": input}
                ]
            }),
        });

        if (!res.ok) {
            throw new Error("Network response was not ok");
        }

        const data = await res.json();
        console.log(data)
        return data?.content || "No response";
        
    } catch (error) {
        console.error("There was an error!", error);
    }
}