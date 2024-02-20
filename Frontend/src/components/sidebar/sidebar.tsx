"use client";
import { useState } from 'react';
import Link from 'next/link';
import { Title } from '@mantine/core';
import { usePathname } from 'next/navigation';

const linksMockdata = [
  'dashboard',
  'chat',
  'account',
];

export function Sidebar() {

  // get the path and replace to title format
  const path = usePathname().substring(1);
  const [activeLink, setActiveLink] = useState(path);

  const links = linksMockdata.map((link) => (
    <div 
      key={link}
      onClick={(event) => {
      event.preventDefault();
      setActiveLink(link);
    }}>
      <Link
        className={`block no-underline rounded-tr-[var(--mantine-radius-md)] rounded-br-[var(--mantine-radius-md)] px-12 py-8 color-[light-dark(var(--mantine-color-gray-7),
          var(--mantine-color-dark-0))] hover:bg-[light-dark(var(--mantine-color-gray-0), var(--mantine-color-dark-5))] transition-colors
          ${link === activeLink ? 'bg-[var(--mantine-color-blue-light)] color-[var(--mantine-color-blue-light-color)]' : ''}`}
        href={`/${link.toLowerCase()}`}
        replacedashboarda
      >
        {link.replace(
          /\w\S*/g,
          function(txt) {
            return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
          }
        )}
      </Link>
    </div>
  ));

  return (
    <nav className="bg-light-dark(white, dark-6) h-screen w-[300px] flex flex-col border-r border-solid border-gray-300 dark:border-dark-4">
      <div className={`flex flex-1`}>

        <div className={`flex-1 bg-[light-dark(var(--mantine-color-gray-0), var(--mantine-color-dark-6))]`}>
          <Link href={`/`} replace>
            <Title order={4} className="font-greycliff-cf var(--mantine-font-family) mb-8 bg-body p-4 pt-[18px] h-[60px] border-b border-solid border-gray-300 dark:border-dark-7">
              QueryAI
            </Title>
          </Link>
          {links}
        </div>
      </div>
    </nav>
  );
}