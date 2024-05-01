'use client';

import { signIn, signOut, useSession } from 'next-auth/react';

export default function LoginPage() {
  return (
    <main className="flex items-center justify-center md:h-screen">
      <div className="relative mx-auto flex w-full max-w-[400px] flex-col space-y-2.5 p-4 md:-mt-32">
        <button onClick={() => signIn('discord')}>Sign in with Discord</button>
      </div>
    </main>
  );
}
