"use client";

import { createNewConversation } from '@/utils/api';
import { useRouter } from 'next/navigation';
import React, { useState } from 'react';

export const CreateChatForm = () => {
    const [name, setName] = useState('');
    const router = useRouter();

    const handleSubmit = async (event: React.FormEvent) => {
        event.preventDefault();
        // Do something with the name
        const data = await createNewConversation({name});
        router.push(`/chat/${data?.id}`);
    };

    const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setName(event.target.value);
    };

    return (
        <form onSubmit={handleSubmit} className='flex flex-col border-cyan-900 border-2 rounded-xl gap-4 w-[300px]'>
            <input type="text" value={name} onChange={handleChange} placeholder='Create a new topic' className='text-center bg-transparent'/>
            <button type="submit" className='bg-cyan-900'>Submit</button>
        </form>
    );
};