---
# Liquid-templated so the cache version bumps with each deploy
---
// Service worker for hunterdavis.com.
//
// Strategy:
//   - Network-first for HTML (so post updates are immediate)
//   - Stale-while-revalidate for CSS/JS/fonts (fast, but kept fresh)
//   - Cache-first for images (long-lived, big bandwidth saver offline)
//   - Network-only for search index, RSS feeds, sitemap, search-result
//     pages (always fresh / privacy-respecting)
//   - Offline fallback: a tiny inline page for navigation requests
//     that miss the cache when the network is unreachable
//
// Cache name embeds the site build time so a deploy invalidates the
// old caches automatically — no stuck-on-old-version surprises.

const VERSION = "{{ site.time | date: '%Y%m%d%H%M%S' }}";
const HTML_CACHE = "hd-html-" + VERSION;
const ASSET_CACHE = "hd-assets-" + VERSION;
const IMG_CACHE = "hd-img-" + VERSION;
const PRECACHE = [
  "/",
  "/css/style.css",
  "/fonts/vollkorn-latin.woff2",
  "/fonts/vollkorn-latin-italic.woff2",
  "/favicon.png",
  "/sharer.png"
];

self.addEventListener("install", function (event) {
  event.waitUntil(
    caches.open(ASSET_CACHE).then(function (c) { return c.addAll(PRECACHE); })
      .then(function () { return self.skipWaiting(); })
  );
});

self.addEventListener("activate", function (event) {
  event.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(keys.map(function (k) {
        if (k !== HTML_CACHE && k !== ASSET_CACHE && k !== IMG_CACHE) {
          return caches.delete(k);
        }
      }));
    }).then(function () { return self.clients.claim(); })
  );
});

function isHTML(req) {
  return req.mode === "navigate" ||
    (req.headers.get("accept") || "").indexOf("text/html") !== -1;
}
function isImage(req) {
  return req.destination === "image";
}
function isAsset(req) {
  return ["script", "style", "font"].indexOf(req.destination) !== -1;
}
function shouldBypass(url) {
  return url.pathname === "/search.json" ||
    url.pathname === "/sitemap.xml" ||
    url.pathname === "/feed.xml" ||
    url.pathname === "/feed-full.xml" ||
    url.pathname.indexOf("/search.html") === 0 ||
    url.pathname === "/random.html";
}

self.addEventListener("fetch", function (event) {
  var req = event.request;
  if (req.method !== "GET") return;
  var url = new URL(req.url);
  if (url.origin !== location.origin) return;
  if (shouldBypass(url)) return;

  if (isHTML(req)) {
    // Network-first: try the network, fall back to cache, then offline page
    event.respondWith(
      fetch(req).then(function (res) {
        var copy = res.clone();
        caches.open(HTML_CACHE).then(function (c) { c.put(req, copy); });
        return res;
      }).catch(function () {
        return caches.match(req).then(function (cached) {
          return cached || new Response(
            "<!doctype html><meta charset=utf-8><title>Offline</title>" +
            "<p style=\"font:1.2em/1.4 system-ui,sans-serif;max-width:32em;margin:4em auto;padding:0 1em\">" +
            "You're offline and this page isn't cached yet. Try again once you're back online.</p>",
            { headers: { "Content-Type": "text/html; charset=utf-8" } }
          );
        });
      })
    );
    return;
  }

  if (isImage(req)) {
    // Cache-first
    event.respondWith(
      caches.open(IMG_CACHE).then(function (c) {
        return c.match(req).then(function (cached) {
          if (cached) return cached;
          return fetch(req).then(function (res) {
            if (res.ok) c.put(req, res.clone());
            return res;
          });
        });
      })
    );
    return;
  }

  if (isAsset(req)) {
    // Stale-while-revalidate
    event.respondWith(
      caches.open(ASSET_CACHE).then(function (c) {
        return c.match(req).then(function (cached) {
          var fetched = fetch(req).then(function (res) {
            if (res.ok) c.put(req, res.clone());
            return res;
          }).catch(function () { return cached; });
          return cached || fetched;
        });
      })
    );
    return;
  }
});
