#!/usr/bin/env python3
"""Build Lao Xiang Tennis · Racket Service brand proposal — 5 directions, 13 slides."""
import base64, os

ASSET = "/Users/kay/.cursor/projects/Users-kay-Downloads-For-Works-Main/assets"
OUT   = "/Users/kay/Downloads/For Works/Main/lao-xiang-brand-proposal.html"

def b64(fn):
    with open(os.path.join(ASSET, fn), "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode()

img1 = b64("___-794bbe46-5b50-4b0a-888c-a646275a90ad.png")   # 方案一·莫比乌斯之环
img2 = b64("___-2df21e6a-02d3-4092-8c00-253e567b167d.png")   # 方案二·骑士勋章
img3 = b64("___-eddb24a7-0356-4660-a5e9-81deac6905a0.png")   # 方案三·幻视立方
img4 = b64("___-f984d2eb-bda2-44f3-bbb5-f5a2035da021.png")   # 方案四·核心之结
img5 = b64("___-4f301c52-d516-4ee0-89df-63d996203d45.png")   # 方案五·轨迹之线

print("Images loaded. Building HTML…")

HTML = f"""<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>老项网球 · Racket Service — LOGO 品牌设计提案</title>
<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0;}}
html,body{{width:100%;height:100%;overflow:hidden;background:#0d0d0d;}}
:root{{
  --bg:#111213;--red:#d63031;--rdim:rgba(214,48,49,.14);
  --w:#fff;--w6:rgba(255,255,255,.6);--w3:rgba(255,255,255,.3);
  --w12:rgba(255,255,255,.12);--w06:rgba(255,255,255,.06);
  --D:'Archivo Black',sans-serif;--B:'Space Grotesk',sans-serif;
}}

/* ── ENGINE ── */
.deck{{position:relative;width:100vw;height:100vh;height:100dvh;}}
.slide{{
  position:absolute;inset:0;width:100%;height:100vh;height:100dvh;
  overflow:hidden;
  background:linear-gradient(135deg,#111213 0%,#1a1b1d 50%,#111213 100%);
  opacity:0;pointer-events:none;transition:opacity .5s ease;
}}
.slide.active{{opacity:1;pointer-events:all;}}

/* ── CHROME ── */
.chrome{{position:absolute;inset:0;z-index:10;pointer-events:none;}}
.chr-top{{
  position:absolute;top:clamp(16px,2.8vh,36px);
  left:clamp(20px,3.2vw,52px);right:clamp(20px,3.2vw,52px);
  display:flex;align-items:center;justify-content:space-between;
}}
.slide-num{{font-family:var(--B);font-size:clamp(.48rem,.72vw,.62rem);font-weight:500;color:var(--w3);letter-spacing:.12em;}}
.dots{{display:flex;gap:5px;align-items:center;pointer-events:all;}}
.dot{{width:5px;height:5px;border-radius:50%;background:var(--w12);cursor:pointer;transition:all .3s;}}
.dot.active{{background:var(--red);transform:scale(1.5);}}
.chr-bot{{
  position:absolute;bottom:clamp(14px,2.5vh,32px);
  left:clamp(20px,3.2vw,52px);right:clamp(20px,3.2vw,52px);
  display:flex;align-items:center;justify-content:space-between;
}}
.bmark{{font-family:var(--B);font-size:clamp(.42rem,.62vw,.54rem);font-weight:500;letter-spacing:.22em;text-transform:uppercase;color:var(--w3);}}
.arrows{{display:flex;gap:7px;pointer-events:all;}}
.arr{{
  width:clamp(24px,2.6vw,34px);height:clamp(24px,2.6vw,34px);
  border:1px solid var(--w12);background:transparent;color:var(--w3);
  font-size:clamp(.6rem,.85vw,.76rem);cursor:pointer;
  display:flex;align-items:center;justify-content:center;
  transition:all .2s;border-radius:2px;
}}
.arr:hover{{border-color:var(--red);color:var(--red);}}

/* ── LAYOUT ── */
.two-col{{
  position:absolute;inset:0;display:flex;align-items:center;
  padding:clamp(48px,7.5vh,76px) clamp(20px,3.2vw,52px) clamp(40px,6vh,64px);
  gap:clamp(28px,4.5vw,64px);
}}
.col-l{{display:flex;flex-direction:column;gap:clamp(10px,1.6vh,18px);}}
.col-r{{flex:1;display:flex;flex-direction:column;gap:clamp(8px,1.4vh,16px);}}

/* ── TYPE ── */
.ey{{font-family:var(--B);font-size:clamp(.48rem,.76vw,.64rem);font-weight:600;letter-spacing:.28em;text-transform:uppercase;color:var(--red);}}
.h1{{font-family:var(--D);font-size:clamp(1.9rem,4.8vw,4.4rem);color:var(--w);line-height:.92;letter-spacing:-.02em;}}
.h2{{font-family:var(--D);font-size:clamp(1.2rem,2.8vw,2.6rem);color:var(--w);line-height:.95;letter-spacing:-.02em;}}
.bt{{font-family:var(--B);font-size:clamp(.62rem,.96vw,.8rem);font-weight:400;color:var(--w6);line-height:1.75;}}
.rule{{width:clamp(28px,4vw,56px);height:2px;background:var(--red);}}
.tag{{display:inline-block;font-family:var(--B);font-size:clamp(.44rem,.66vw,.57rem);font-weight:600;letter-spacing:.15em;text-transform:uppercase;color:var(--red);border:1px solid var(--red);padding:3px 8px;border-radius:2px;}}

/* ── LOGO IMAGE PANEL (single, large, hover-zoom) ── */
.logo-panel{{
  flex:1;border-radius:5px;overflow:hidden;cursor:zoom-in;
  background:#ffffff;
  display:flex;align-items:center;justify-content:center;
  min-height:clamp(220px,52vh,500px);
  position:relative;
}}
.logo-panel.dark{{background:#0c0c0c;border:1px solid #242424;}}
.logo-panel img{{
  max-width:86%;max-height:86%;object-fit:contain;display:block;
  transition:transform .45s cubic-bezier(.25,.46,.45,.94);
  will-change:transform;
}}
.logo-panel:hover img{{transform:scale(1.07);}}

/* ── ANALYSIS ROWS ── */
.ai{{padding:clamp(6px,1vh,11px) 0;border-bottom:1px solid var(--w06);display:flex;flex-direction:column;gap:3px;}}
.ai:last-child{{border-bottom:none;}}
.alb{{font-family:var(--B);font-size:clamp(.44rem,.65vw,.56rem);font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--red);}}
.av{{font-family:var(--B);font-size:clamp(.58rem,.88vw,.74rem);color:var(--w6);line-height:1.55;}}

/* ── TOC ── */
.ti{{display:flex;align-items:center;gap:clamp(10px,1.6vw,20px);padding:clamp(7px,1.1vh,13px) clamp(10px,1.5vw,18px);border:1px solid var(--w06);background:var(--w06);}}
.ti.ft{{border-color:var(--red);background:var(--rdim);}}
.tn{{font-family:var(--D);font-size:clamp(.6rem,1vw,.86rem);color:var(--red);min-width:2em;}}
.tt{{font-family:var(--B);font-size:clamp(.58rem,.88vw,.76rem);font-weight:500;color:var(--w6);}}
.ti.ft .tt{{color:var(--w);}}

/* ── BRIEF ── */
.bc{{padding:clamp(10px,1.6vh,20px) clamp(12px,1.8vw,22px);border-left:2.5px solid var(--red);background:var(--w06);display:flex;flex-direction:column;gap:3px;}}
.bcl{{font-family:var(--B);font-size:clamp(.44rem,.65vw,.56rem);font-weight:700;letter-spacing:.22em;text-transform:uppercase;color:var(--red);}}
.bcv{{font-family:var(--B);font-size:clamp(.58rem,.9vw,.76rem);font-weight:500;color:var(--w);line-height:1.5;}}

/* ── CONCEPT ── */
.cp{{display:flex;gap:clamp(10px,1.6vw,18px);align-items:flex-start;}}
.cn{{font-family:var(--D);font-size:clamp(1.3rem,2.6vw,2.4rem);color:var(--red);opacity:.28;line-height:1;flex-shrink:0;width:clamp(26px,3.2vw,44px);}}
.cb{{display:flex;flex-direction:column;gap:4px;padding-top:3px;}}
.ct{{font-family:var(--B);font-size:clamp(.58rem,.92vw,.78rem);font-weight:700;color:var(--w);letter-spacing:.04em;}}
.cd{{font-family:var(--B);font-size:clamp(.54rem,.82vw,.7rem);color:var(--w3);line-height:1.65;}}

/* ── COVER X ── */
.cx{{position:relative;width:clamp(130px,24vw,240px);height:clamp(130px,24vw,240px);}}
.cx::before,.cx::after{{content:'';position:absolute;width:100%;height:clamp(14px,3%,24px);background:linear-gradient(90deg,#a01818,var(--red));top:50%;left:0;transform-origin:center;margin-top:calc(-1*clamp(7px,1.5%,12px));border-radius:2px;}}
.cx::before{{transform:rotate(45deg);}}
.cx::after{{transform:rotate(-45deg);}}
.cd2{{position:absolute;width:34%;height:34%;top:33%;left:33%;border:1.5px solid rgba(214,48,49,.45);transform:rotate(45deg);}}

/* ── BADGE GRID ── */
.bg-grid{{display:flex;flex-direction:column;gap:clamp(12px,2.2vh,24px);justify-content:center;}}
.bg-row{{display:flex;gap:clamp(12px,2.2vw,24px);justify-content:center;}}
.bi{{display:flex;flex-direction:column;gap:5px;align-items:center;}}
.bcirc{{border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0;}}
.blbl{{font-family:var(--B);font-size:clamp(.42rem,.65vw,.56rem);font-weight:700;color:var(--w);text-align:center;letter-spacing:.04em;}}
.bsub{{font-family:var(--B);font-size:clamp(.36rem,.55vw,.48rem);color:var(--w3);text-align:center;letter-spacing:.08em;}}

/* ── BW BOXES ── */
.bwr{{display:flex;gap:clamp(8px,1.5vw,18px);}}
.bwb{{flex:1;padding:clamp(8px,1.4vh,16px);display:flex;flex-direction:column;align-items:center;gap:clamp(5px,.9vh,9px);border-radius:3px;}}
.bwb img{{height:clamp(32px,7.5vh,68px);width:100%;object-fit:contain;}}
.bwb.bwl{{background:#fff;}}
.bwb.bwk{{background:#000;border:1px solid #333;}}
.bwb.bwn{{background:#c4a882;}}
.bwb.bwk img{{filter:invert(1);}}
.bwb.bwn img{{filter:brightness(0);}}
.bwtx{{font-family:var(--B);font-size:clamp(.4rem,.6vw,.52rem);font-weight:600;letter-spacing:.15em;text-transform:uppercase;}}
.bwl .bwtx{{color:#888;}}.bwk .bwtx{{color:rgba(255,255,255,.3);}}.bwn .bwtx{{color:rgba(0,0,0,.4);}}

/* ── BIZ CARD ── */
.biz{{background:#111;border:1px solid #2a2a2a;border-radius:3px;padding:clamp(10px,1.8vh,20px) clamp(12px,1.8vw,22px);display:flex;flex-direction:column;justify-content:space-between;min-height:clamp(72px,13vh,120px);position:relative;overflow:hidden;}}
.biz::after{{content:'X';position:absolute;right:-4px;top:50%;transform:translateY(-50%);font-family:var(--D);font-size:clamp(3rem,6.5vw,6.5rem);color:rgba(214,48,49,.05);line-height:1;pointer-events:none;}}
.biz-t{{display:flex;align-items:center;gap:9px;}}
.biz-logo{{height:clamp(16px,2.8vh,28px);object-fit:contain;}}
.biz-name{{font-family:var(--D);font-size:clamp(.52rem,.85vw,.72rem);color:var(--w);letter-spacing:.04em;}}
.biz-bot{{font-family:var(--B);font-size:clamp(.4rem,.6vw,.52rem);color:rgba(255,255,255,.2);letter-spacing:.08em;}}

/* ── ANIMATIONS ── */
@keyframes fU{{from{{opacity:0;transform:translateY(16px);}}to{{opacity:1;transform:translateY(0);}}}}
@keyframes fI{{from{{opacity:0;}}to{{opacity:1;}}}}
@keyframes sI{{from{{opacity:0;transform:scale(.86);}}to{{opacity:1;transform:scale(1);}}}}
@keyframes xW{{from{{transform:scaleX(0);}}to{{transform:scaleX(1);}}}}
.slide.active .a1{{animation:fU .55s ease .08s both;}}
.slide.active .a2{{animation:fU .55s ease .2s both;}}
.slide.active .a3{{animation:fU .55s ease .32s both;}}
.slide.active .a4{{animation:fU .55s ease .44s both;}}
.slide.active .a5{{animation:fU .55s ease .56s both;}}
.slide.active .a6{{animation:fU .55s ease .68s both;}}
.slide.active .aFI{{animation:fI .7s ease .1s both;}}
.slide.active .aSC{{animation:sI .65s cubic-bezier(.16,1,.3,1) .15s both;}}
.slide.active .aRU{{animation:xW .45s ease .38s both;transform-origin:left;}}
@media(prefers-reduced-motion:reduce){{.slide *{{animation:none!important;opacity:1!important;transform:none!important;}}}}
</style>
</head>
<body>
<div class="deck" id="deck">

<!-- ══ 01 COVER ══ -->
<div class="slide active" id="s01">
  <div class="two-col">
    <div class="col-l" style="flex:0 0 54%;">
      <div class="ey a1">LOGO 品牌设计提案</div>
      <div class="h1 a2">老项网球<br>穿线<br>工作室</div>
      <div class="rule aRU"></div>
      <div class="bt a3">Racket Service · 赛级穿线师<br>精工穿线，每一张拍面的承诺</div>
      <div class="a4" style="display:flex;gap:7px;flex-wrap:wrap;margin-top:4px;">
        <span class="tag">赛级穿线</span><span class="tag">五方向提案</span><span class="tag">2026</span>
      </div>
    </div>
    <div style="flex:1;display:flex;align-items:center;justify-content:center;position:relative;">
      <div style="position:absolute;width:clamp(180px,36vw,380px);height:clamp(180px,36vw,380px);opacity:.05;" class="aFI">
        <div style="position:absolute;width:100%;height:clamp(30px,5%,48px);background:#fff;top:50%;left:0;transform:rotate(45deg);transform-origin:center;margin-top:calc(-1*clamp(15px,2.5%,24px));"></div>
        <div style="position:absolute;width:100%;height:clamp(30px,5%,48px);background:#fff;top:50%;left:0;transform:rotate(-45deg);transform-origin:center;margin-top:calc(-1*clamp(15px,2.5%,24px));"></div>
      </div>
      <div class="cx aSC"><div class="cd2"></div></div>
    </div>
  </div>
</div>

<!-- ══ 02 TOC ══ -->
<div class="slide" id="s02">
  <div class="two-col">
    <div class="col-l" style="flex:0 0 36%;">
      <div class="ey a1">目录</div>
      <div class="h2 a2">Contents</div>
      <div class="rule aRU"></div>
      <div class="bt a3" style="max-width:24ch;">五个方向，一个选择。<br>从品牌根源出发，为老项找到属于自己的那个 X。</div>
    </div>
    <div class="col-r">
      <div class="ti a2"><span class="tn">01</span><span class="tt">品牌背景 · Brand Brief</span></div>
      <div class="ti a2"><span class="tn">02</span><span class="tt">设计理念 · Design Concept</span></div>
      <div class="ti ft a3" style="flex-direction:column;align-items:flex-start;gap:6px;">
        <div style="display:flex;align-items:center;gap:clamp(10px,1.6vw,20px);width:100%;"><span class="tn">03</span><span class="tt" style="color:var(--w);">设计方案 · 五个 LOGO 方向</span></div>
        <div style="padding-left:clamp(22px,3.2vw,44px);display:flex;gap:clamp(5px,.9vw,12px);flex-wrap:wrap;">
          <span style="font-family:var(--B);font-size:clamp(.42rem,.62vw,.54rem);color:rgba(214,48,49,.75);letter-spacing:.08em;">莫比乌斯之环</span><span style="color:var(--w12);">·</span>
          <span style="font-family:var(--B);font-size:clamp(.42rem,.62vw,.54rem);color:rgba(214,48,49,.75);letter-spacing:.08em;">骑士勋章</span><span style="color:var(--w12);">·</span>
          <span style="font-family:var(--B);font-size:clamp(.42rem,.62vw,.54rem);color:rgba(214,48,49,.75);letter-spacing:.08em;">幻视立方</span><span style="color:var(--w12);">·</span>
          <span style="font-family:var(--B);font-size:clamp(.42rem,.62vw,.54rem);color:rgba(214,48,49,.75);letter-spacing:.08em;">核心之结</span><span style="color:var(--w12);">·</span>
          <span style="font-family:var(--B);font-size:clamp(.42rem,.62vw,.54rem);color:rgba(214,48,49,.75);letter-spacing:.08em;">轨迹之线</span>
        </div>
      </div>
      <div class="ti a4"><span class="tn">04</span><span class="tt">应用样机 · 徽章对比</span></div>
      <div class="ti a5"><span class="tn">05</span><span class="tt">结语</span></div>
    </div>
  </div>
</div>

<!-- ══ 03 BRIEF ══ -->
<div class="slide" id="s03">
  <div class="two-col">
    <div class="col-l" style="flex:0 0 38%;">
      <div class="ey a1">01 · 品牌背景</div>
      <div class="h2 a2">Brand<br>Brief</div>
      <div class="rule aRU"></div>
      <div class="bt a3" style="max-width:24ch;">这不是一家普通的穿线店。<br>以赛级标准为目标，为认真打球的人服务。</div>
    </div>
    <div class="col-r">
      <div class="bc a2"><div class="bcl">工作室名称</div><div class="bcv">老项网球 · 穿线工作室</div></div>
      <div class="bc a2"><div class="bcl">英文品牌</div><div class="bcv">Racket Service</div></div>
      <div class="bc a3"><div class="bcl">品牌定位</div><div class="bcv">专业赛级穿线工作室 · 面向竞技爱好者与职业选手</div></div>
      <div class="bc a4"><div class="bcl">核心目标</div><div class="bcv">成为认证赛级穿线师，建立专业、精工、可信赖的品牌形象</div></div>
      <div class="bc a5"><div class="bcl">设计关键词</div><div class="bcv">精准 · 专注 · 匠人 · X</div></div>
      <div class="bc a6"><div class="bcl">灵感参考</div><div class="bcv">X JAPAN 美学 · 弦面交叉结构 · 竞技视觉语言</div></div>
    </div>
  </div>
</div>

<!-- ══ 04 CONCEPT ══ -->
<div class="slide" id="s04">
  <div class="two-col">
    <div class="col-l" style="flex:0 0 36%;">
      <div class="ey a1">02 · 设计理念</div>
      <div class="h2 a2">Why<br>X ?</div>
      <div class="rule aRU"></div>
      <div class="bt a3" style="max-width:22ch;">X 不只是字母，它是这个品牌全部语义的交汇点。</div>
    </div>
    <div class="col-r">
      <div class="cp a2"><div class="cn">1</div><div class="cb"><div class="ct">弦面交叉 · 核心工艺</div><div class="cd">网球拍弦面横竖线交叉天然构成 X 骨架，X 本身即穿线工艺的视觉还原。</div></div></div>
      <div class="cp a3"><div class="cn">2</div><div class="cb"><div class="ct">穿线动作 · 工艺叙事</div><div class="cd">穿线时线在拍框内交叉穿越，X 既是动作本身，也是匠人手艺的符号化表达。</div></div></div>
      <div class="cp a4"><div class="cn">3</div><div class="cb"><div class="ct">X JAPAN 精神 · 极致美学</div><div class="cd">极致、专注、戏剧性——X 承载粉丝彩蛋，也定义了品牌的气质边界：不普通，有锋芒。</div></div></div>
      <div class="cp a5"><div class="cn">4</div><div class="cb"><div class="ct">老项 · 个人 IP 符号化</div><div class="cd">"项" 字与 X 形成品牌创始人专属符号，让 LOGO 成为可识别的个人标记。</div></div></div>
    </div>
  </div>
</div>

<!-- ══ 05 方案一·莫比乌斯之环 ══ -->
<div class="slide" id="s05">
  <div class="two-col" style="gap:clamp(24px,4vw,56px);">
    <div class="col-l" style="flex:0 0 34%;">
      <div class="ey a1">03 · 方案一</div>
      <div class="h1 a2" style="font-size:clamp(1.7rem,4vw,3.8rem);">莫比乌斯<br>之环</div>
      <div class="rule aRU"></div>
      <div class="ai a3"><div class="alb">设计语言</div><div class="av">弦线自我缠绕交织，形成莫比乌斯环式的无限循环结构。无起点、无终点，暗喻"无限延续的专注"。立体徽章造型致敬匠人精工。</div></div>
      <div class="ai a4"><div class="alb">核心优势</div><div class="av">哲学深度强 · 立体质感突出 · 圆形徽章灵活 · 金银双版适配高端场景</div></div>
      <div class="ai a5"><div class="alb">适用场景</div><div class="av">赛事证书 · VIP 会员卡 · 礼品盒 · 穿线机铭牌</div></div>
      <div class="a6" style="display:flex;gap:5px;flex-wrap:wrap;"><span class="tag">立体编织</span><span class="tag">圆形徽章</span><span class="tag">金/银双版</span></div>
    </div>
    <div class="logo-panel a3"><img src="{img1}" alt="莫比乌斯之环"></div>
  </div>
</div>

<!-- ══ 06 方案二·骑士勋章 ══ -->
<div class="slide" id="s06">
  <div class="two-col" style="gap:clamp(24px,4vw,56px);">
    <div class="col-l" style="flex:0 0 34%;">
      <div class="ey a1">04 · 方案二</div>
      <div class="h1 a2" style="font-size:clamp(1.7rem,4vw,3.8rem);">骑士<br>勋章</div>
      <div class="rule aRU"></div>
      <div class="ai a3"><div class="alb">设计语言</div><div class="av">几何方框包裹 X 字形，四角延伸如盾徽纹章。圆形格式赋予官方权威感，黑白反色均完整成立，实用性极强。</div></div>
      <div class="ai a4"><div class="alb">核心优势</div><div class="av">正式权威感最强 · 盾徽纹章赋予荣誉感 · 黑白单色完美适配</div></div>
      <div class="ai a5"><div class="alb">适用场景</div><div class="av">名片 · 服务单抬头 · 社媒头像 · 工作服 · 穿线机铭牌</div></div>
      <div class="a6" style="display:flex;gap:5px;flex-wrap:wrap;"><span class="tag">几何方框</span><span class="tag">盾徽纹章</span><span class="tag">黑白通用</span></div>
    </div>
    <div class="logo-panel a3"><img src="{img2}" alt="骑士勋章"></div>
  </div>
</div>

<!-- ══ 07 方案三·幻视立方 ══ -->
<div class="slide" id="s07">
  <div class="two-col" style="gap:clamp(24px,4vw,56px);">
    <div class="col-l" style="flex:0 0 34%;">
      <div class="ey a1">05 · 方案三</div>
      <div class="h1 a2" style="font-size:clamp(1.7rem,4vw,3.8rem);">幻视<br>立方</div>
      <div class="rule aRU"></div>
      <div class="ai a3"><div class="alb">设计语言</div><div class="av">弦线交叉穿插形成视错觉般的立体 X，"不可能图形"式的空间迷惑感是核心张力。简洁线条蕴含极强视觉冲击。</div></div>
      <div class="ai a4"><div class="alb">核心优势</div><div class="av">立体感与视错觉最强 · 造型辨识度高 · 配色灵活 · 数字端表现极佳</div></div>
      <div class="ai a5"><div class="alb">适用场景</div><div class="av">社媒封面 · 推广物料 · 联名 T 恤 · 贴纸</div></div>
      <div class="a6" style="display:flex;gap:5px;flex-wrap:wrap;"><span class="tag">3D视错觉</span><span class="tag">冲击力强</span><span class="tag">配色灵活</span></div>
    </div>
    <div class="logo-panel a3"><img src="{img3}" alt="幻视立方"></div>
  </div>
</div>

<!-- ══ 08 方案四·核心之结 ══ -->
<div class="slide" id="s08">
  <div class="two-col" style="gap:clamp(24px,4vw,56px);">
    <div class="col-l" style="flex:0 0 34%;">
      <div class="ey a1">06 · 方案四</div>
      <div class="h1 a2" style="font-size:clamp(1.7rem,4vw,3.8rem);">核心<br>之结</div>
      <div class="rule aRU"></div>
      <div class="ai a3"><div class="alb">设计语言</div><div class="av">球拍轮廓与弦线弧形融合成封闭连续的符号，完整圆形构图暗示"闭环的专业体系"。多色变体留足品牌延展空间。</div></div>
      <div class="ai a4"><div class="alb">核心优势</div><div class="av">网球专业性最强 · 圆形构图稳定 · 多色变体灵活 · 识别度最高</div></div>
      <div class="ai a5"><div class="alb">适用场景</div><div class="av">全场景通用 · 社媒头像 · 球拍包挂件 · APP 图标</div></div>
      <div class="a6" style="display:flex;gap:5px;flex-wrap:wrap;"><span class="tag">圆形构图</span><span class="tag">多色方案</span><span class="tag">全场景通用</span></div>
    </div>
    <div class="logo-panel a3"><img src="{img4}" alt="核心之结"></div>
  </div>
</div>

<!-- ══ 09 方案五·轨迹之线 ══ -->
<div class="slide" id="s09">
  <div class="two-col" style="gap:clamp(24px,4vw,56px);">
    <div class="col-l" style="flex:0 0 34%;">
      <div class="ey a1">07 · 方案五</div>
      <div class="h1 a2" style="font-size:clamp(1.7rem,4vw,3.8rem);">轨迹<br>之线</div>
      <div class="rule aRU"></div>
      <div class="ai a3"><div class="alb">设计语言</div><div class="av">圆弧动态 X 如击球瞬间球拍的扫击轨迹，线条在空间中划出速度感。"线"既是穿线，也是运动的轨迹，充满动感与个性。</div></div>
      <div class="ai a4"><div class="alb">核心优势</div><div class="av">动感最强 · 造型独特无可复制 · 与赛级专业定位形成有趣反差张力</div></div>
      <div class="ai a5"><div class="alb">适用场景</div><div class="av">品牌故事页 · 穿线日志封面 · 动态 LOGO · 签名款证书</div></div>
      <div class="a6" style="display:flex;gap:5px;flex-wrap:wrap;"><span class="tag">动感速度</span><span class="tag">轨迹叙事</span><span class="tag">个性签名</span></div>
    </div>
    <div class="logo-panel a3"><img src="{img5}" alt="轨迹之线"></div>
  </div>
</div>

<!-- ══ 10 BADGES ══ -->
<div class="slide" id="s10">
  <div class="two-col">
    <div class="col-l" style="flex:0 0 32%;">
      <div class="ey a1">04 · 应用样机</div>
      <div class="h2 a2">五方案<br>徽章对比</div>
      <div class="rule aRU"></div>
      <div class="bt a3" style="max-width:22ch;">相同圆形徽章形态下的五方案对比，直观感受各方向气质差异。</div>
      <div class="bt a4" style="max-width:22ch;margin-top:4px;">徽章可用于：球拍包挂件、帽徽、穿线机铭牌、会员证书压章。</div>
    </div>
    <div class="col-r" style="justify-content:center;">
      <div class="bg-row a2">
        <div class="bi"><div class="bcirc" style="width:clamp(106px,15.5vw,162px);height:clamp(106px,15.5vw,162px);background:#1a1a1a;border:2px solid #333;"><img src="{img1}" style="width:82%;object-fit:contain;" alt=""></div><div class="blbl">方案一</div><div class="bsub">莫比乌斯之环</div></div>
        <div class="bi"><div class="bcirc" style="width:clamp(106px,15.5vw,162px);height:clamp(106px,15.5vw,162px);background:#f0f0f0;border:2px solid #ddd;"><img src="{img2}" style="width:82%;object-fit:contain;" alt=""></div><div class="blbl">方案二</div><div class="bsub">骑士勋章</div></div>
        <div class="bi"><div class="bcirc" style="width:clamp(106px,15.5vw,162px);height:clamp(106px,15.5vw,162px);background:#f5f5f5;border:2px solid #e0e0e0;"><img src="{img3}" style="width:82%;object-fit:contain;" alt=""></div><div class="blbl">方案三</div><div class="bsub">幻视立方</div></div>
      </div>
      <div class="bg-row a3">
        <div class="bi"><div class="bcirc" style="width:clamp(106px,15.5vw,162px);height:clamp(106px,15.5vw,162px);background:#111;border:2px solid var(--red);box-shadow:0 0 0 clamp(4px,.7vw,8px) rgba(214,48,49,.1);"><img src="{img4}" style="width:82%;object-fit:contain;" alt=""></div><div class="blbl">方案四</div><div class="bsub">核心之结</div></div>
        <div class="bi"><div class="bcirc" style="width:clamp(106px,15.5vw,162px);height:clamp(106px,15.5vw,162px);background:#f5f5f5;border:2px solid #e0e0e0;"><img src="{img5}" style="width:82%;object-fit:contain;" alt=""></div><div class="blbl">方案五</div><div class="bsub">轨迹之线</div></div>
      </div>
    </div>
  </div>
</div>

<!-- ══ 11 CLOSING ══ -->
<div class="slide" id="s11">
  <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:clamp(14px,2.8vh,32px);padding:clamp(36px,6vw,90px);">
    <div style="position:absolute;width:62vmin;height:62vmin;opacity:.03;pointer-events:none;">
      <div style="position:absolute;width:100%;height:8%;background:#fff;top:50%;left:0;transform:rotate(45deg);transform-origin:center;margin-top:-4%;"></div>
      <div style="position:absolute;width:100%;height:8%;background:#fff;top:50%;left:0;transform:rotate(-45deg);transform-origin:center;margin-top:-4%;"></div>
    </div>
    <div class="cx aSC" style="width:clamp(55px,9vw,90px);height:clamp(55px,9vw,90px);"></div>
    <div class="ey a1" style="letter-spacing:.35em;">老项网球 · Racket Service</div>
    <div class="h1 a2" style="font-size:clamp(1.5rem,3.8vw,3.6rem);">精工穿线<br>赛级标准</div>
    <div class="rule aRU" style="margin:0 auto;"></div>
    <div class="bt a3" style="max-width:34ch;">每一张拍面，都是一次承诺</div>
    <div class="a4" style="display:flex;gap:9px;flex-wrap:wrap;justify-content:center;">
      <span class="tag">X · 交叉</span><span class="tag">X · 精准</span><span class="tag">X · 极致</span>
    </div>
  </div>
</div>

</div><!-- /deck -->

<div class="chrome">
  <div class="chr-top">
    <div class="slide-num" id="snum">01 / 11</div>
    <div class="dots" id="dots"></div>
  </div>
  <div class="chr-bot">
    <div class="bmark">老项网球 · RACKET SERVICE</div>
    <div class="arrows">
      <button class="arr" onclick="nav(-1)">←</button>
      <button class="arr" onclick="nav(1)">→</button>
    </div>
  </div>
</div>

<script>
const slides=document.querySelectorAll('.slide'),total=slides.length;
let cur=0;
const dotsEl=document.getElementById('dots');
slides.forEach((_,i)=>{{
  const d=document.createElement('div');
  d.className='dot'+(i===0?' active':'');
  d.addEventListener('click',()=>go(i));
  dotsEl.appendChild(d);
}});
function go(n){{
  slides[cur].classList.remove('active');dotsEl.children[cur].classList.remove('active');
  cur=(n+total)%total;
  slides[cur].classList.add('active');dotsEl.children[cur].classList.add('active');
  document.getElementById('snum').textContent=String(cur+1).padStart(2,'0')+' / '+String(total).padStart(2,'0');
}}
function nav(d){{go(cur+d);}}
document.addEventListener('keydown',e=>{{
  if(e.key==='ArrowRight'||e.key==='ArrowDown'||e.key===' ')nav(1);
  if(e.key==='ArrowLeft'||e.key==='ArrowUp')nav(-1);
}});
let tx=0;
document.addEventListener('touchstart',e=>{{tx=e.touches[0].clientX;}},{{passive:true}});
document.addEventListener('touchend',e=>{{const dx=e.changedTouches[0].clientX-tx;if(Math.abs(dx)>40)nav(dx<0?1:-1);}},{{passive:true}});
</script>
</body>
</html>"""

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(HTML)
print(f"Done → {OUT}")
print(f"Size: {os.path.getsize(OUT)/1024/1024:.1f} MB")
