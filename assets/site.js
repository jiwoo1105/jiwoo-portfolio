(() => {
  'use strict';
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const finePointer = window.matchMedia('(hover: hover) and (pointer: fine)');
  const body = document.body;
  const dialog = document.getElementById('menu-dialog');
  const menuTrigger = document.querySelector('.menu-trigger');
  if (dialog && menuTrigger && typeof dialog.showModal === 'function') {
    body.classList.add('menu-enhanced');
    menuTrigger.addEventListener('click', () => dialog.showModal());
    dialog.querySelector('.menu-close').addEventListener('click', () => dialog.close());
    dialog.querySelectorAll('a').forEach(link => link.addEventListener('click', () => dialog.close()));
    dialog.addEventListener('click', event => { if (event.target === dialog && event.clientX < dialog.getBoundingClientRect().left) dialog.close(); });
  }
  let observer;
  if ('IntersectionObserver' in window && !reducedMotion.matches) {
    body.classList.add('js-ready');
    observer = new IntersectionObserver(entries => entries.forEach(entry => {
      if (entry.isIntersecting) { entry.target.classList.remove('is-pending'); entry.target.classList.add('is-visible'); observer.unobserve(entry.target); }
    }), { threshold: 0.06 });
    document.querySelectorAll('.reveal').forEach(el => { el.classList.add('is-pending'); observer.observe(el); });
  }
  const hero = document.querySelector('.hero');
  const photo = document.querySelector('.hero-photo');
  const motionButton = document.querySelector('.motion-toggle');
  if (motionButton) body.classList.add('motion-enabled');
  let paused = false;
  let framePending = false;
  function updateParallax() {
    framePending = false;
    if (!photo || !hero) return;
    if (reducedMotion.matches || paused) { photo.style.transform = ''; return; }
    const scroll = Math.min(Math.max(0, -hero.getBoundingClientRect().top), hero.offsetHeight);
    photo.style.transform = `translate3d(0, ${scroll * 0.12}px, 0)`;
  }
  if (hero) window.addEventListener('scroll', () => { if (!framePending) { requestAnimationFrame(updateParallax); framePending = true; } }, { passive: true });
  if (motionButton) motionButton.addEventListener('click', () => {
    paused = !paused;
    body.classList.toggle('motion-paused', paused);
    motionButton.setAttribute('aria-pressed', String(paused));
    motionButton.querySelector('.motion-label').textContent = paused ? '움직임 재생' : '움직임 멈추기';
    motionButton.querySelector('.motion-symbol').textContent = paused ? '▷' : 'Ⅱ';
    updateParallax();
  });
  const chapterButtons = document.querySelectorAll('[data-video][data-seek]');
  if (chapterButtons.length) body.classList.add('video-enhanced');
  chapterButtons.forEach(button => button.addEventListener('click', () => {
    const video = document.getElementById(button.dataset.video);
    if (!video) return;
    video.currentTime = Number(button.dataset.seek);
    video.play().catch(() => video.focus());
  }));
  const cursor = document.querySelector('.project-cursor');
  document.querySelectorAll('[data-project-link]').forEach(card => {
    card.addEventListener('pointermove', event => {
      if (!cursor || !finePointer.matches || reducedMotion.matches || paused) return;
      cursor.style.transform = `translate3d(${event.clientX - 42}px, ${event.clientY - 42}px, 0)`;
      cursor.classList.add('is-active');
    });
    card.addEventListener('pointerleave', () => cursor?.classList.remove('is-active'));
  });
  document.querySelectorAll('.magnetic').forEach(button => {
    button.addEventListener('pointermove', event => {
      if (!finePointer.matches || reducedMotion.matches || paused) return;
      const r = button.getBoundingClientRect();
      button.style.setProperty('--mx', `${(event.clientX - r.left - r.width / 2) * 0.18}px`);
      button.style.setProperty('--my', `${(event.clientY - r.top - r.height / 2) * 0.18}px`);
    });
    button.addEventListener('pointerleave', () => { button.style.removeProperty('--mx'); button.style.removeProperty('--my'); });
  });
  reducedMotion.addEventListener('change', () => {
    updateParallax();
    cursor?.classList.remove('is-active');
    if (reducedMotion.matches) {
      observer?.disconnect();
      document.querySelectorAll('.is-pending').forEach(el => el.classList.remove('is-pending'));
    }
  });
  document.querySelectorAll('[data-copy-email]').forEach(button => {
    let resetTimer;
    button.addEventListener('click', async () => {
      const status = button.parentElement.querySelector('.copy-status');
      try {
        if (!navigator.clipboard?.writeText) throw new Error('Clipboard unavailable');
        await navigator.clipboard.writeText(button.dataset.copyEmail);
        button.textContent = '복사했어요';
        if (status) status.textContent = '이메일 주소를 복사했습니다.';
      } catch {
        button.textContent = '주소를 직접 선택해 주세요';
        if (status) status.textContent = '복사할 수 없습니다. 옆의 이메일 주소를 직접 선택해 주세요.';
      }
      clearTimeout(resetTimer);
      resetTimer = setTimeout(() => { button.textContent = '이메일 복사'; }, 2500);
    });
  });
})();
