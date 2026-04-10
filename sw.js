const CACHE_NAME = 'flota-mvp-v1';
const SHELL_ASSETS = [
  './',
  './index.html',
  './manifest.json',
  './icons/icon-192.png',
  './icons/icon-512.png'
];

// Instalar: cachear el shell de la app
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(SHELL_ASSETS))
  );
  self.skipWaiting();
});

// Activar: borrar caches viejas
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
});

// Fetch: network-first para AppSheet, cache-first para assets locales
self.addEventListener('fetch', event => {
  const url = new URL(event.request.url);

  // Assets locales del shell → cache first
  if (url.origin === self.location.origin) {
    event.respondWith(
      caches.match(event.request).then(cached => cached || fetch(event.request))
    );
    return;
  }

  // AppSheet y cualquier recurso externo → network first, sin bloquear en fallo
  event.respondWith(
    fetch(event.request).catch(() =>
      caches.match('/index.html')
    )
  );
});
