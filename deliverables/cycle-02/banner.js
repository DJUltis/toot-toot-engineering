(function () {
  'use strict';

  function parseSTL(data, sample) {
    const lines = data.split('\n');
    const tris = [];
    let verts = [];
    let triIndex = 0;
    let minX = Infinity, minY = Infinity, minZ = Infinity;
    let maxX = -Infinity, maxY = -Infinity, maxZ = -Infinity;

    for (let i = 0; i < lines.length; i++) {
      const line = lines[i].trim();
      if (line.startsWith('vertex')) {
        const parts = line.split(/\s+/);
        const x = parseFloat(parts[1]);
        const y = parseFloat(parts[2]);
        const z = parseFloat(parts[3]);
        verts.push(x, y, z);
        if (verts.length === 9) {
          if (triIndex % sample === 0) {
            tris.push(verts.slice());
          }
          triIndex++;
          verts = [];
        }
        if (x < minX) minX = x;
        if (y < minY) minY = y;
        if (z < minZ) minZ = z;
        if (x > maxX) maxX = x;
        if (y > maxY) maxY = y;
        if (z > maxZ) maxZ = z;
      }
    }

    const cx = (minX + maxX) * 0.5;
    const cy = (minY + maxY) * 0.5;
    const cz = (minZ + maxZ) * 0.5;
    const size = Math.max(maxX - minX, maxY - minY, maxZ - minZ);

    return {
      tris: tris,
      center: [cx, cy, cz],
      size: size
    };
  }

  function shadeColor(base, brightness) {
    const r = Math.min(255, Math.floor(base[0] * brightness));
    const g = Math.min(255, Math.floor(base[1] * brightness));
    const b = Math.min(255, Math.floor(base[2] * brightness));
    return 'rgb(' + r + ',' + g + ',' + b + ')';
  }

  function createRenderer(canvas, config, model) {
    const ctx = canvas.getContext('2d');
    const baseColor = [210, 198, 170];
    const leafColor = [170, 198, 170];
    const lightDir = normalize([0.6, -0.2, 0.8]);

    function resize() {
      const dpr = window.devicePixelRatio || 1;
      const rect = canvas.getBoundingClientRect();
      canvas.width = Math.floor(rect.width * dpr);
      canvas.height = Math.floor(rect.height * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }

    function normalize(v) {
      const len = Math.hypot(v[0], v[1], v[2]) || 1;
      return [v[0] / len, v[1] / len, v[2] / len];
    }

    function render(timeMs) {
      const time = timeMs * 0.001;
      const rect = canvas.getBoundingClientRect();
      const w = rect.width;
      const h = rect.height;
      const cx = w * 0.5;
      const cy = h * 0.52;

      const angle = time * (Math.PI * 2 / config.turnSeconds);
      const tilt = config.tilt + Math.sin(time * 0.4) * 0.02;
      const scale = Math.min(w, h) * 0.7 / model.size;
      const camDist = config.camDist;

      // Background gradient
      const grad = ctx.createLinearGradient(0, 0, 0, h);
      grad.addColorStop(0, '#e7e1d4');
      grad.addColorStop(1, '#c9d7e8');
      ctx.fillStyle = grad;
      ctx.fillRect(0, 0, w, h);

      // Ground shadow
      ctx.fillStyle = 'rgba(0, 0, 0, 0.18)';
      ctx.beginPath();
      ctx.ellipse(cx, cy + h * 0.19, w * 0.2, h * 0.05, 0, 0, Math.PI * 2);
      ctx.fill();

      const sinY = Math.sin(angle);
      const cosY = Math.cos(angle);
      const sinX = Math.sin(tilt);
      const cosX = Math.cos(tilt);

      const drawList = [];
      const tris = model.tris;
      for (let i = 0; i < tris.length; i++) {
        const t = tris[i];
        const v = [];
        for (let j = 0; j < 9; j += 3) {
          let x = (t[j] - model.center[0]) * scale;
          let y = (t[j + 1] - model.center[1]) * scale;
          let z = (t[j + 2] - model.center[2]) * scale;

          // Rotate around Y
          let rx = x * cosY + z * sinY;
          let rz = -x * sinY + z * cosY;

          // Rotate around X
          let ry = y * cosX - rz * sinX;
          let rz2 = y * sinX + rz * cosX;

          // Perspective projection
          const p = camDist / (camDist + rz2 + config.zOffset);
          const sx = rx * p + cx;
          const sy = ry * p + cy;

          v.push(sx, sy, rz2);
        }

        const ax = v[3] - v[0];
        const ay = v[4] - v[1];
        const az = v[5] - v[2];
        const bx = v[6] - v[0];
        const by = v[7] - v[1];
        const bz = v[8] - v[2];

        const nx = ay * bz - az * by;
        const ny = az * bx - ax * bz;
        const nz = ax * by - ay * bx;
        const n = normalize([nx, ny, nz]);
        const brightness = Math.max(0.18, n[0] * lightDir[0] + n[1] * lightDir[1] + n[2] * lightDir[2]);
        const useLeaf = (t[2] > model.center[2] + model.size * 0.12);
        const color = useLeaf ? leafColor : baseColor;

        const zAvg = (v[2] + v[5] + v[8]) / 3;
        drawList.push({
          z: zAvg,
          v: v,
          shade: shadeColor(color, brightness)
        });
      }

      drawList.sort(function (a, b) { return a.z - b.z; });

      for (let i = 0; i < drawList.length; i++) {
        const tri = drawList[i];
        ctx.fillStyle = tri.shade;
        ctx.beginPath();
        ctx.moveTo(tri.v[0], tri.v[1]);
        ctx.lineTo(tri.v[3], tri.v[4]);
        ctx.lineTo(tri.v[6], tri.v[7]);
        ctx.closePath();
        ctx.fill();
      }

      // Vignette overlay
      const vignette = ctx.createRadialGradient(cx, cy, Math.min(w, h) * 0.2, cx, cy, Math.max(w, h));
      vignette.addColorStop(0, 'rgba(0,0,0,0)');
      vignette.addColorStop(1, 'rgba(0,0,0,0.18)');
      ctx.fillStyle = vignette;
      ctx.fillRect(0, 0, w, h);

      requestAnimationFrame(render);
    }

    window.addEventListener('resize', resize);
    resize();
    requestAnimationFrame(render);
  }

  const canvas = document.getElementById('banner');
  if (!canvas || typeof STL_DATA === 'undefined') {
    return;
  }

  const config = window.BANNER_CONFIG || {
    turnSeconds: 14,
    tilt: -0.35,
    camDist: 220,
    zOffset: 30,
    sample: 5
  };

  const model = parseSTL(STL_DATA, config.sample || 5);
  createRenderer(canvas, config, model);
})();
