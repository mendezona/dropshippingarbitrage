import '@/app/globals.css';
import { PROJECT_NAME } from '@/components/constants';
import { figtree } from '@/components/fonts';
import { ThemeProvider } from '@/components/theme-provider';
import { cn } from '@/lib/utils';
import { Metadata } from 'next';

export const metadata: Metadata = {
  title: {
    template: `%s |${PROJECT_NAME}`,
    default: `${PROJECT_NAME}`,
  },
  description: 'Next generation automated dropshipping',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body
        className={cn(
          'min-h-screen bg-background font-sans antialiased',
          figtree.variable
        )}
      >
        <ThemeProvider
          attribute="class"
          defaultTheme="system"
          enableSystem
          disableTransitionOnChange
        >
          {children}
        </ThemeProvider>
      </body>
    </html>
  );
}
