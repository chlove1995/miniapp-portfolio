# -*- coding: utf-8 -*-
"""Generate an A4 PDF portfolio and a WeChat-ready long PNG from the same case data."""
import os, math
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import Color, HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

SRC = r"C:\Users\Windows10\Desktop\ma"
DESKTOP = r"C:\Users\Windows10\Desktop"
OUT = r"C:\Users\Windows10\WorkBuddy\2026-11-25-17-14-14"
PDF = os.path.join(OUT, "miniapp-portfolio.pdf")
PDF_TMP = os.path.join(OUT, "_portfolio-building.pdf")
PDF_FALLBACK = os.path.join(OUT, "miniapp-portfolio-13.pdf")
PNG = os.path.join(OUT, "miniapp-cases-long.png")

FILES = ["0 (1).jpg", "0 (2).jpg", "0 (3).jpg", "0 (4).jpg",
         "0 (5).jpg", "0 (6).jpg", "0 (7).jpg", "0 (8).jpg",
         "0 (9).jpg", "0.jpg", "gh_4031f3ca5277_258.jpg"]
PATHS = [os.path.join(SRC, f) for f in FILES]
PATHS += [os.path.join(DESKTOP, "4e83fa24fee28cd2d9c95a9bb7b28021.jpg"),
          os.path.join(DESKTOP, "31deadf64b32da853ff096e0a97968cd.jpg")]

CASES = [
    ("橙黄票券标识", "码面为几何品牌标识", "卡券 / 品牌"),
    ("酸匠", "SUAN JIANG", "食品 / 餐饮"),
    ("粉色人形标识", "抽象人形品牌标识", "社交 / 会员"),
    ("铭硕母婴", "MISOU · INFANT & MOM", "母婴 / 零售"),
    ("BEAUTY SEEDS", "黑色圆形品牌标识", "美业 / 品牌"),
    ("家庭保洁体验页", "首次体验保洁 · ¥165", "家政 / 生活服务"),
    ("Camping Tomorrow", "露营帐篷与山野主题", "户外 / 露营"),
    ("FONE HOTEL", "英文标识部分被码点遮挡", "酒店 / 住宿"),
    ("蜜蜂卡通 IP", "蜜蜂与蜗牛壳卡通形象", "亲子 / 儿童"),
    ("鑫选易购", "橙色圆形 + 蓝色 U 形标识", "电商 / 购物"),
    ("紫底闪电标识", "紫色圆角方 + 云朵闪电", "工具 / 服务"),
    ("粉色小鱼标识", "粉色圆环与小鱼图形", "餐饮 / 生鲜"),
    ("绿色山形标识", "绿色渐变圆与线条图形", "文旅 / 品牌"),
]

INK = "#1a1a1a"; PAPER = "#f7f5f2"; PINK = "#ff4785"; PURPLE = "#a259ff"; GREEN = "#07c160"

# ---------------- fonts ----------------
def load_fonts():
    regular = bold = None
    for p in [r"C:\Windows\Fonts\msyh.ttc", r"C:\Windows\Fonts\simhei.ttf"]:
        try:
            regular = p; break
        except Exception: pass
    for p in [r"C:\Windows\Fonts\msyhbd.ttc", r"C:\Windows\Fonts\simhei.ttf", r"C:\Windows\Fonts\msyh.ttc"]:
        if os.path.exists(p): bold = p; break
    return regular, bold

FR, FB = load_fonts()
def pf(size, bold=False):
    return ImageFont.truetype(FB if bold else FR, size, index=0)

try:
    pdfmetrics.registerFont(TTFont("CN", r"C:\Windows\Fonts\msyh.ttc", subfontIndex=0))
except Exception:
    pdfmetrics.registerFont(TTFont("CN", r"C:\Windows\Fonts\simhei.ttf"))
try:
    pdfmetrics.registerFont(TTFont("CNB", r"C:\Windows\Fonts\msyhbd.ttc", subfontIndex=0))
except Exception:
    pdfmetrics.registerFont(TTFont("CNB", r"C:\Windows\Fonts\simhei.ttf"))

# ==================== A4 PDF ====================
W, H = A4
c = canvas.Canvas(PDF_TMP, pagesize=A4)
c.setTitle("微信小程序 · 案例作品集")
c.setAuthor("Mini Program Portfolio")

def rect(x, y, w, h, color, r=0, alpha=1.0):
    c.saveState(); c.setFillAlpha(alpha); c.setFillColor(HexColor(color))
    if r: c.roundRect(x, y, w, h, r, stroke=0, fill=1)
    else: c.rect(x, y, w, h, stroke=0, fill=1)
    c.restoreState()

