"use client";
import { useState } from 'react';
import Link from 'next/link';
import { UnstyledButton, Tooltip, Title, rem } from '@mantine/core';
import {
  IconHome2,
  IconGauge,
  IconDeviceDesktopAnalytics,
  IconFingerprint,
  IconCalendarStats,
  IconUser,
  IconSettings,
} from '@tabler/icons-react';

const mainLinksMockdata = [
  { icon: IconHome2, label: 'Home' },
  { icon: IconGauge, label: 'Dashboard' },
  { icon: IconDeviceDesktopAnalytics, label: 'Analytics' },
  { icon: IconCalendarStats, label: 'Releases' },
  { icon: IconUser, label: 'Account' },

];

const linksMockdata = [
  'Dashboard',
  'Chat',
  'Account',
];

export function Sidebar() {
  const [activeLink, setActiveLink] = useState('Settings');

  const links = linksMockdata.map((link) => (
    <Link
      className={`block no-underline rounded-tr-[var(--mantine-radius-md)] rounded-br-[var(--mantine-radius-md)] px-12 py-8 color-[light-dark(var(--mantine-color-gray-7),
        var(--mantine-color-dark-0))] hover:bg-[light-dark(var(--mantine-color-gray-0), var(--mantine-color-dark-5))] transition-colors
        ${link === activeLink ? 'bg-[var(--mantine-color-blue-light)] color-[var(--mantine-color-blue-light-color)]' : ''}`}
      href="#"
      onClick={(event) => {
        event.preventDefault();
        setActiveLink(link);
      }}
      key={link}
    >
      {link}
    </Link>
  ));

  return (
    <nav className="bg-light-dark(white, dark-6) h-[750px] w-[300px] flex flex-col border-r border-solid border-gray-300 dark:border-dark-4">
      <div className={`flex flex-1`}>

        <div className={`flex-1 bg-[light-dark(var(--mantine-color-gray-0), var(--mantine-color-dark-6))]`}>
          <Title order={4} className="font-greycliff-cf var(--mantine-font-family) mb-8 bg-body p-4 pt-[18px] h-[60px] border-b border-solid border-gray-300 dark:border-dark-7">
            AIBot
          </Title>

          {links}
        </div>
      </div>
    </nav>
  );
}