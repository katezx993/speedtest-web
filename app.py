<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title> SpeedTest Pro</title>
<link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #0a0f0a;
    --card: #0f1a0f;
    --neon: #00ff88;
    --neon2: #00ccff;
    --neon3: #ff4466;
    --gray: #2a3a2a;
    --text: #e0ffe0;
    --sub: #5a8a5a;
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'Share Tech Mono', monospace;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    overflow-x: hidden;
  }

  /* Grid background */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
      linear-gradient(rgba(0,255,136,0.03) 1px, transparent 1px),
      linear-gradient(90deg, rgba(0,255,136,0.03) 1px, transparent 1px);
    background-size: 40px 40px;
    pointer-events: none;
    z-index: 0;
  }

  .container {
    width: 100%;
    max-width: 480px;
    position: relative;
    z-index: 1;
  }

  /* Header */
  header {
    text-align: center;
    padding: 30px 0 10px;
  }

  .title {
    font-family: 'Orbitron', sans-serif;
    font-size: 2rem;
    font-weight: 900;
    letter-spacing: 4px;
  }

  .title span:first-child { color: var(--neon); }
  .title span:last-child { color: var(--neon2); }

  .subtitle {
    color: var(--sub);
    font-size: 0.8rem;
    margin-top: 6px;
    letter-spacing: 2px;
  }

  /* ISP Info */
  .isp-bar {
    text-align: center;
    font-size: 0.78rem;
    color: var(--neon2);
    margin: 10px 0;
    min-height: 18px;
    letter-spacing: 1px;
  }

  /* Gauge */
  .gauge-wrap {
    display: flex;
    justify-content: center;
    margin: 10px 0;
  }

  canvas#gauge {
    filter: drop-shadow(0 0 12px rgba(0,255,136,0.3));
  }

  /* Speed display */
  .speed-display {
    text-align: center;
    margin: -10px 0 4px;
  }

  .speed-num {
    font-family: 'Orbitron', sans-serif;
    font-size: 3.5rem;
    font-weight: 900;
    color: var(--neon);
    text-shadow: 0 0 20px rgba(0,255,136,0.5);
    line-height: 1;
  }

  .speed-unit {
    color: var(--sub);
    font-size: 0.9rem;
    letter-spacing: 2px;
    margin-top: 4px;
  }

  .phase-text {
    color: var(--sub);
    font-size: 0.82rem;
    text-align: center;
    margin: 6px 0;
    min-height: 20px;
    letter-spacing: 1px;
  }

  /* Graph */
  .graph-wrap {
    background: var(--card);
    border: 1px solid var(--gray);
    border-radius: 6px;
    padding: 8px;
    margin: 10px 0;
  }

  canvas#graph {
    width: 100%;
    height: 60px;
    display: block;
  }

  /* Stat cards */
  .stats {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 8px;
    margin: 10px 0;
  }

  .stat-card {
    background: var(--card);
    border-radius: 8px;
    padding: 12px 8px;
    text-align: center;
    position: relative;
    overflow: hidden;
  }

  .stat-card::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 2px;
  }

  .stat-card.dl::after { background: var(--neon); }
  .stat-card.ul::after { background: var(--neon2); }
  .stat-card.ping::after { background: var(--neon3); }

  .stat-label {
    font-size: 0.65rem;
    letter-spacing: 1px;
    margin-bottom: 4px;
  }

  .stat-card.dl .stat-label { color: var(--neon); }
  .stat-card.ul .stat-label { color: var(--neon2); }
  .stat-card.ping .stat-label { color: var(--neon3); }

  .stat-val {
    font-family: 'Orbitron', sans-serif;
    font-size: 1.3rem;
    font-weight: 700;
    color: var(--text);
  }

  .stat-unit {
    font-size: 0.6rem;
    color: var(--sub);
    margin-top: 2px;
  }

  /* Server */
  .server-text {
    text-align: center;
    font-size: 0.75rem;
    color: var(--sub);
    min-height: 16px;
    margin: 4px 0 10px;
  }

  /* Button */
  .btn-wrap { text-align: center; margin: 10px 0; }

  #startBtn {
    font-family: 'Orbitron', sans-serif;
    font-size: 1rem;
    font-weight: 700;
    letter-spacing: 3px;
    padding: 14px 40px;
    background: var(--neon);
    color: var(--bg);
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.2s;
    text-transform: uppercase;
  }

  #startBtn:hover:not(:disabled) {
    background: #00ffaa;
    box-shadow: 0 0 24px rgba(0,255,136,0.6);
    transform: translateY(-1px);
  }

  #startBtn:disabled {
    background: var(--gray);
    color: var(--sub);
    cursor: not-allowed;
  }

  /* History */
  .history-section {
    margin-top: 16px;
    border-top: 1px solid var(--gray);
    padding-top: 12px;
  }

  .history-title {
    font-size: 0.75rem;
    color: var(--sub);
    letter-spacing: 2px;
    margin-bottom: 8px;
  }

  .history-row {
    display: flex;
    justify-content: space-between;
    font-size: 0.72rem;
    padding: 6px 0;
    border-bottom: 1px solid var(--gray);
    color: var(--text);
  }

  .history-row span { color: var(--sub); }

  /* Export btn */
  .export-btn {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.8rem;
    padding: 6px 16px;
    background: transparent;
    color: var(--neon3);
    border: 1px solid var(--neon3);
    border-radius: 4px;
    cursor: pointer;
    margin-top: 10px;
    transition: all 0.2s;
  }

  .export-btn:hover { background: rgba(255,68,102,0.1); }

  @media (max-width: 400px) {
    .speed-num { font-size: 2.8rem; }
    .title { font-size: 1.5rem; }
  }
