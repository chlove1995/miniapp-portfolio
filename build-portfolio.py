# -*- coding: utf-8 -*-
"""Build a single-file, offline-ready mini-program portfolio HTML."""
import base64, json, os, glob

SRC = r"C:\Users\Windows10\Desktop\ma"
DESKTOP = r"C:\Users\Windows10\Desktop"
OUT_DIR = r"C:\Users\Windows10\WorkBuddy\2026-11-25-17-14-14"
OUT = os.path.join(OUT_DIR, "miniapp-portfolio.html")

order = [
    "0 (1).jpg", "0 (2).jpg", "0 (3).jpg", "0 (4).jpg",
    "0 (5).jpg", "0 (6).jpg", "0 (7).jpg", "0 (8).jpg",
    "0 (9).jpg", "0.jpg", "gh_4031f3ca5277_258.jpg",
    os.path.join(DESKTOP, "4e83fa24fee28cd2d9c95a9bb7b28021.jpg"),
    os.path.join(DESKTOP, "31deadf64b32da853ff096e0a97968cd.jpg"),
]

imgs = {}
for i, fn in enumerate(order, 1):
    p = fn if os.path.isabs(fn) else os.path.join(SRC, fn)
    with open(p, "rb") as f:
        imgs[str(i)] = "data:image/jpeg;base64," + base64.b64encode(f.read()).decode("ascii")

HTML = r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>微信小程序 · 案例作品集</title>
<style>
:root{
  --ink:#1a1a1a; --ink2:#3d3833; --muted:#8b857c;
  --paper:#f7f5f2; --card:#fff; --line:#e8e3dc;
  --pink:#ff4785; --purple:#a259ff; --green:#07c160;
  --shadow:0 10px 30px rgba(26,26,26,.06);
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:"Noto Sans SC","PingFang SC","Microsoft YaHei",-apple-system,system-ui,sans-serif;
  background:var(--paper);color:var(--ink);-webkit-font-smoothing:antialiased;line-height:1.6}
.wrap{max-width:1180px;margin:0 auto;padding:0 40px}
img{display:block}

