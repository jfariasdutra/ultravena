// Live 3D view of the UltraVena CAD model. Loads the light model first and
// fetches the wired one (about 6 MB) only if the visitor asks for wiring.
(function () {
  var root = document.getElementById('viewer');
  var stage = document.getElementById('v-stage');
  var status = document.getElementById('v-status');
  if (!root || !stage) return;
  if (!window.THREE || !THREE.GLTFLoader || !THREE.OrbitControls) {
    status.textContent = 'The 3D view could not load. The renders below show the same model.';
    return;
  }
  var base = root.getAttribute('data-base');
  var wiresBox = document.getElementById('v-wires');
  var wallsBox = document.getElementById('v-walls');
  var variant = 'butterfly';
  var renderer;
  try {
    renderer = new THREE.WebGLRenderer({ antialias: true });
  } catch (e) {
    status.textContent = 'This browser cannot show 3D here. The renders below show the same model.';
    return;
  }
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
  renderer.outputEncoding = THREE.sRGBEncoding;
  stage.appendChild(renderer.domElement);

  var scene = new THREE.Scene();
  scene.background = new THREE.Color(0xeef0f2);
  scene.add(new THREE.HemisphereLight(0xffffff, 0x8a8a8a, 1.05));
  [[-300, 900, 500, 0.55], [400, 600, -900, 0.45], [600, 300, 700, 0.3]].forEach(function (q) {
    var d = new THREE.DirectionalLight(0xffffff, q[3]);
    d.position.set(q[0], q[1], q[2]);
    scene.add(d);
  });
  var camera = new THREE.PerspectiveCamera(35, 1, 10, 9000);
  camera.position.set(-950, 760, 1250);
  var controls = new THREE.OrbitControls(camera, renderer.domElement);
  controls.target.set(0, 280, 0);
  controls.enableDamping = true;
  controls.dampingFactor = 0.08;
  controls.minDistance = 250;
  controls.maxDistance = 3200;
  controls.update();

  var dirty = true;
  controls.addEventListener('change', function () { dirty = true; });
  function size() {
    var w = stage.clientWidth, h = stage.clientHeight;
    if (!w || !h) return;
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
    dirty = true;
  }
  window.addEventListener('resize', size);
  size();
  (function loop() {
    requestAnimationFrame(loop);
    controls.update();
    if (dirty) { renderer.render(scene, camera); dirty = false; }
  })();

  var loader = new THREE.GLTFLoader();
  var cache = {};
  var current = null;
  var ticket = 0;

  function prepare(gltf) {
    var walls = [];
    gltf.scene.traverse(function (o) {
      if (!o.isMesh) return;
      var n = '', q = o;
      while (q) { n += '/' + q.name; q = q.parent; }
      o.material = o.material.clone();
      o.material.side = THREE.DoubleSide;
      o.material.metalness = 0.1;
      o.material.roughness = 0.7;
      if (/wall_|front_panel_slanted/.test(n)) {
        o.material.transparent = true;
        o.material.opacity = 0.22;
        o.material.depthWrite = false;
        walls.push(o);
      }
    });
    gltf.scene.userData.walls = walls;
    return gltf.scene;
  }

  function applyWalls() {
    if (!current) return;
    current.userData.walls.forEach(function (o) { o.visible = wallsBox.checked; });
    dirty = true;
  }

  function show() {
    var key = variant + (wiresBox.checked ? '_wired' : '');
    var mine = ++ticket;
    function place(obj) {
      if (mine !== ticket) return;
      if (current) scene.remove(current);
      current = obj;
      scene.add(obj);
      applyWalls();
      status.textContent = 'CAD version 6';
      dirty = true;
    }
    if (cache[key]) { place(cache[key]); return; }
    status.textContent = wiresBox.checked ? 'Loading the wired model, about 6 MB' : 'Loading model';
    loader.load(base + key + '.glb', function (g) {
      cache[key] = prepare(g);
      place(cache[key]);
    }, function (e) {
      if (mine === ticket && e.total) status.textContent = 'Loading, ' + Math.round(100 * e.loaded / e.total) + '%';
    }, function () {
      if (mine === ticket) status.textContent = 'The model could not load. The renders below show it.';
    });
  }

  Array.prototype.forEach.call(root.querySelectorAll('[data-variant]'), function (b) {
    b.addEventListener('click', function () {
      variant = b.getAttribute('data-variant');
      Array.prototype.forEach.call(root.querySelectorAll('[data-variant]'), function (x) { x.classList.toggle('on', x === b); });
      show();
    });
  });
  wiresBox.addEventListener('change', show);
  wallsBox.addEventListener('change', applyWalls);
  show();
})();
