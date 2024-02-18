"use client";
import { useState } from 'react';
import { fetchResponseFromUserInput } from '@/utils/api';

export function ChatForm() {
  const [input, setInput] = useState('');
  const [response, setResponse] = useState<string[]>([]);

  const handleSubmit = async (event: { preventDefault: () => void; }) => {
    event.preventDefault();
    const data = await fetchResponseFromUserInput(input);

    setResponse([...response, data]);
  };

  return (
    <div className='flex w-full flex-col justify-start items-center p-10 gap-4'>
        <div className='h-5/6 w-full border-cyan-900 border-2 rounded-xl overflow-y-auto'>
            {response.map((message, index) => (
                <div key={index} className='bg-cyan-900 text-white p-2 rounded-xl m-2'>
                    {message}
                </div>))
            }
        </div>

        <form
            className='flex h-1/6 w-full border-cyan-900 border-2 rounded-xl gap-4' 
            onSubmit={handleSubmit}>
            <input
                className='basis-5/6 bg-transparent'
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