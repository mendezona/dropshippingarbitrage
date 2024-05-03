import { Button } from '@/components/ui/button';
import Link from 'next/link';

export default function Page() {
  return (
    <main className="flex min-h-screen flex-col p-6 items-center justify-center">
      <div className="flex flex-col items-center text-center">
        <h1 className="text-6xl font-bold text-gray-800 mt-2 mb-4 px-4 py-2">
          BuyBridge
        </h1>
        <h3 className="text-3xl font-semibold text-gray-600 mt-2 mb-4 px-4 py-2">
          Seamlessly Connect, Effortlessly Shop
        </h3>
        <p className="text-lg text-gray-600 mt-6 max-w-2xl">
          Welcome to BuyBridge, your ultimate solution for the best shopping
          experience. With BuyBridge, we bridge the gap between retailers,
          empowering you to shop effortlessly across multiple platforms. Say
          goodbye to the hassle of switching between stores - BuyBridge
          synchronizes your shopping journey, making it easier than ever to find
          and purchase your favorite products. Whether you're a frequent online
          shopper or a busy professional, BuyBridge optimizes the process,
          ensuring every purchase is smooth and convenient. Join the BuyBridge
          community today and discover a new era of stress-free shopping!
        </p>
        <p className="text-lg text-gray-600 mt-4 max-w-2xl">
          With our innovative platform, you'll never miss out on a great deal
          again. Whether you're searching for electronics, fashion, home goods,
          or more, BuyBridge ensures that you find the best offers from trusted
          retailers, all in one place. Experience hassle-free shopping and make
          every purchase with confidence.
        </p>
        <div className="flex flex-col items-center mt-8">
          <Button className="w-full max-w-xs" disabled>
            Coming Soon
          </Button>
          <Link
            href="/login"
            className="mt-4 w-full max-w-xs flex items-center justify-center rounded-lg bg-blue-500 px-6 py-3 text-sm font-medium text-white transition-colors hover:bg-blue-400 md:text-base"
          >
            Log in
          </Link>
        </div>
      </div>
    </main>
  );
}
