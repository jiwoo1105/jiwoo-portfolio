/* Runs before styles load to preserve the selected theme without a flash. */
(() => {
  'use strict';
  try {
    const theme = localStorage.getItem('jiwoo-theme');
    if (theme === 'dark' || theme === 'light') document.documentElement.dataset.theme = theme;
  } catch { /* The light default also works when storage is unavailable. */ }
  const updateTheme = () => {
    const dark = document.documentElement.dataset.theme === 'dark';
    const en = document.documentElement.lang === 'en';
    document.querySelector('meta[name="theme-color"]')?.setAttribute('content', dark ? '#151719' : '#ffffff');
    document.querySelectorAll('[data-theme-toggle]').forEach(button => {
      const label = en ? (dark ? 'Switch to light mode' : 'Switch to dark mode') : (dark ? '라이트 모드로 전환' : '다크 모드로 전환');
      button.setAttribute('aria-pressed', String(dark));
      button.setAttribute('aria-label', label);
      button.title = label;
      button.querySelector('.theme-label').textContent = en ? (dark ? 'Light' : 'Dark') : (dark ? '라이트' : '다크');
    });
  };
  document.addEventListener('DOMContentLoaded', () => {
    updateTheme();
    document.querySelectorAll('[data-theme-toggle]').forEach(button => button.addEventListener('click', () => {
      const theme = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
      document.documentElement.dataset.theme = theme;
      try { localStorage.setItem('jiwoo-theme', theme); } catch { /* Keep the current-page setting. */ }
      updateTheme();
    }));
    document.querySelectorAll('[data-language-link]').forEach(link => {
      const updateLink = () => {
        const url = new URL(link.href);
        url.hash = location.hash;
        link.href = url.href;
      };
      updateLink();
      window.addEventListener('hashchange', updateLink);
      link.addEventListener('click', updateLink);
    });
  });
  window.addEventListener('storage', event => {
    if (event.key === 'jiwoo-theme') {
      document.documentElement.dataset.theme = event.newValue === 'dark' ? 'dark' : 'light';
      updateTheme();
    }
  });
})();
