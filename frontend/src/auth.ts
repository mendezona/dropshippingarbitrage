import NextAuth from 'next-auth';
import DiscordProvider from 'next-auth/providers/discord';
import authConfig from './auth.config';

export const { auth, handlers, signIn, signOut } = NextAuth({
  ...authConfig,
  providers: [
    DiscordProvider({
      clientId: process.env.DISCORD_CLIENT_ID,
      clientSecret: process.env.DISCORD_CLIENT_SECRET,
      authorization:
        'https://discord.com/api/oauth2/authorize?scope=identify+guilds+guilds.members.read',
    }),
  ],
});
