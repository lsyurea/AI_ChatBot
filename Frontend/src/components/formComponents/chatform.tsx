"use client";
import React, { useState } from 'react';
import { fetchChatHistory, fetchResponseFromUserInput } from '@/utils/api';

interface ChatFormProps {
    chatHistory: {
        _id: string
        name: string
        messages: {
            role: string
            content: string
        }[]
    }
}

const ChatForm: React.FC<ChatFormProps> = ({chatHistory}) => {
    
    const [input, setInput] = useState('');
    const [name, setName] = useState(chatHistory?.name || '');
    const [response, setResponse] = useState<string[]>(chatHistory?.messages?.map((x: { role: string, content: string; })=> x?.content)
        ||[]);

    const handleSubmit = async (event: any) => {
        event.preventDefault();
        const data = await fetchResponseFromUserInput(input, chatHistory._id);
        if (data) {
            console.log(data.id);
            const chatHistory = await fetchChatHistory(data.id);
            setResponse(chatHistory?.messages?.map((x: { role: string, content: string; })=> x?.content)
        ||[])
        }
    };

    return (
        <div className='flex w-full flex-col justify-start items-center p-10 gap-4'>
            <h1 className='w-full h-[50px] text-white'>Your current chat: <span className="font-bold">{name}</span></h1>

            <div className='h-5/6 w-full border-cyan-900 border-2 rounded-xl overflow-y-auto'>
                {response.map((message, index) => (
                    <div key={index} className='bg-cyan-900 text-white p-2 rounded-xl m-2'>
                        {message}
                    </div>))
                }
            </div>

            <form
                className='flex h-[80px] w-full border-cyan-900 border-2 rounded-xl gap-4' 
                onSubmit={handleSubmit}>
                <input
                    className='text-center basis-5/6 bg-transparent'
                    type="text"
                    placeholder="Type a message..."
                    value={input}
                    onChange={(event) => setInput(event.target.value)}
                />
                <button type="submit" className='bg-cyan-900 basis-1/6'>Send</button>
            </form>
        </div>
    );
}

export { ChatForm };