def text(s, x, y, size, color, bold=False, align="left"):
    c.saveState(); c.setFillColor(HexColor(color)); c.setFont("CNB" if bold else "CN", size)
    if align == "center": c.drawCentredString(x, y, s)
    elif align == "right": c.drawRightString(x, y, s)
    else: c.drawString(x, y, s)
    c.restoreState()

def glow(cx, cy, radius, color, layers=26):
    c.saveState()
    for i in range(layers, 0, -1):
        c.setFillColor(HexColor(color)); c.setFillAlpha(0.012 + (layers-i)*0.0004)
        c.circle(cx, cy, radius*i/layers, stroke=0, fill=1)
    c.restoreState()

def dot_ring(cx, cy, r0, n=64):
    c.saveState()
    for layer, (cnt, rad, al) in enumerate([(34, r0, .55), (44, r0+34, .38), (54, r0+66, .24)]):
        for i in range(cnt):
            a = 2*math.pi*i/cnt + layer*0.12
            x = cx + math.cos(a)*rad; y = cy + math.sin(a)*rad
            c.saveState(); c.translate(x, y); c.rotate(math.degrees(a)-90)
            c.setFillColor(Color(1,1,1,alpha=al)); c.setFillAlpha(al)
            c.rect(-0.9, -4.5, 1.8, 9, stroke=0, fill=1); c.restoreState()
    c.restoreState()

# ---- P1 cover ----
rect(0, 0, W, H, INK)
glow(W-70, H-90, 300, PINK)
glow(90, 90, 260, PURPLE)
dot_ring(W-150, H-310, 92)
c.saveState(); c.setFillColor(HexColor(PURPLE)); c.circle(W-150, H-310, 74, stroke=0, fill=1); c.restoreState()
text("13", W-150, H-330, 40, "#ffffff", True, "center")
text("CASES", W-150, H-352, 9, "#ffffff", False, "center")

text("WECHAT MINI PROGRAM  /  PORTFOLIO", 46, H-70, 9, "#ff9abb", True)
text("每一个码，", 44, H-140, 38, "#ffffff", True)
c.saveState(); c.setFillColor(HexColor(PINK)); c.setFont("CNB", 38); c.drawString(44, H-188, "都是一次交付"); c.restoreState()
text("已开发的微信小程序案例作品集", 46, H-232, 12, "#c6c1ba")
text("13 个小程序码，用微信「扫一扫」或长按识别，", 46, H-256, 12, "#c6c1ba")
text("即可直接打开体验每一个项目。", 46, H-276, 12, "#c6c1ba")

for i, (big, small) in enumerate([("13", "案例项目"), ("01", "扫码直达"), ("N", "业务场景")]):
    x = 46 + i*150
    text(big, x, H-350, 27, "#ffffff", True)
    text(small, x, H-368, 9, "#938d85")
c.saveState(); c.setStrokeColor(HexColor("#3a3531")); c.line(46, H-392, W-46, H-392); c.restoreState()
text("下面每一个码，都是一扇可以直接推开的门。", 46, H-420, 12, "#b9b3ab")
text("SELECTED WORKS  ·  2026", 46, 52, 9, "#6f6a64")
text("01 / 04", W-46, 52, 9, "#6f6a64", False, "right")
c.showPage()

