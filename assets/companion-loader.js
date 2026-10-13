const host = document.querySelector('[data-companion]');
if (host) {
  let started = false;
  const load = async () => {
    if (started) return;
    started = true;
    try {
      const { mountCompanion } = await import('./companion.js');
      mountCompanion(host);
    } catch {
      // The original SVG remains visible if WebGL or the module is unavailable.
      host.classList.add('companion-fallback');
    }
  };
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => {
      if (entries.some(entry => entry.isIntersecting)) { observer.disconnect(); load(); }
    }, { rootMargin: '250px' });
    observer.observe(host);
  } else load();
}
