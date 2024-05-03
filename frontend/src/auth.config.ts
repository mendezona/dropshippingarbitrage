import { NextAuthConfig } from 'next-auth';

export const authConfig = {
  callbacks: {
    authorized({ auth, request: { nextUrl } }) {
      const isLoggedIn = !!auth?.user;
      const unprotectedPaths = ['/login', '/'];
      const isProtected = !unprotectedPaths.some((path) =>
        nextUrl.pathname.startsWith(path)
      );

      if (isProtected && !isLoggedIn) {
        const redirectUrl = new URL('/login', nextUrl.origin);
        redirectUrl.searchParams.append('callbackUrl', nextUrl.href);
        return Response.redirect(redirectUrl);
      }

      return true;
    },
    async signIn({ user, account, profile, email, credentials }) {
      if (account?.provider === 'discord') {
        const accessToken = account.access_token;

        // Fetch guilds from Discord
        const response = await fetch(
          'https://discord.com/api/users/@me/guilds',
          {
            headers: {
              Authorization: `Bearer ${accessToken}`,
            },
          }
        );

        const guilds = await response.json();

        // Define the ID of the guild the user must be part of
        const requiredGuildId = process.env.DISCORD_DROPSHIPPING_SERVER_ID; // Replace with your actual guild ID

        console.log('guilds', guilds);

        // Check if user is part of the required guild
        const isMember = guilds.some(
          (guild: any) => guild.id === requiredGuildId
        );
        if (isMember) {
          return true;
        } else {
          return false;
        }
      }
      return true;
    },
  },
  providers: [],
} satisfies NextAuthConfig;

export default authConfig;