# ---- P2 & P3 case pages ----
def case_page(items, page_no, title="案例一览 · 扫码即看"):
    rect(0, 0, W, H, PAPER)
    text("SELECTED WORKS  /  0"+str(page_no-1), 40, H-46, 8, PURPLE, True)
    text(title, 40, H-76, 20, INK, True)
    text("点击不了没关系 —— 拿手机扫一下就好", W-40, H-74, 9, "#8b857c", False, "right")
    c.saveState(); c.setStrokeColor(HexColor("#e0dbd3")); c.line(40, H-88, W-40, H-88); c.restoreState()

    cw, ch, gx, gy = 165, 292, 10, 14
    x0, y0 = 40, H-108-ch
    for k, (idx, (name, sub, tag)) in enumerate(items):
        col, row = k % 3, k // 3
        x = x0 + col*(cw+gx); y = y0 - row*(ch+gy)
        rect(x, y, cw, ch, "#ffffff", 10)
        c.saveState(); c.setStrokeColor(HexColor("#e8e3dc")); c.roundRect(x, y, cw, ch, 10, stroke=1, fill=0); c.restoreState()
        s = 160
        c.drawImage(PATHS[idx], x+(cw-s)/2, y+ch-s-14, s, s, mask=None)
        text("CASE "+str(idx+1).zfill(2), x+12, y+ch-s-29.5, 7.5, "#b0a99f", True)
        tw = c.stringWidth(tag, "CN", 7) + 12
        rect(x+cw-8-tw, y+ch-s-33, tw, 14, "#f4efff", 7)
        text(tag, x+cw-14, y+ch-s-29.5, 7, "#7b46c9", False, "right")
        text(name, x+12, y+70, 12, INK, True)
        text(sub, x+12, y+52, 7.5, "#a09a91")
        c.saveState(); c.setStrokeColor(HexColor("#ece7df")); c.setDash(2, 3)
        c.line(x+12, y+42, x+cw-12, y+42); c.restoreState()
        c.saveState(); c.setFillColor(HexColor(GREEN)); c.circle(x+16, y+28, 2.6, stroke=0, fill=1); c.restoreState()
        text("微信扫码，直接体验", x+24, y+24.5, 7.5, "#3d3833")
    if len(items) < 6:
        k = len(items); col, row = k % 3, k // 3
        x = x0 + col*(cw+gx); y = y0 - row*(ch+gy)
        rect(x, y, cw, ch, INK, 10)
        text("NEXT", x+14, y+ch-34, 8, "#ff9abb", True)
        text("下一个案例", x+14, y+ch-78, 14, "#ffffff", True)
        text("可能是你的", x+14, y+ch-98, 14, PINK, True)
        text("聊聊业务场景与功能范围，", x+14, y+ch-140, 8, "#aaa49c")
        text("一起把想法做成小程序。", x+14, y+ch-155, 8, "#aaa49c")
        text("欢迎沟通 →", x+14, y+30, 9, "#ff9abb", True)
    text("* 案例名称依据小程序码可辨识信息整理，行业标签为按码面视觉所做的场景归类，具体以实际项目为准。", 40, 44, 7, "#a29b91")
    text("案例图片与小程序码版权归各品牌方所有，仅作项目展示用途。", 40, 33, 7, "#a29b91")
    text("0"+str(page_no)+" / 04", W-40, 33, 8, "#a29b91", False, "right")
    c.showPage()

case_page(list(enumerate(CASES[:6])), 2)
case_page(list(enumerate(CASES[6:12], start=6)), 3, "案例一览 · 续")

# ---- P4: final case + delivery chain + CTA ----
rect(0, 0, W, H, PAPER)
text("FINAL CASE  /  03", 40, H-46, 8, PURPLE, True)
text("第 13 个，留给下一个", 40, H-76, 20, INK, True)
c.saveState(); c.setStrokeColor(HexColor("#e0dbd3")); c.line(40, H-88, W-40, H-88); c.restoreState()

# big case card
rect(40, 340, 250, 390, "#ffffff", 12)
c.saveState(); c.setStrokeColor(HexColor("#e8e3dc")); c.roundRect(40, 340, 250, 390, 12, stroke=1, fill=0); c.restoreState()
c.drawImage(PATHS[12], 60, 470, 220, 220, mask=None)
name13, sub13, tag13 = CASES[12]
text("CASE 13", 60, 450, 8, "#b0a99f", True)
tw = c.stringWidth(tag13, "CN", 8) + 14
rect(290-8-tw, 446, tw, 16, "#f4efff", 8)
text(tag13, 282, 450, 8, "#7b46c9", False, "right")
text(name13, 60, 422, 15, INK, True)
text(sub13, 60, 402, 8.5, "#a09a91")
c.saveState(); c.setStrokeColor(HexColor("#ece7df")); c.setDash(2, 3)
c.line(60, 388, 270, 388); c.restoreState()
c.saveState(); c.setFillColor(HexColor(GREEN)); c.circle(64, 368, 2.8, stroke=0, fill=1); c.restoreState()
text("微信扫码，直接体验", 74, 364.5, 8.5, "#3d3833")

# right column: delivery chain
text("13 个案例，一条完整链路", 310, 700, 14, INK, True)
text("从需求梳理到提审上线，按模块把事情拆清楚。", 310, 678, 8.5, "#8b857c")
text("以下为通用交付链路说明，可按实际项目范围调整。", 310, 662, 8.5, "#8b857c")
CAPS = [("01", "需求梳理"), ("02", "界面设计"), ("03", "前端开发"),
        ("04", "云开发 / 后端"), ("05", "交易与营销"), ("06", "上线与迭代")]
