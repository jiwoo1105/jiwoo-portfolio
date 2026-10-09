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
  const motionButtons = document.querySelectorAll('[data-motion-toggle]');
  if (motionButtons.length) body.classList.add('motion-enabled');
  let paused = false;
  let framePending = false;
  function updateParallax() {
    framePending = false;
    if (!photo || !hero) return;
    if (reducedMotion.matches || paused) { photo.style.transform = ''; return; }
    const scroll = Math.min(Math.max(0, -hero.getBoundingClientRect().top), hero.offsetHeight);
    photo.style.transform = `translate3d(0, ${scroll * 0.035}px, 0)`;
  }
  if (hero) window.addEventListener('scroll', () => { if (!framePending) { requestAnimationFrame(updateParallax); framePending = true; } }, { passive: true });
  motionButtons.forEach(button => button.addEventListener('click', () => {
    paused = !paused;
    body.classList.toggle('motion-paused', paused);
    motionButtons.forEach(control => {
      control.setAttribute('aria-pressed', String(paused));
      control.querySelector('.motion-label').textContent = paused ? '애니메이션 재생' : '애니메이션 멈추기';
      control.querySelector('.motion-symbol').textContent = paused ? '▷' : 'Ⅱ';
    });
    updateParallax();
    syncPreviews();
  }));
  const previews = [];
  const shouldPlay = state => state.visible && !document.hidden && !paused && !state.userPaused && (!reducedMotion.matches || state.manualPlay);
  function syncPreview(state) {
    if (shouldPlay(state)) {
      if (!state.video.paused || state.starting) return;
      state.starting = true;
      state.video.play().then(() => {
        if (!shouldPlay(state)) state.video.pause();
      }).catch(error => {
        if (error.name !== 'AbortError' && shouldPlay(state)) state.userPaused = true;
      }).finally(() => {
        state.starting = false;
        if (shouldPlay(state) && state.video.paused) syncPreview(state);
      });
    } else state.video.pause();
  }
  function syncPreviews() { previews.forEach(syncPreview); }
  if ('IntersectionObserver' in window) {
    const previewObserver = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        const state = previews.find(item => item.video === entry.target);
        if (state) { state.visible = entry.isIntersecting && entry.intersectionRatio >= 0.4; syncPreview(state); }
      });
    }, { threshold: [0, 0.4] });
    document.querySelectorAll('[data-preview]').forEach(video => {
      const media = video.closest('.preview-media');
      const button = media.querySelector('[data-preview-toggle]');
      if (!button) return;
      const state = { video, visible: false, userPaused: false, manualPlay: false, starting: false };
      previews.push(state);
      video.muted = true;
      video.controls = false;
      media.classList.add('preview-enhanced');
      const updateLabel = () => {
        button.querySelector('.preview-button-label').textContent = video.paused ? '재생' : '멈춤';
        button.querySelector('[aria-hidden]').textContent = video.paused ? '▶' : 'Ⅱ';
        button.setAttribute('aria-label', `${video.getAttribute('aria-label')} ${video.paused ? '재생' : '멈춤'}`);
      };
      video.addEventListener('play', updateLabel);
      video.addEventListener('pause', updateLabel);
      button.addEventListener('click', () => {
        if (video.paused) {
          state.userPaused = false;
          state.manualPlay = true;
          // An explicit preview play is allowed while decorative motion is paused.
          video.play().catch(error => {
            if (error.name === 'AbortError') return;
            video.controls = true;
            media.classList.remove('preview-enhanced');
          });
        } else { state.userPaused = true; state.manualPlay = false; video.pause(); }
      });
      previewObserver.observe(video);
    });
  }
  document.addEventListener('visibilitychange', syncPreviews);
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
    previews.forEach(state => { state.manualPlay = false; });
    syncPreviews();
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