</style>
</head>
<body>
<div class="container">
  <header>
    <div class="title"><span>⚡ SPEED</span><span>TEST PRO</span></div>
    <div class="subtitle">วัดความเร็วอินเทอร์เน็ต</div>
  </header>

  <div class="isp-bar" id="ispBar"></div>

  <div class="gauge-wrap">
    <canvas id="gauge" width="300" height="180"></canvas>
  </div>

  <div class="speed-display">
    <div class="speed-num" id="speedNum">0.00</div>
    <div class="speed-unit">Mbps</div>
  </div>

  <div class="phase-text" id="phaseText">พร้อมใช้งาน</div>

  <div class="graph-wrap">
    <canvas id="graph" width="440" height="60"></canvas>
  </div>

  <div class="stats">
    <div class="stat-card dl">
      <div class="stat-label">⬇ DOWNLOAD</div>
      <div class="stat-val" id="dlVal">—</div>
      <div class="stat-unit">Mbps</div>
    </div>
    <div class="stat-card ul">
      <div class="stat-label">⬆ UPLOAD</div>
      <div class="stat-val" id="ulVal">—</div>
      <div class="stat-unit">Mbps</div>
    </div>
    <div class="stat-card ping">
      <div class="stat-label">📡 PING</div>
      <div class="stat-val" id="pingVal">—</div>
      <div class="stat-unit">ms</div>
    </div>
  </div>

  <div class="server-text" id="serverText"></div>

  <div class="btn-wrap">
    <button id="startBtn" onclick="startTest()">▶ เริ่มทดสอบ</button>
  </div>

  <div class="history-section">
    <div class="history-title">── ประวัติล่าสุด ──</div>
    <div id="historyList"></div>
    <button class="export-btn" onclick="exportCSV()">💾 Export CSV</button>
  </div>
</div>

<script>
// ── Gauge ──
const gc = document.getElementById('gauge');
const gx = gc.getContext('2d');

