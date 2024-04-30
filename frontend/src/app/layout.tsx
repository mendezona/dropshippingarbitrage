import '@/app/globals.css';
import { projectName } from '@/components/constants';
import { figtree } from '@/components/fonts';
import { cn } from '@/lib/utils';
import { Metadata } from 'next';

export const metadata: Metadata = {
  title: {
    template: `%s |${projectName}`,
    default: `${projectName}`,
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
        {children}
      </body>
    </html>
  );
}
