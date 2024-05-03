'use client';

import { Button } from '@/components/ui/button';
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from '@/components/ui/card';
import { signIn, signOut, useSession } from 'next-auth/react';
import Link from 'next/link';

export default function LoginPage() {
  return (
    <main className="flex items-center justify-center md:h-screen">
      <Card className="mx-auto max-w-sm">
        <CardHeader>
          <CardTitle className="text-2xl">Login</CardTitle>
          <CardDescription>
            Login with your Discord credentials to access your account
          </CardDescription>
        </CardHeader>
        <CardContent>
          <div className="grid gap-4">
            <Button
              variant="outline"
              className="w-full bg-discord text-white hover:bg-discordHover hover:text-white"
              onClick={() => signIn('discord')}
            >
              Login with Discord
            </Button>
          </div>
        </CardContent>
      </Card>
    </main>
  );
}