/* ---------- HERO ---------- */
.hero{background:#1a1a1a;color:#fff;position:relative;overflow:hidden;padding:84px 0 88px}
.hero::before{content:"";position:absolute;width:900px;height:900px;right:-180px;top:-360px;
  background:radial-gradient(circle,rgba(255,71,133,.22),transparent 62%);pointer-events:none}
.hero::after{content:"";position:absolute;width:760px;height:760px;right:120px;bottom:-480px;
  background:radial-gradient(circle,rgba(162,89,255,.20),transparent 62%);pointer-events:none}
.hero-grid{display:grid;grid-template-columns:1.12fr .88fr;gap:56px;align-items:center;position:relative;z-index:2}
.eyebrow{font-size:12px;letter-spacing:.32em;color:#ff9abb;font-weight:700;text-transform:uppercase}
.eyebrow span{display:inline-block;width:26px;height:1px;background:#ff9abb;vertical-align:middle;margin-right:12px}
h1{font-size:clamp(38px,4.5vw,64px);line-height:1.2;font-weight:800;letter-spacing:-.02em;margin-top:22px}
h1 em{font-style:normal;background:linear-gradient(90deg,#ff4785,#a259ff);-webkit-background-clip:text;background-clip:text;color:transparent}
.lead{margin-top:22px;font-size:16px;line-height:1.95;color:#c6c1ba;max-width:510px}
.stats{display:flex;gap:38px;margin-top:42px;flex-wrap:wrap}
.stat b{display:block;font-size:30px;font-weight:800;line-height:1.1;letter-spacing:-.02em}
.stat b i{font-style:normal;font-size:14px;font-weight:600;margin-left:3px;color:#ff9abb}
.stat span{font-size:12px;color:#938d85;letter-spacing:.06em}
.hint{margin-top:40px;display:inline-flex;align-items:center;gap:10px;font-size:13px;color:#b9b3ab;
  border:1px solid rgba(255,255,255,.18);border-radius:99px;padding:9px 18px}
.hint .g{width:7px;height:7px;border-radius:50%;background:var(--green);box-shadow:0 0 0 4px rgba(7,193,96,.14)}

.visual{height:420px;position:relative;display:flex;align-items:center;justify-content:center;overflow:hidden}
.dot-ring{position:absolute;inset:0;pointer-events:none}
.dot-ring i{position:absolute;left:50%;top:50%;width:3px;height:13px;border-radius:3px;
  background:rgba(255,255,255,.5);transform-origin:50% 50%}
.core{width:212px;height:212px;border-radius:50%;z-index:2;text-align:center;
  background:linear-gradient(140deg,#ff4785,#a259ff);box-shadow:0 26px 70px rgba(162,89,255,.38);
  display:flex;flex-direction:column;align-items:center;justify-content:center;position:relative}
.core b{font-size:66px;line-height:1;font-weight:800;letter-spacing:-.04em}
.core span{font-size:11px;letter-spacing:.34em;margin-top:8px;opacity:.9}
.core small{font-size:11px;letter-spacing:.1em;margin-top:16px;opacity:.82}
.pill{position:absolute;z-index:3;background:rgba(255,255,255,.09);border:1px solid rgba(255,255,255,.16);
  color:#e9e5e0;font-size:11px;letter-spacing:.08em;padding:7px 13px;border-radius:99px;white-space:nowrap;
  backdrop-filter:blur(4px)}
.p1{top:44px;left:16px} .p2{bottom:58px;left:-6px} .p3{top:96px;right:-4px} .p4{bottom:40px;right:26px}

/* ---------- SECTION ---------- */
.section{padding:66px 0 74px}
.sec-head{display:flex;align-items:flex-end;justify-content:space-between;gap:20px;margin-bottom:28px;flex-wrap:wrap}
.sec-head .kicker{font-size:11px;letter-spacing:.28em;color:var(--purple);font-weight:800;text-transform:uppercase}
.sec-head h2{font-size:30px;font-weight:800;letter-spacing:-.01em;margin-top:8px}
.sec-head p{font-size:13px;color:var(--muted);max-width:420px;text-align:right}
.notice{font-size:11px;color:#a29b91;margin-top:18px;line-height:1.8}

.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:20px}
@media(max-width:1040px){.grid{grid-template-columns:repeat(3,1fr)}}
@media(max-width:760px){.grid{grid-template-columns:repeat(2,1fr);gap:14px}.wrap{padding:0 20px}
  .hero-grid{grid-template-columns:1fr}.visual{height:300px}.hero{padding:56px 0 60px}.sec-head p{text-align:left}}
@media(max-width:440px){.grid{gap:10px}.card{padding:10px}.card h3{font-size:14px}}
.card{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:16px;
  box-shadow:var(--shadow);cursor:pointer;transition:transform .25s ease,box-shadow .25s ease,border-color .25s ease;
  break-inside:avoid;page-break-inside:avoid}
.card:hover{transform:translateY(-6px);box-shadow:0 20px 42px rgba(26,26,26,.12);border-color:#e0c9ff}
.code{border:1px solid #f0ede8;border-radius:12px;overflow:hidden;aspect-ratio:1;background:#fff}
.code img{width:100%;height:100%;object-fit:contain}
.card-top{display:flex;justify-content:space-between;align-items:center;gap:8px;margin:14px 2px 9px}
.num{font-size:11px;color:#b0a99f;letter-spacing:.14em;font-weight:800}
.tag{font-size:10px;padding:4px 9px;border-radius:99px;background:#f4efff;color:#7b46c9;white-space:nowrap;font-weight:600}
.card h3{font-size:16px;font-weight:800;line-height:1.4;letter-spacing:-.01em}
.card .sub{font-size:11px;color:#a09a91;margin-top:5px;min-height:17px;line-height:1.5}
.card .foot{margin-top:13px;padding-top:10px;border-top:1px dashed var(--line);display:flex;align-items:center;gap:7px;
  font-size:11px;color:var(--ink2)}
.card .foot .g{width:7px;height:7px;border-radius:50%;background:var(--green);flex:none}
.vdesc{color:#9b6a2f}
.card.cta{grid-column:span 3;background:#1a1a1a;border-color:#1a1a1a;color:#fff;min-height:180px;
  display:flex;flex-direction:column;justify-content:center;align-items:flex-start;padding:30px 34px;
  position:relative;overflow:hidden}
.card.cta::before{content:"";position:absolute;width:300px;height:300px;right:-70px;top:-110px;
  background:radial-gradient(circle,rgba(162,89,255,.42),transparent 65%);pointer-events:none}
.card.cta .ci{font-size:11px;letter-spacing:.22em;color:#ff9abb;font-weight:800;position:relative}
.card.cta h3{font-size:26px;color:#fff;line-height:1.35;margin-top:12px;position:relative}
.card.cta p{font-size:13px;color:#aaa49c;margin-top:10px;line-height:1.8;max-width:520px;position:relative}
.card.cta .go{margin-top:20px;background:#ff4785;color:#fff;font-size:12px;font-weight:700;
  padding:9px 18px;border-radius:99px;position:relative}
@media(max-width:760px){.card.cta{grid-column:span 1}}
@media(max-width:440px){.card.cta{grid-column:span 1;padding:20px}}

/* ---------- CAPABILITY ---------- */
.cap{background:#fff;border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:60px 0 64px}
.cap .sec-head p{text-align:left;max-width:560px}
.cap-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:26px}
@media(max-width:760px){.cap-grid{grid-template-columns:repeat(2,1fr)}}
.cap-item{padding:22px;border:1px solid var(--line);border-radius:14px;background:var(--paper)}
.cap-item .ci{font-size:11px;letter-spacing:.16em;color:var(--purple);font-weight:800}
.cap-item b{display:block;font-size:16px;margin:9px 0 6px;font-weight:800}
.cap-item span{font-size:12px;color:var(--muted);line-height:1.75}

/* ---------- FOOTER ---------- */
.end{background:#1a1a1a;color:#fff;padding:62px 0 34px;position:relative;overflow:hidden}
.end::before{content:"";position:absolute;width:600px;height:600px;left:-240px;top:-300px;
  background:radial-gradient(circle,rgba(255,71,133,.16),transparent 65%)}
.end-in{position:relative;z-index:2}
.end h2{font-size:32px;font-weight:800;letter-spacing:-.01em}
.end h2 em{font-style:normal;color:#ff8fb3}
.end p{color:#aaa49c;font-size:14px;margin-top:14px;max-width:520px;line-height:1.9}
.end .bar{margin-top:34px;display:flex;align-items:center;gap:14px;flex-wrap:wrap}
.end .bar a{color:#fff;text-decoration:none;font-size:13px;border:1px solid rgba(255,255,255,.22);
  border-radius:99px;padding:10px 20px;transition:.2s}
.end .bar a:hover{background:#fff;color:#1a1a1a}
.copyright{margin-top:52px;padding-top:20px;border-top:1px solid rgba(255,255,255,.1);
  font-size:11px;color:#6f6a64;display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap}

/* ---------- UI ---------- */
.fab{position:fixed;right:24px;bottom:24px;z-index:60;display:flex;gap:10px}
.fab button{font-family:inherit;font-size:13px;font-weight:700;color:#fff;background:#1a1a1a;border:0;
  border-radius:99px;padding:12px 20px;cursor:pointer;box-shadow:0 8px 24px rgba(0,0,0,.22);transition:.2s}
.fab button:hover{background:linear-gradient(90deg,#ff4785,#a259ff);transform:translateY(-2px)}
.modal{position:fixed;inset:0;z-index:100;background:rgba(18,16,14,.76);display:none;place-items:center;padding:20px;
  backdrop-filter:blur(6px)}
.modal.on{display:grid}
.modal-box{background:#fff;border-radius:22px;padding:28px 28px 24px;width:min(400px,92vw);text-align:center;position:relative;
  box-shadow:0 30px 80px rgba(0,0,0,.3)}
.modal-box .x{position:absolute;right:16px;top:14px;border:0;background:#f3f0ec;width:30px;height:30px;border-radius:50%;
  cursor:pointer;font-size:16px;color:#555;line-height:1}
.modal-box img{width:100%;max-width:300px;margin:6px auto 16px;border-radius:12px}
.modal-box .mt{font-size:11px;letter-spacing:.16em;color:var(--purple);font-weight:800}
.modal-box h3{font-size:21px;font-weight:800;margin-top:6px}
.modal-box p{font-size:12px;color:var(--muted);margin-top:8px;line-height:1.8}
.modal-box .tip{margin-top:16px;background:var(--paper);border-radius:10px;padding:11px;font-size:12px;color:var(--ink2)}

/* ---------- PRINT / PDF ---------- */
@page{size:A4;margin:11mm}
@media print{
  *{-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}
  body{background:#fff}
  .wrap{max-width:none;padding:0}
  .fab,.modal,.no-print{display:none!important}
  .hero{padding:22px 0 26px}
  .hero-grid{grid-template-columns:1.25fr .75fr;gap:18px}
  .eyebrow{font-size:8px}
  h1{font-size:30px;margin-top:12px}
  .lead{font-size:10px;margin-top:9px;line-height:1.7}
  .stats{margin-top:16px;gap:18px}
  .stat b{font-size:19px} .stat span{font-size:8px}
  .hint{margin-top:16px;font-size:8px;padding:5px 12px}
  .visual{height:150px}
  .dot-ring{transform:scale(.40)}
  .core{width:96px;height:96px;box-shadow:none}
  .core b{font-size:32px} .core span{font-size:7px;margin-top:4px} .core small{display:none}
  .pill{font-size:7px;padding:4px 8px}
  .p1{top:10px;left:0} .p2{bottom:12px;left:0} .p3{top:26px;right:0} .p4{bottom:8px;right:0}
  .section{padding:18px 0 20px}
  .sec-head{margin-bottom:12px}
  .sec-head h2{font-size:19px;margin-top:4px}
  .sec-head p,.sec-head .kicker{font-size:8px}
  .notice{font-size:8px;margin-top:9px}
  .grid{grid-template-columns:repeat(3,1fr);gap:9px}
  .card{padding:9px;border-radius:10px;box-shadow:none}
  .card-top{margin:8px 1px 5px}
  .num,.tag{font-size:7px} .tag{padding:2px 6px}
  .card h3{font-size:11px}
  .card .sub{font-size:8px;margin-top:3px;min-height:0}
  .card .foot{font-size:8px;margin-top:7px;padding-top:6px}
  .card.cta{grid-column:span 2;padding:12px 16px;min-height:0}
  .card.cta .ci{font-size:7px}
  .card.cta h3{font-size:14px;margin-top:5px}
  .card.cta p{font-size:8px;margin-top:4px}
  .card.cta .go{font-size:8px;padding:4px 10px;margin-top:7px}
  .cap{padding:20px 0;break-before:page;page-break-before:always}
  .cap-grid{gap:8px;margin-top:12px}
  .cap-item{padding:11px}
  .cap-item .ci{font-size:7px} .cap-item b{font-size:11px;margin:5px 0 3px} .cap-item span{font-size:8px}
  .end{padding:24px 0 16px}
  .end h2{font-size:21px} .end p{font-size:9px;margin-top:7px}
  .end .bar{margin-top:14px} .end .bar a{font-size:9px;padding:6px 12px}
  .copyright{margin-top:20px;padding-top:10px;font-size:7px}
}
</style>
</head>
<body>

<header class="hero">
  <div class="wrap hero-grid">
    <div>
      <div class="eyebrow"><span></span>WECHAT MINI PROGRAM · PORTFOLIO</div>
      <h1>每一个<em>码</em>，<br>都是一次交付</h1>
      <p class="lead">已开发的微信小程序案例作品集。下面 13 个小程序码，用微信「扫一扫」或长按识别，就能直接打开体验每一个项目。</p>
      <div class="stats">
        <div class="stat"><b>13<i>个</i></b><span>案例项目</span></div>
        <div class="stat"><b>1<i>次</i></b><span>扫码直达体验</span></div>
        <div class="stat"><b>N<i>类</i></b><span>业务场景覆盖</span></div>
      </div>
      <div class="hint"><span class="g"></span>点击任意案例可放大扫码</div>
    </div>
    <div class="visual">
      <div class="dot-ring" id="ring"></div>
      <span class="pill p1">微信生态</span>
      <span class="pill p2">扫码即达</span>
      <span class="pill p3">原生体验</span>
      <span class="pill p4">多行业</span>
      <div class="core"><b>13</b><span>CASES</span><small>微信小程序案例</small></div>
    </div>
  </div>
</header>

<main>
  <section class="section">
    <div class="wrap">
      <div class="sec-head">
        <div><div class="kicker">SELECTED WORKS / 01</div><h2>案例一览 · 扫码即看</h2></div>
        <p>零售电商、母婴、美业、家政、酒店、户外露营……不同行业，同一套从设计到上线的交付能力。</p>
      </div>
      <div class="grid" id="grid"></div>
      <p class="notice">* 案例名称依据小程序码可辨识信息整理，行业标签为按码面视觉所做的场景归类，具体以实际项目为准。<br>
      * 案例图片与小程序码版权归各品牌方所有，仅作项目展示用途。</p>
    </div>
  </section>

  <section class="cap">
    <div class="wrap">
      <div class="sec-head">
        <div><div class="kicker">WHAT WE DO / 02</div><h2>从一个想法，到一个能上线的小程序</h2></div>
        <p>以下为通用交付链路说明，可按实际项目范围调整。</p>
      </div>
      <div class="cap-grid">
        <div class="cap-item"><div class="ci">01 / DISCOVERY</div><b>需求梳理</b><span>业务流程、角色权限、页面清单与原型确认，先把要做的事说清楚。</span></div>
        <div class="cap-item"><div class="ci">02 / DESIGN</div><b>界面设计</b><span>视觉规范、组件体系与移动端适配，保证品牌调性统一。</span></div>
        <div class="cap-item"><div class="ci">03 / DEVELOP</div><b>前端开发</b><span>原生小程序 / 框架开发，交互细节与性能优化同步落地。</span></div>
        <div class="cap-item"><div class="ci">04 / CLOUD</div><b>云开发 / 后端</b><span>数据建模、云函数、接口联调与后台管理能力。</span></div>
        <div class="cap-item"><div class="ci">05 / GROWTH</div><b>交易与营销</b><span>支付、会员、优惠券、活动页与分享裂变等常见业务模块。</span></div>
        <div class="cap-item"><div class="ci">06 / LAUNCH</div><b>上线与迭代</b><span>提审发布、体验问题跟进，以及后续版本持续迭代。</span></div>
      </div>
    </div>
  </section>
</main>

<footer class="end">
  <div class="wrap end-in">
    <h2>想做一个<em>类似的小程序</em>？</h2>
    <p>把你的业务场景和大概想法发过来，我们一起把页面清单、功能范围和上线节奏聊清楚。上面的每一个码，都可以直接点开看效果。</p>
    <div class="bar no-print"><a href="#grid">↓ 回看案例</a><a href="#" onclick="window.print();return false;">导出 PDF / 打印</a></div>
    <div class="copyright"><span>© 2026 微信小程序案例作品集</span><span>用微信「扫一扫」体验 · 建议手机端扫码</span></div>
  </div>
</footer>

<div class="fab no-print"><button onclick="window.print()">打印 / 导出 PDF</button></div>

<div class="modal" id="modal" onclick="if(event.target===this)closeM()">
  <div class="modal-box">
    <button class="x" onclick="closeM()" aria-label="关闭">×</button>
    <div class="mt" id="mNum">CASE 01</div>
    <img id="mImg" src="" alt="小程序码">
    <h3 id="mName"></h3>
    <p id="mSub"></p>
    <div class="tip">用微信「扫一扫」打开，或保存图片后在微信内长按识别</div>
  </div>
</div>

<script>
/* ===== 修改指引：只需改 CASES 数组里的 name / sub / tag，即可替换案例名称与行业标签 ===== */
const IMGS = __IMAGE_DATA__;
const CASES = [
  {img:1,  name:"橙黄票券标识",   sub:"码面为几何品牌标识，未含文字",       tag:"卡券 / 品牌", desc:true},
  {img:2,  name:"酸匠",          sub:"SUAN JIANG",                        tag:"食品 / 餐饮"},
  {img:3,  name:"粉色人形标识",   sub:"码面为抽象人形品牌标识，未含文字",     tag:"社交 / 会员", desc:true},
  {img:4,  name:"铭硕母婴",       sub:"MISOU · INFANT & MOM",              tag:"母婴 / 零售"},
  {img:5,  name:"BEAUTY SEEDS",  sub:"黑色圆形品牌标识",                   tag:"美业 / 品牌"},
  {img:6,  name:"家庭保洁体验页", sub:"码面为「首次体验保洁 · ¥165」活动页",  tag:"家政 / 生活服务"},
  {img:7,  name:"Camping Tomorrow", sub:"露营帐篷与山野主题标识",           tag:"户外 / 露营"},
  {img:8,  name:"FONE HOTEL",    sub:"码面英文标识部分被码点遮挡",          tag:"酒店 / 住宿"},
  {img:9,  name:"蜜蜂卡通 IP",    sub:"橙黄蜜蜂与绿色蜗牛壳卡通形象",        tag:"亲子 / 儿童", desc:true},
  {img:10, name:"鑫选易购",       sub:"橙色圆形 + 蓝色 U 形标识",            tag:"电商 / 购物"},
  {img:11, name:"紫底闪电标识",   sub:"紫色圆角方 + 云朵闪电图形",           tag:"工具 / 服务", desc:true},
  {img:12, name:"粉色小鱼标识",   sub:"粉色圆环与小鱼图形，未含文字",         tag:"餐饮 / 生鲜", desc:true},
  {img:13, name:"绿色山形标识",   sub:"绿色渐变圆与线条图形，未含文字",       tag:"文旅 / 品牌", desc:true}
];

const grid = document.getElementById('grid');
CASES.forEach((c,i)=>{
  const n = String(i+1).padStart(2,'0');
  const el = document.createElement('article');
  el.className = 'card';
  el.innerHTML = '<div class="code"><img src="'+IMGS[c.img]+'" alt="'+c.name+' 小程序码" loading="lazy"></div>'
    + '<div class="card-top"><span class="num">CASE '+n+'</span><span class="tag">'+c.tag+'</span></div>'
    + '<h3'+(c.desc?' class="vdesc"':'')+'>'+c.name+'</h3>'
    + '<div class="sub">'+c.sub+'</div>'
    + '<div class="foot"><span class="g"></span>微信扫码，直接体验</div>';
  el.onclick = ()=>openM(i);
  grid.appendChild(el);
});

const ctaCard = document.createElement('article');
ctaCard.className = 'card cta';
ctaCard.innerHTML = '<div class="ci">NEXT PROJECT</div>'
  + '<h3>下一个案例，可能是你的</h3>'
  + '<p>把业务场景和大概想法发过来，一起把页面清单、功能范围和上线节奏聊清楚。</p>'
  + '<span class="go">欢迎沟通 →</span>';
ctaCard.onclick = ()=>document.querySelector('.end').scrollIntoView({behavior:'smooth'});
grid.appendChild(ctaCard);

const ring = document.getElementById('ring');
for(let layer=0; layer<3; layer++){
  const count = [30, 40, 50][layer];
  const radius = [132, 176, 216][layer];
  for(let i=0;i<count;i++){
    const deg = (i/count)*360 + layer*7;
    const d = document.createElement('i');
    d.style.transform = 'translate(-50%,-50%) rotate('+deg+'deg) translateY('+(-radius)+'px)';
    d.style.opacity = (0.28 + (i%4)*0.16).toFixed(2);
    d.style.height = (10 + (i%3)*5)+'px';
    ring.appendChild(d);
  }
}

function openM(i){
  const c = CASES[i], n = String(i+1).padStart(2,'0');
  document.getElementById('mNum').textContent = 'CASE ' + n + ' / ' + c.tag;
  document.getElementById('mImg').src = IMGS[c.img];
  document.getElementById('mName').textContent = c.name;
  document.getElementById('mSub').textContent = c.sub;
  document.getElementById('modal').classList.add('on');
  document.body.style.overflow = 'hidden';
}
function closeM(){
  document.getElementById('modal').classList.remove('on');
  document.body.style.overflow = '';
}
document.addEventListener('keydown', e=>{ if(e.key==='Escape') closeM(); });
</script>
</body>
</html>
'''

html = HTML.replace("__IMAGE_DATA__", json.dumps(imgs, ensure_ascii=False))
with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)
print("WROTE", OUT, os.path.getsize(OUT), "bytes")
