// stealth.js
Object.defineProperty(navigator, 'webdriver', { get: () => false });
Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] });
Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3] });

window.chrome = {
  runtime: {}
};

Object.defineProperty(navigator, 'platform', { get: () => 'Win32' });