function drawGauge(val, max=200) {
  gx.clearRect(0, 0, gc.width, gc.height);
  const cx=150, cy=165, r=120;
  const ratio = Math.min(val/max, 1);

  // BG arc
  gx.beginPath();
  gx.arc(cx, cy, r, Math.PI, 0, false);
  gx.strokeStyle = '#2a3a2a';
  gx.lineWidth = 16;
  gx.stroke();

  // Value arc
  if (ratio > 0) {
    gx.beginPath();
    gx.arc(cx, cy, r, Math.PI, Math.PI + ratio*Math.PI, false);
    gx.strokeStyle = ratio < 0.6 ? '#00ff88' : ratio < 0.85 ? '#00ccff' : '#ff4466';
    gx.lineWidth = 16;
    gx.shadowColor = ratio < 0.6 ? '#00ff88' : '#00ccff';
    gx.shadowBlur = 12;
    gx.stroke();
    gx.shadowBlur = 0;
  }

  // Ticks
  for (let i=0; i<=10; i++) {
    const a = Math.PI + i*(Math.PI/10);
    const ro = r+8, ri = i%5===0 ? r-10 : r-5;
    gx.beginPath();
    gx.moveTo(cx+ro*Math.cos(a), cy+ro*Math.sin(a));
    gx.lineTo(cx+ri*Math.cos(a), cy+ri*Math.sin(a));
    gx.strokeStyle = '#5a8a5a';
    gx.lineWidth = 1;
    gx.stroke();
  }

  // Needle
  const na = Math.PI + ratio*Math.PI;
  gx.beginPath();
  gx.moveTo(cx, cy);
  gx.lineTo(cx+(r-18)*Math.cos(na), cy+(r-18)*Math.sin(na));
  gx.strokeStyle = '#00ff88';
  gx.lineWidth = 3;
  gx.lineCap = 'round';
  gx.stroke();

  gx.beginPath();
  gx.arc(cx, cy, 6, 0, Math.PI*2);
  gx.fillStyle = '#00ff88';
  gx.fill();

  // Labels
  ['0','50','100','150','200'].forEach((lbl, i) => {
    const a = Math.PI + i*(Math.PI/4);
    const lx = cx+(r+22)*Math.cos(a), ly = cy+(r+22)*Math.sin(a);
    gx.fillStyle = '#5a8a5a';
    gx.font = '10px Share Tech Mono';
    gx.textAlign = 'center';
    gx.fillText(lbl, lx, ly+4);
  });
}

// ── Graph ──
const graphCanvas = document.getElementById('graph');
const grc = graphCanvas.getContext('2d');
let graphData = [];

function updateGraph(val, phase) {
  graphData.push({val, phase});
  if (graphData.length > 60) graphData.shift();

  const W = graphCanvas.width, H = graphCanvas.height;
  grc.clearRect(0, 0, W, H);

  const maxVal = Math.max(...graphData.map(d=>d.val), 1);
  const pad = 8;

  // Grid
  for (let i=1; i<4; i++) {
    const y = H - pad - (i/4)*(H-2*pad);
    grc.beginPath();
    grc.moveTo(pad, y); grc.lineTo(W-pad, y);
    grc.strokeStyle = 'rgba(42,58,42,0.6)';
    grc.lineWidth = 1;
    grc.setLineDash([2,4]);
    grc.stroke();
    grc.setLineDash([]);
  }

  // Line
  if (graphData.length < 2) return;
  grc.beginPath();
  graphData.forEach((d, i) => {
    const x = pad + i*(W-2*pad)/(graphData.length-1);
    const y = H - pad - (d.val/maxVal)*(H-2*pad);
    i===0 ? grc.moveTo(x,y) : grc.lineTo(x,y);
  });
  grc.strokeStyle = graphData[graphData.length-1].phase==='dl' ? '#00ff88' : '#00ccff';
  grc.lineWidth = 2;
  grc.shadowColor = graphData[graphData.length-1].phase==='dl' ? '#00ff88' : '#00ccff';
  grc.shadowBlur = 6;
  grc.stroke();
  grc.shadowBlur = 0;
}

// ── Animation ──
let animId = null;
let animAngle = 0;
function animateGauge() {
  animAngle = (animAngle + 3) % 180;
  const v = 100 + 80*Math.sin(animAngle * Math.PI/90);
  drawGauge(v);
  animId = requestAnimationFrame(animateGauge);
}
function stopAnim() { if(animId) { cancelAnimationFrame(animId); animId=null; } }

// ── History ──
let history = JSON.parse(localStorage.getItem('speedtest_history') || '[]');
renderHistory();

function saveHistory(rec) {
  history.push(rec);
  localStorage.setItem('speedtest_history', JSON.stringify(history));
  renderHistory();
}