for k, (ci, nm) in enumerate(CAPS):
    col, row = k % 2, k // 2
    x = 310 + col*127; y = 564 - row*85
    rect(x, y, 118, 76, "#ffffff", 8)
    c.saveState(); c.setStrokeColor(HexColor("#e8e3dc")); c.roundRect(x, y, 118, 76, 8, stroke=1, fill=0); c.restoreState()
    text(ci + " /", x+12, y+52, 8, PURPLE, True)
    text(nm, x+12, y+30, 10.5, INK, True)
text("每一个码，都可以直接用微信扫开看效果。", 310, 360, 9, "#8b857c")

rect(40, 110, W-80, 170, INK, 12)
glow(W-60, 280, 150, PINK, 18)
text("想做一个类似的小程序？", 62, 232, 18, "#ffffff", True)
text("把业务场景和大概想法发过来，一起把页面清单、功能范围和上线节奏聊清楚。", 62, 205, 9, "#aaa49c")
text("上面的 13 个码，都可以直接点开看效果。", 62, 188, 9, "#aaa49c")
text("欢迎沟通 →", 62, 148, 11, "#ff9abb", True)
text("© 2026 微信小程序案例作品集", 40, 44, 7.5, "#a29b91")
text("04 / 04", W-40, 44, 8, "#a29b91", False, "right")
c.showPage()
c.save()
# The preview panel may hold a lock on the previous PDF; fall back to a versioned name.
try:
    os.replace(PDF_TMP, PDF)
    FINAL_PDF = PDF
except OSError:
    os.replace(PDF_TMP, PDF_FALLBACK)
    FINAL_PDF = PDF_FALLBACK
print("PDF OK", FINAL_PDF, os.path.getsize(FINAL_PDF))

# ==================== LONG PNG ====================
PW, PH = 1080, 3400
img = Image.new("RGB", (PW, PH), PAPER)
d = ImageDraw.Draw(img)

# header background
d.rectangle((0, 0, PW, 560), fill=INK)
# soft glows + radiate dot ring, drawn once on a single overlay
ov = Image.new("RGBA", (PW, 560), (0, 0, 0, 0))
od = ImageDraw.Draw(ov)
gx, gy = 880, 60
for i in range(60, 0, -1):
    a = int(3 + (60-i)*0.35)
    od.ellipse((gx-i*5, gy-i*5, gx+i*5, gy+i*5), fill=(255, 71, 133, a))
cx, cy, rr = 860, 300, 175
for layer, (cnt, rad) in enumerate([(38, rr), (50, rr+52), (62, rr+100)]):
    for i in range(cnt):
        a = 2*math.pi*i/cnt + layer*0.1
        x = cx + math.cos(a)*rad; y = cy + math.sin(a)*rad
        ln = 12 + (i%3)*6
        od.line((x, y, x+math.cos(a)*ln, y+math.sin(a)*ln),
                fill=(255, 255, 255, int(90 + (i%4)*35)), width=4)
header = Image.alpha_composite(img.crop((0, 0, PW, 560)).convert("RGBA"), ov).convert("RGB")
img.paste(header, (0, 0))
d = ImageDraw.Draw(img)

d.text((56, 62), "WECHAT MINI PROGRAM  /  PORTFOLIO", font=pf(19, True), fill="#ff9abb")
d.text((54, 128), "每一个码，", font=pf(66, True), fill="#ffffff")
d.text((54, 212), "都是一次交付", font=pf(66, True), fill=PINK)
d.text((56, 318), "已开发的微信小程序案例作品集 · 13 个项目", font=pf(25), fill="#c6c1ba")
d.text((56, 358), "用微信「扫一扫」或长按识别，直接打开体验", font=pf(25), fill="#c6c1ba")
for i, (big, small) in enumerate([("13", "案例项目"), ("01", "扫码直达"), ("N", "业务场景")]):
    x = 56 + i*180
    d.text((x, 424), big, font=pf(46, True), fill="#ffffff")
    d.text((x+4, 484), small, font=pf(18), fill="#938d85")

# center badge on ring
d.ellipse((cx-96, cy-96, cx+96, cy+96), fill=PURPLE)
d.text((cx, cy-52), "13", font=pf(72, True), fill="#ffffff", anchor="mt")
d.text((cx, cy+34), "CASES", font=pf(20), fill="#ffffff", anchor="mt")

# section title
d.text((56, 596), "SELECTED WORKS  /  01", font=pf(18, True), fill=PURPLE)
d.text((54, 626), "案例一览 · 扫码即看", font=pf(40, True), fill=INK)

