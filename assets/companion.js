import * as THREE from './vendor/three.module.js';

// Original procedural scene. No downloaded character meshes or textures.
export function mountCompanion(host) {
  const canvas = host.querySelector('canvas');
  const greet = host.querySelector('[data-companion-greet]');
  const status = host.querySelector('[data-companion-status]');
  const en = document.documentElement.lang === 'en';
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  const pointerFine = matchMedia('(hover: hover) and (pointer: fine)');
  const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true, powerPreference: 'low-power' });
  renderer.setPixelRatio(Math.min(devicePixelRatio, 1.75));
  renderer.setClearColor(0x000000, 0);
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFShadowMap;
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.25;
  const scene = new THREE.Scene();
  const camera = new THREE.OrthographicCamera(-3, 3, 2.65, -2.65, .1, 50);
  camera.position.set(5.5, 4.2, 7.5);
  camera.lookAt(0, 1.25, 0);
  const room = new THREE.Group();
  scene.add(room);
  scene.add(new THREE.HemisphereLight(0xffffff, 0xc1c9db, 2.5));
  const sun = new THREE.DirectionalLight(0xfff4e5, 4.2);
  sun.position.set(-3, 7, 5);
  sun.castShadow = true;
  sun.shadow.mapSize.set(1024, 1024);
  Object.assign(sun.shadow.camera, { left: -4, right: 4, top: 4, bottom: -4, near: .5, far: 20 });
  sun.shadow.normalBias = .035;
  sun.shadow.bias = -.0003;
  scene.add(sun);
  const fill = new THREE.DirectionalLight(0xc9ddff, 1.4);
  fill.position.set(4, 3, -3);
  scene.add(fill);
  const material = color => new THREE.MeshStandardMaterial({ color, roughness: .78 });
  const fur = material(0xc99458), cream = material(0xfff5df), pink = material(0xdcab97);
  const ink = material(0x292c37), blue = material(0x4e6ce5), wood = material(0xcdaf8b);
  const white = material(0xf2f2ed), silver = material(0xabb4c3), leaf = material(0x74917a);
  const geometryCache = new Map();
  function roundBox(w, h, d, r = .07) {
    const key = [w, h, d, r].join(',');
    if (geometryCache.has(key)) return geometryCache.get(key);
    const g = new THREE.BoxGeometry(w, h, d, 5, 5, 5);
    const pos = g.attributes.position;
    const core = new THREE.Vector3(w / 2 - r, h / 2 - r, d / 2 - r);
    const p = new THREE.Vector3(), inner = new THREE.Vector3();
    for (let i = 0; i < pos.count; i++) {
      p.fromBufferAttribute(pos, i);
      inner.set(Math.max(-core.x, Math.min(core.x, p.x)), Math.max(-core.y, Math.min(core.y, p.y)), Math.max(-core.z, Math.min(core.z, p.z)));
      p.sub(inner).normalize().multiplyScalar(r).add(inner);
      pos.setXYZ(i, p.x, p.y, p.z);
    }
    g.computeVertexNormals();
    geometryCache.set(key, g);
    return g;
  }
  function mesh(geometry, mat, parent, x, y, z) {
    const m = new THREE.Mesh(geometry, mat);
    m.position.set(x, y, z);
    m.castShadow = true;
    m.receiveShadow = true;
    parent.add(m);
    return m;
  }
  const box = (parent, w, h, d, mat, x, y, z, r = .06) => mesh(roundBox(w, h, d, Math.min(r, w / 3, h / 3, d / 3)), mat, parent, x, y, z);
  const sphereGeo = new THREE.SphereGeometry(1, 24, 16);
  function ball(parent, mat, x, y, z, sx, sy = sx, sz = sx) {
    const m = mesh(sphereGeo, mat, parent, x, y, z);
    m.scale.set(sx, sy, sz);
    return m;
  }
  // A quiet floor and a small wooden desk.
  const floorMat = material(0xf3f5f7);
  const floor = mesh(new THREE.CylinderGeometry(2.55, 2.55, .1, 64), floorMat, room, 0, -.04, 0);
  floor.receiveShadow = true;
  box(room, 3.55, .15, 1.65, wood, 0, 1.2, .15);
  for (const x of [-1.5, 1.5]) for (const z of [-.45, .7]) box(room, .11, 1.2, .11, wood, x, .59, z, .025);
  box(room, .92, .13, .85, blue, -.65, .59, -.95);
  for (const x of [-.98, -.32]) for (const z of [-1.2, -.68]) box(room, .085, .6, .085, silver, x, .28, z, .02);
  // Shiba-like companion, with a cream muzzle, upright ears and curled tail.
  const dog = new THREE.Group();
  dog.position.set(-.65, 0, -.64);
  room.add(dog);
  box(dog, .74, .85, .64, fur, 0, 1.13, 0, .2);
  ball(dog, cream, 0, 1.15, .29, .29, .35, .1);
  for (const x of [-.26, .26]) {
    box(dog, .27, .56, .29, fur, x, .55, .12, .1);
    box(dog, .28, .17, .38, cream, x, .29, .24, .075);
  }
  // Blue bandana ties this character to the portfolio's accent color.
  mesh(new THREE.CylinderGeometry(.37, .38, .11, 32), blue, dog, 0, 1.56, 0);
  const bandana = mesh(new THREE.ConeGeometry(.21, .3, 3), blue, dog, .06, 1.41, .35);
  bandana.rotation.z = Math.PI;
  const head = new THREE.Group();
  head.position.set(0, 1.98, .015);
  dog.add(head);
  box(head, .96, .84, .83, fur, 0, 0, 0, .24);
  for (const x of [-.32, .32]) {
    const ear = mesh(new THREE.ConeGeometry(.225, .5, 4), fur, head, x, .55, -.05);
    ear.rotation.y = Math.PI / 4;
    ear.rotation.z = -Math.sign(x) * .14;
    const inside = mesh(new THREE.ConeGeometry(.125, .29, 3), pink, head, x, .56, .074);
    inside.rotation.x = -.16;
    ball(head, cream, x * .9, -.2, .35, .25, .2, .13);
  }
  box(head, .56, .33, .25, cream, 0, -.2, .43, .12);
  const nose = ball(head, ink, 0, -.12, .59, .115, .077, .065);
  const eyes = [-.235, .235].map(x => {
    const eye = ball(head, ink, x, .045, .413, .045, .062, .035);
    ball(head, white, x - .009, .063, .44, .012);
    ball(head, cream, x, .19, .37, .075, .034, .025);
    return eye;
  });
  box(head, .026, .1, .02, ink, 0, -.225, .56, .006);
  for (const x of [-.04, .04]) {
    const smile = box(head, .09, .023, .025, ink, x, -.274, .55, .008);
    smile.rotation.z = Math.sign(x) * .24;
  }
  const arms = [-.38, .38].map(x => {
    const joint = new THREE.Group();
    joint.position.set(x, 1.45, .1);
    dog.add(joint);
    joint.rotation.x = -.95;
    box(joint, .22, .44, .24, fur, 0, -.18, 0, .095);
    ball(joint, cream, 0, -.39, .035, .13, .12, .14);
    return joint;
  });
  const tail = new THREE.Group();
  tail.position.set(-.46, 1.32, -.25);
  dog.add(tail);
  const curl = mesh(new THREE.TorusGeometry(.29, .12, 12, 24, Math.PI * 1.7), fur, tail, -.19, .15, 0);
  curl.rotation.y = .2;
  ball(tail, cream, -.37, -.07, 0, .125);
  // Laptop and a separate little keyboard. Screen bars are abstract code.
  const laptop = new THREE.Group();
  laptop.position.set(.62, 1.31, .05);
  laptop.rotation.y = -.34;
  room.add(laptop);
  box(laptop, 1.18, .055, .75, silver, 0, 0, 0, .025);
  const lid = new THREE.Group();
  lid.position.set(0, .04, -.32);
  lid.rotation.x = -.12;
  laptop.add(lid);
  box(lid, 1.18, .82, .07, silver, 0, .38, 0, .045);
  box(lid, 1.07, .68, .012, ink, 0, .4, .041, .02);
  const codeMat = new THREE.MeshBasicMaterial({ color: 0x91c2e6 });
  const purpleMat = new THREE.MeshBasicMaterial({ color: 0xb9a5e7 });
  const screenBars = [];
  for (let i = 0; i < 6; i++) {
    screenBars.push(box(lid, [.53, .34, .61, .4, .51, .27][i], .021, .008, i % 3 ? codeMat : purpleMat, -.12 + (i % 2) * .06, .65 - i * .078, .052, .003));
  }
  const cursor = box(lid, .035, .048, .008, cream, -.29, .18, .053, .003);
  box(room, .83, .045, .34, white, -.63, 1.306, -.13, .023);
  for (let row = 0; row < 3; row++) for (let col = 0; col < 9; col++) box(room, .055, .012, .055, col === 8 ? blue : silver, -.95 + col * .078, 1.333, -.22 + row * .075, .008);
  // A mug and a plant give the scene a lived-in scale.
  mesh(new THREE.CylinderGeometry(.12, .095, .23, 24), blue, room, -1.4, 1.39, .22);
  const coffee = mesh(new THREE.CircleGeometry(.104, 24), material(0x5a4233), room, -1.4, 1.51, .22);
  coffee.rotation.x = -Math.PI / 2;
  const handle = mesh(new THREE.TorusGeometry(.075, .025, 8, 16), blue, room, -1.53, 1.4, .22);
  handle.rotation.y = .3;
  mesh(new THREE.CylinderGeometry(.16, .11, .23, 16), white, room, 1.45, 1.4, -.37);
  for (let i = 0; i < 5; i++) {
    const angle = i * 2.4;
    const stem = box(room, .018, .36, .018, leaf, 1.45 + Math.sin(angle) * .06, 1.65, -.37 + Math.cos(angle) * .06, .005);
    stem.rotation.z = Math.sin(angle) * .3;
    const l = ball(room, leaf, 1.45 + Math.sin(angle) * .13, 1.8 + i % 2 * .08, -.37 + Math.cos(angle) * .13, .1, .18, .045);
    l.rotation.z = Math.sin(angle) * .65;
    l.rotation.y = angle;
  }
  let visible = false, frame = 0, last = 0, elapsed = 0, waveUntil = 0, targetX = 0, targetY = 0;
  const stopped = () => reduced.matches || document.body.classList.contains('motion-paused');
  const allowed = () => visible && !document.hidden && !stopped();
  function render() { renderer.render(scene, camera); }
  function update(t) {
    const wave = t < waveUntil;
    room.rotation.y += (targetX * .12 - room.rotation.y) * .065;
    head.rotation.y += ((wave ? .34 : .07 + targetX * .16) - head.rotation.y) * .075;
    head.rotation.x = (wave ? -.12 : .025 + Math.sin(t * 1.7) * .018) + targetY * .035;
    head.rotation.z = Math.sin(t * .7) * .025;
    arms[0].rotation.x = -.95 + Math.sin(t * 11) * .09;
    arms[1].position.y = wave ? 1.82 : 1.45;
    arms[1].rotation.x = wave ? -2.7 : -.95 + Math.sin(t * 11 + Math.PI) * .09;
    arms[1].rotation.z = wave ? -.55 + Math.sin(t * 10) * .26 : 0;
    tail.rotation.y = Math.sin(t * (wave ? 9 : 3.6)) * (wave ? .4 : .17);
    tail.rotation.z = Math.sin(t * 2) * .07;
    const blink = t % 5.4 > 5.15 && t % 5.4 < 5.3;
    eyes.forEach(eye => { eye.scale.y = blink ? .008 : .062; });
    cursor.visible = Math.floor(t * 2) % 2 === 0;
    screenBars[5].scale.x = .65 + Math.sin(t * .6) * .25;
    if (!wave && host.dataset.greeting === 'true') {
      delete host.dataset.greeting;
      status.textContent = '';
    }
  }
  function tick(now) {
    frame = 0;
    if (!allowed()) { last = 0; return; }
    if (last) elapsed += Math.min((now - last) / 1000, .06);
    last = now;
    update(elapsed);
    render();
    frame = requestAnimationFrame(tick);
  }
  function sync() {
    if (allowed()) { if (!frame) frame = requestAnimationFrame(tick); }
    else { cancelAnimationFrame(frame); frame = 0; last = 0; }
    host.dataset.motion = allowed() ? 'running' : 'paused';
  }
  function resize() {
    const width = host.clientWidth, height = canvas.clientHeight;
    if (!width || !height) return;
    renderer.setSize(width, height, false);
    const aspect = width / height;
    const halfHeight = aspect < 1.1 ? 2.75 : 2.4;
    camera.left = -halfHeight * aspect;
    camera.right = halfHeight * aspect;
    camera.top = halfHeight;
    camera.bottom = -halfHeight;
    camera.updateProjectionMatrix();
    render();
  }
  function theme() {
    const dark = document.documentElement.dataset.theme === 'dark';
    floorMat.color.setHex(dark ? 0x282d36 : 0xf1f3f6);
    render();
  }
  host.addEventListener('pointermove', event => {
    if (!pointerFine.matches || stopped()) return;
    const r = host.getBoundingClientRect();
    targetX = (event.clientX - r.left) / r.width * 2 - 1;
    targetY = (event.clientY - r.top) / r.height * 2 - 1;
  });
  host.addEventListener('pointerleave', () => { targetX = 0; targetY = 0; });
  let greetingTimer;
  greet.addEventListener('click', () => {
    clearTimeout(greetingTimer);
    host.dataset.greeting = 'true';
    status.textContent = en ? 'Hey, nice to meet you!' : '안녕, 반가워요!';
    if (!stopped()) waveUntil = elapsed + 2.5;
    else greetingTimer = setTimeout(() => { status.textContent = ''; delete host.dataset.greeting; }, 2500);
    sync();
  });
  new IntersectionObserver(entries => { visible = entries[0].isIntersecting; sync(); }, { threshold: .05 }).observe(host);
  new ResizeObserver(resize).observe(host);
  new MutationObserver(theme).observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme'] });
  new MutationObserver(sync).observe(document.body, { attributes: true, attributeFilter: ['class'] });
  document.addEventListener('visibilitychange', sync);
  reduced.addEventListener('change', sync);
  canvas.addEventListener('webglcontextlost', event => {
    event.preventDefault();
    visible = false;
    sync();
    host.classList.remove('companion-ready');
    greet.hidden = true;
  });
  canvas.addEventListener('webglcontextrestored', () => {
    host.classList.add('companion-ready');
    greet.hidden = false;
    const r = host.getBoundingClientRect();
    visible = r.bottom > 0 && r.top < innerHeight;
    resize();
    sync();
  });
  update(0);
  theme();
  resize();
  host.classList.add('companion-ready');
  greet.hidden = false;
}
