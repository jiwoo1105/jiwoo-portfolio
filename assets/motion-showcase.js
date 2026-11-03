/* Every stage maps to the same 360 source frames. No synthetic motion. */
(() => {
  const root = document.querySelector('[data-motion-showcase]');
  if (!root) return;
  const player = root.querySelector('video');
  const buttons = [...root.querySelectorAll('[data-stage]')];
  const title = root.querySelector('#motion-stage-title');
  const description = root.querySelector('#motion-stage-description');
  const speed = root.querySelector('[data-playback-speed]');
  const error = root.querySelector('.motion-error');
  const en = document.documentElement.lang === 'en';
  let current = buttons[0];
  let pending = null;
  let revision = 0;

  root.querySelector('.motion-stages').hidden = false;
  root.querySelector('.motion-speed').hidden = false;

  function selectStage(button) {
    if (button === current) return;
    const wasPlaying = pending ? pending.playing : !player.paused;
    const time = pending ? pending.time : player.currentTime;
    const rate = pending ? pending.rate : player.playbackRate;
    pending = { time, rate, playing: wasPlaying, revision: ++revision };
    player.pause();
    current = button;
    buttons.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
    title.textContent = button.dataset.title;
    description.textContent = button.dataset.description;
    error.hidden = true;
    player.poster = button.dataset.poster;
    player.src = button.dataset.src;
    player.load();
  }

  player.addEventListener('loadedmetadata', () => {
    const state = pending;
    pending = null;
    player.playbackRate = state ? state.rate : Number(speed.value);
    if (!state) return;
    player.currentTime = Math.min(state.time, Math.max(0, player.duration - 0.05));
    if (state.playing && !document.hidden) {
      player.play().then(() => {
        if (state.revision !== revision || document.hidden) player.pause();
      }).catch(() => {}); // Native controls remain available if autoplay is blocked.
    }
  });

  buttons.forEach((button, index) => {
    button.addEventListener('click', () => selectStage(button));
    button.addEventListener('keydown', event => {
      const next = { ArrowRight: (index + 1) % buttons.length,
        ArrowLeft: (index + buttons.length - 1) % buttons.length,
        Home: 0, End: buttons.length - 1 }[event.key];
      if (next === undefined) return;
      event.preventDefault();
      buttons[next].focus();
      selectStage(buttons[next]);
    });
  });
  speed.addEventListener('change', () => {
    const rate = Number(speed.value);
    if (pending) pending.rate = rate;
    player.playbackRate = rate;
  });
  player.addEventListener('ratechange', () => {
    if (pending) return;
    const rate = String(player.playbackRate);
    if (![...speed.options].some(option => option.value === rate)) {
      speed.querySelector('[data-native-rate]')?.remove();
      const option = document.createElement('option');
      option.value = rate;
      option.textContent = `${rate}×`;
      option.dataset.nativeRate = '';
      speed.append(option);
    }
    speed.value = rate;
  });
  player.addEventListener('error', () => {
    pending = null;
    error.replaceChildren(document.createTextNode(en
      ? 'This video could not load. Try another stage or '
      : '영상을 불러오지 못했어요. 다른 단계를 선택하거나 '));
    const link = document.createElement('a');
    link.href = current.dataset.src;
    link.textContent = en ? 'open the video file.' : '영상 파일을 직접 열어보세요.';
    error.append(link);
    error.hidden = false;
  });
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
      player.pause();
      if (pending) pending.playing = false;
    }
  });
})();