function renderHistory() {
  const el = document.getElementById('historyList');
  if (!history.length) { el.innerHTML = '<div style="color:var(--sub);font-size:0.75rem">ยังไม่มีประวัติ</div>'; return; }
  el.innerHTML = history.slice(-5).reverse().map(r =>
    `<div class="history-row">
      <span>${r.timestamp}</span>
      <span style="color:var(--neon)">⬇${r.download}</span>
      <span style="color:var(--neon2)">⬆${r.upload}</span>
      <span style="color:var(--neon3)">📡${r.ping}ms</span>
    </div>`
  ).join('');
}

function exportCSV() {
  if (!history.length) { alert('ยังไม่มีข้อมูล'); return; }
  const header = 'timestamp,download,upload,ping,isp,ip,server';
  const rows = history.map(r => `${r.timestamp},${r.download},${r.upload},${r.ping},${r.isp||''},${r.ip||''},${r.server||''}`);
  const csv = [header, ...rows].join('\n');
  const blob = new Blob(['\ufeff'+csv], {type:'text/csv'});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = `speedtest_${Date.now()}.csv`;
  a.click();
}

// ── Test ──
function startTest() {
  const btn = document.getElementById('startBtn');
  btn.disabled = true;
  btn.textContent = '⏳ กำลังทดสอบ...';
  graphData = [];
  document.getElementById('dlVal').textContent = '—';
  document.getElementById('ulVal').textContent = '—';
  document.getElementById('pingVal').textContent = '—';
  document.getElementById('speedNum').textContent = '0.00';
  document.getElementById('ispBar').textContent = '';
  document.getElementById('serverText').textContent = '';
  document.getElementById('phaseText').textContent = 'กำลังเริ่มต้น...';
  animateGauge();

  const es = new EventSource('/run');
  es.onmessage = e => {
    const d = JSON.parse(e.data);

    if (d.phase === 'finding') {
      document.getElementById('phaseText').textContent = d.msg;
    }
    else if (d.phase === 'server') {
      document.getElementById('serverText').textContent = '📍 ' + d.msg;
      document.getElementById('ispBar').textContent = `🌐 IP: ${d.ip}  |  ISP: ${d.isp}`;
    }
    else if (d.phase === 'ping') {
      document.getElementById('pingVal').textContent = d.ping;
      document.getElementById('phaseText').textContent = '⬇ กำลังวัด Download...';
    }
    else if (d.phase === 'downloading') {
      document.getElementById('phaseText').textContent = d.msg;
    }
    else if (d.phase === 'download_done') {
      document.getElementById('dlVal').textContent = d.download;
      document.getElementById('speedNum').textContent = d.download;
      stopAnim(); drawGauge(d.download);
      updateGraph(d.download, 'dl');
      document.getElementById('phaseText').textContent = '⬆ กำลังวัด Upload...';
    }
    else if (d.phase === 'done') {
      stopAnim();
      document.getElementById('ulVal').textContent = d.upload;
      document.getElementById('dlVal').textContent = d.download;
      document.getElementById('speedNum').textContent = d.download;
      document.getElementById('phaseText').textContent = '✅ ทดสอบเสร็จสิ้น!';
      drawGauge(d.download);
      updateGraph(d.upload, 'ul');
      btn.disabled = false;
      btn.textContent = '🔄 ทดสอบอีกครั้ง';

      saveHistory({
        timestamp: new Date().toLocaleString('th-TH'),
        download: d.download,
        upload: d.upload,
        ping: d.ping,
        isp: d.isp,
        ip: d.ip,
        server: d.server
      });
      es.close();
    }
    else if (d.phase === 'error') {
      stopAnim(); drawGauge(0);
      document.getElementById('phaseText').textContent = '❌ ' + d.msg;
      btn.disabled = false;
      btn.textContent = '▶ ลองใหม่';
      es.close();
    }
  };

  es.onerror = () => {
    stopAnim();
    document.getElementById('phaseText').textContent = '❌ เชื่อมต่อเซิร์ฟเวอร์ไม่ได้';
    btn.disabled = false;
    btn.textContent = '▶ ลองใหม่';
    es.close();
  };
}

drawGauge(0);
</script>
</body>
</html>