# cards: 13 cases + scan guide + next-project CTA = 15 cells (3 x 5)
CW, CH, GX, GY = 320, 442, 20, 20
X0, Y0 = 40, 700
for k in range(15):
    col, row = k % 3, k // 3
    x = X0 + col*(CW+GX); y = Y0 + row*(CH+GY)
    if k == 13:
        d.rounded_rectangle((x, y, x+CW, y+CH), radius=22, fill="#ffffff", outline="#e8e3dc", width=2)
        d.text((x+24, y+38), "HOW TO SCAN", font=pf(18, True), fill=PURPLE)
        d.text((x+24, y+76), "怎么扫码", font=pf(34, True), fill=INK)
        d.text((x+24, y+128), "13 个码，手机就能打开", font=pf(19), fill="#a09a91")
        steps = ["微信「扫一扫」直接扫", "保存图片，微信内长按识别", "点开原图，识别更稳"]
        for i, t in enumerate(steps):
            yy = y+188+i*66
            d.rounded_rectangle((x+24, yy, x+52, yy+28), radius=14, fill="#f4efff")
            d.text((x+38, yy+14), str(i+1), font=pf(17, True), fill="#7b46c9", anchor="mm")
            d.text((x+64, yy+3), t, font=pf(18), fill=INK)
        d.line((x+24, y+404, x+CW-24, y+404), fill="#ece7df", width=2)
        d.text((x+24, y+416), "建议发送原图，别压缩", font=pf(17), fill="#a09a91")
        continue
    if k == 14:
        d.rounded_rectangle((x, y, x+CW, y+CH), radius=22, fill=INK)
        d.ellipse((x+CW-110, y+CH-110, x+CW-30, y+CH-30), fill="#2b2136")
        d.text((x+26, y+56), "NEXT PROJECT", font=pf(18, True), fill="#ff9abb")
        d.text((x+26, y+142), "下一个案例", font=pf(32, True), fill="#ffffff")
        d.text((x+26, y+190), "可能是你的", font=pf(32, True), fill=PINK)
        d.text((x+26, y+268), "聊聊业务场景与功能范围", font=pf(19), fill="#aaa49c")
        d.text((x+26, y+300), "一起把想法做成小程序", font=pf(19), fill="#aaa49c")
        d.rounded_rectangle((x+26, y+364, x+176, y+412), radius=24, fill=PINK)
        d.text((x+101, y+388), "欢迎沟通", font=pf(19, True), fill="#ffffff", anchor="mm")
        continue
    name, sub, tag = CASES[k]
    d.rounded_rectangle((x, y, x+CW, y+CH), radius=22, fill="#ffffff", outline="#e8e3dc", width=2)
    im = Image.open(PATHS[k]).convert("RGB").resize((284, 284), Image.LANCZOS)
    img.paste(im, (x+18, y+16))
    d.text((x+20, y+312), "CASE "+str(k+1).zfill(2), font=pf(17, True), fill="#b0a99f")
    # tag pill
    tw = int(d.textlength(tag, font=pf(17))) + 22
    d.rounded_rectangle((x+CW-20-tw, y+308, x+CW-20, y+342), radius=17, fill="#f4efff")
    d.text((x+CW-20-tw/2, y+325), tag, font=pf(17), fill="#7b46c9", anchor="mm")
    d.text((x+20, y+350), name, font=pf(27, True), fill=INK)
    d.text((x+20, y+387), sub, font=pf(17), fill="#a09a91")
    d.line((x+20, y+414, x+CW-20, y+414), fill="#ece7df", width=2)
    d.ellipse((x+22, y+425, x+32, y+435), fill=GREEN)
    d.text((x+42, y+420), "微信扫码，直接体验", font=pf(17), fill="#3d3833")

# footer
fy = Y0 + 5*(CH+GY) + 8
d.rectangle((0, fy, PW, PH), fill=INK)
d.text((56, fy+52), "想做一个类似的小程序？", font=pf(42, True), fill="#ffffff")
d.text((56, fy+118), "把业务场景和大概想法发过来，一起把页面清单、功能范围和上线节奏聊清楚。", font=pf(22), fill="#aaa49c")
d.text((56, fy+158), "案例名称依据小程序码可辨识信息整理 · 行业标签为视觉归类 · 图片版权归各品牌方所有", font=pf(17), fill="#6f6a64")
d.line((56, fy+216, PW-56, fy+216), fill="#33302d", width=2)
d.text((56, fy+244), "微信「扫一扫」或长按识别 · 13 个案例，扫码即达", font=pf(20), fill="#8b857c")
d.text((56, PH-52), "© 2026 微信小程序案例作品集", font=pf(17), fill="#6f6a64")

img.save(PNG, quality=94)
print("PNG OK", img.size, os.path.getsize(PNG))
