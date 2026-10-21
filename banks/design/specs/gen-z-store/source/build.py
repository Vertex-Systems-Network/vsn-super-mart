"""Builds afterhours.html — VSN Super Mart / Afterhours preset screens.
Image placeholders get a unique background color (#1E1E<NN>) so they can be found in Figma and filled by Figma AI.
"""
import json, os
OUT = os.path.join(os.path.dirname(__file__), "afterhours.html")
SLOTS = {}  # color -> slot
_n = [0x20]
def ph(slot, cls="", style=""):
    c = f"#1E1E{_n[0]:02X}"; _n[0] += 1
    SLOTS[c] = slot
    return f'<div class="ph {cls}" style="background:{c};{style}"></div>'

ICON = {
 "menu": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#F4F4F0" stroke-width="1.8"><path d="M3 7h18M3 12h18M3 17h12"/></svg>',
 "search": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#F4F4F0" stroke-width="1.8"><circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/></svg>',
 "user": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#F4F4F0" stroke-width="1.8"><circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/></svg>',
 "bag": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#F4F4F0" stroke-width="1.8"><path d="M5 8h14l-1 13H6L5 8Z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/></svg>',
 "arrow": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 "play": '<svg width="18" height="18" viewBox="0 0 24 24" fill="#0B0B0F"><path d="M7 4v16l13-8z"/></svg>',
 "close": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#F4F4F0" stroke-width="1.8"><path d="M6 6l12 12M18 6 6 18"/></svg>',
 "chev": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#F4F4F0" stroke-width="2"><path d="m6 9 6 6 6-6"/></svg>',
 "globe": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#9A9AA3" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/></svg>',
 "ruler": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#C6FF3D" stroke-width="1.8"><rect x="2" y="8" width="20" height="8"/><path d="M6 8v3M10 8v4M14 8v3M18 8v4"/></svg>',
}

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{background:#05050A;font-family:Inter,sans-serif;color:#F4F4F0;padding:80px;display:flex;flex-direction:column;gap:120px;align-items:flex-start}
.screen{background:#0B0B0F;overflow:hidden;position:relative;flex-shrink:0}
.d{width:1440px}.m{width:390px}
.disp{font-family:Oswald,sans-serif;text-transform:uppercase;font-weight:700;letter-spacing:-0.01em;line-height:.92}
.lbl{font-size:12px;letter-spacing:.14em;text-transform:uppercase;font-weight:600}
.muted{color:#9A9AA3}.acid{color:#C6FF3D}
.ph{position:relative;width:100%}
.btn{white-space:nowrap;flex-shrink:0;display:inline-flex;align-items:center;gap:10px;height:52px;padding:0 28px;background:#C6FF3D;color:#0B0B0F;font-weight:700;font-size:14px;letter-spacing:.08em;text-transform:uppercase}
.btn.ghost{background:transparent;color:#F4F4F0;border:1.5px solid #F4F4F0}
.btn.dark{background:#0B0B0F;color:#C6FF3D}
.ticker{height:36px;background:#C6FF3D;color:#0B0B0F;display:flex;align-items:center;gap:40px;white-space:nowrap;overflow:hidden;font-family:Oswald,sans-serif;font-weight:600;font-size:14px;letter-spacing:.12em;text-transform:uppercase;padding-left:24px}
.hdr{height:72px;display:flex;align-items:center;justify-content:space-between;padding:0 32px;border-bottom:1px solid #2A2A33;background:#0B0B0F}
.hdr .l,.hdr .r{display:flex;gap:22px;align-items:center;width:240px}.hdr .r{justify-content:flex-end}
.logo{font-family:Oswald,sans-serif;font-weight:700;font-size:26px;letter-spacing:.06em}
.logo b{color:#C6FF3D}
.count{background:#C6FF3D;color:#0B0B0F;font-size:11px;font-weight:700;width:18px;height:18px;display:flex;align-items:center;justify-content:center;margin-left:-14px;margin-top:-14px}
.sec{padding:96px 32px}
.row{display:flex;gap:16px}
.card{flex:1;position:relative;background:#16161D}
.card .ph{aspect-ratio:4/5}
.card .meta{position:absolute;left:0;right:0;bottom:0;padding:16px;background:linear-gradient(transparent,rgba(11,11,15,.92));display:flex;justify-content:space-between;align-items:flex-end}
.card .nm{font-family:Oswald,sans-serif;font-size:20px;font-weight:600;text-transform:uppercase;line-height:1}
.card .pr{font-size:14px;font-weight:600;margin-top:6px}
.card .sizes{display:flex;gap:4px;margin-top:8px}
.card .sizes span{font-size:11px;border:1px solid #3A3A44;padding:2px 5px;color:#C9C9D0}
.card .sizes span.x{color:#55555E;text-decoration:line-through}
.badge{position:absolute;top:12px;left:12px;font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;padding:5px 8px;background:#C6FF3D;color:#0B0B0F}
.badge.so{background:#F4F4F0}.badge.cs{background:#0B0B0F;color:#C6FF3D;border:1px solid #C6FF3D}
.sechead{display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:32px}
.chip{border:1px solid #3A3A44;height:40px;padding:0 16px;display:flex;align-items:center;gap:8px;font-size:13px;font-weight:600}
.chip.on{background:#F4F4F0;color:#0B0B0F;border-color:#F4F4F0}
.sz{width:64px;height:52px;border:1.5px solid #3A3A44;display:flex;align-items:center;justify-content:center;font-weight:600;font-size:14px}
.sz.on{border-color:#C6FF3D;color:#C6FF3D}.sz.x{color:#55555E;text-decoration:line-through}
.acc{border-top:1px solid #2A2A33;padding:20px 0;display:flex;justify-content:space-between;font-weight:600;font-size:14px;letter-spacing:.06em;text-transform:uppercase}
.input{height:52px;border:1.5px solid #3A3A44;flex:1;display:flex;align-items:center;padding:0 18px;color:#9A9AA3;font-size:14px}
.foot{padding:72px 32px 32px;border-top:1px solid #2A2A33;background:#0B0B0F}
.pay{display:flex;gap:8px}.pay span{width:44px;height:28px;background:#F4F4F0;color:#0B0B0F;font-size:9px;font-weight:800;display:flex;align-items:center;justify-content:center}
"""

def header(cart=2):
    return f'''<div class="ticker"><span>Drop 07 "Night Shift" — Fri 24 Oct, 18:00 CET</span><span>✦</span><span>Free shipping over €150</span><span>✦</span><span>Early access for members</span><span>✦</span><span>Drop 07 "Night Shift" — Fri 24 Oct, 18:00 CET</span><span>✦</span><span>Free shipping over €150</span></div>
<div class="hdr"><div class="l">{ICON["menu"]}<span class="lbl">Menu</span>{ICON["search"]}</div><div class="logo">AFTER<b>/</b>HOURS</div><div class="r"><span class="lbl muted" style="display:flex;gap:6px;align-items:center">{ICON["globe"]} EN · EUR</span>{ICON["user"]}{ICON["bag"]}<span class="count">{cart}</span></div></div>'''

def card(slot, name, price, badge=None, sizes=("S","M","L","XL"), xs=()):
    b = ""
    if badge == "new": b = '<div class="badge">New</div>'
    if badge == "sold": b = '<div class="badge so">Sold out</div>'
    if badge == "soon": b = '<div class="badge cs">Coming soon</div>'
    if badge == "last": b = '<div class="badge">Last sizes</div>'
    sz = "".join(f'<span class="{"x" if s in xs else ""}">{s}</span>' for s in sizes)
    return f'<div class="card">{ph(slot)}{b}<div class="meta"><div><div class="nm">{name}</div><div class="pr">{price}</div><div class="sizes">{sz}</div></div></div></div>'

def footer():
    cols = [("Shop", ["New drop", "Tops", "Bottoms", "Accessories", "Archive"]), ("Help", ["Shipping", "Returns", "Size guide", "Track order", "Contact"]), ("Brand", ["About", "Journal", "Stockists", "Careers"])]
    c = "".join(f'<div><div class="lbl muted" style="margin-bottom:18px">{t}</div>' + "".join(f'<div style="font-size:15px;margin-bottom:12px">{i}</div>' for i in items) + "</div>" for t, items in cols)
    return f'''<div class="foot"><div style="display:flex;justify-content:space-between;gap:64px">
<div style="width:460px"><div class="disp" style="font-size:44px">Stay up after hours</div><p class="muted" style="margin:14px 0 22px;font-size:15px;line-height:1.5">Join the list for early access to every drop.</p><div style="display:flex"><div class="input">Email address</div><div class="btn">Sign up</div></div></div>
<div style="display:flex;gap:96px">{c}</div></div>
<div style="display:flex;justify-content:space-between;align-items:center;margin-top:72px;padding-top:24px;border-top:1px solid #2A2A33"><div class="lbl muted">© 2026 After/Hours · Privacy · Terms</div><div style="display:flex;gap:16px;align-items:center"><span class="lbl muted" style="display:flex;gap:6px;align-items:center">{ICON["globe"]} Germany (EUR €)</span><div class="pay"><span>VISA</span><span>MC</span><span>AMEX</span><span>PAY</span><span>KLARNA</span></div></div></div></div>'''

# ---------------- HOME desktop ----------------
home = f'''<div class="screen d" id="home-desktop">{header()}
<div style="position:relative;height:820px">{ph("home-hero", style="position:absolute;inset:0;height:820px")}
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(11,11,15,.1),rgba(11,11,15,.85))"></div>
<div style="position:absolute;left:32px;right:32px;bottom:56px;display:flex;justify-content:space-between;align-items:flex-end">
<div><div class="lbl acid" style="margin-bottom:20px">Drop 07 — out now</div><div class="disp" style="font-size:168px">Night<br>Shift</div></div>
<div style="width:380px"><p style="font-size:17px;line-height:1.5;color:#D9D9DE;margin-bottom:28px">Heavyweight layers built for 3am city light. 14 pieces, no restocks.</p><div class="row"><div class="btn">Shop the drop {ICON["arrow"]}</div><div class="btn ghost">{ICON["play"].replace("#0B0B0F","#F4F4F0")} Watch film</div></div></div></div></div>
<div class="sec" style="padding-bottom:48px"><div class="sechead"><div><div class="lbl acid" style="margin-bottom:12px">Live now</div><div class="disp" style="font-size:72px">The drop</div></div><div class="row"><div class="chip on">All 14</div><div class="chip">Tops</div><div class="chip">Bottoms</div><div class="chip">Accessories</div></div></div>
<div class="row">{card("product-hoodie","Shift hoodie","€180","new")}{card("product-cargo","Utility cargo","€210",None,("28","30","32","34"),("28",))}{card("product-jacket","Lime track jacket","€240","last",("S","M","L","XL"),("S","M"))}{card("product-tee","Boxy tee 280g","€75","sold",("S","M","L","XL"),("S","M","L","XL"))}</div></div>
<div class="sec" style="padding-top:48px"><div style="background:#C6FF3D;color:#0B0B0F;display:flex;align-items:stretch">
<div style="flex:1;padding:64px"><div class="lbl" style="margin-bottom:24px">Next drop · members first</div><div class="disp" style="font-size:96px">Drop 08<br>Blackout</div>
<div style="display:flex;gap:48px;margin:36px 0"><div><div class="lbl">Release</div><div class="disp" style="font-size:40px;margin-top:8px">Fri 07 Nov</div></div><div><div class="lbl">Time</div><div class="disp" style="font-size:40px;margin-top:8px">18:00 CET</div></div><div><div class="lbl">Pieces</div><div class="disp" style="font-size:40px;margin-top:8px">09</div></div></div>
<div style="display:flex;max-width:520px"><div class="input" style="border-color:#0B0B0F;color:#3A4A10">Email for early access</div><div class="btn dark">Get access</div></div></div>
<div style="width:560px">{ph("drop-next", style="height:100%;min-height:560px")}</div></div></div>
<div class="sec" style="padding-top:0"><div class="sechead"><div class="disp" style="font-size:72px">Shop by</div></div><div class="row">
<div class="card">{ph("category-tops", style="aspect-ratio:1/1")}<div class="meta"><div class="disp" style="font-size:44px">Tops</div>{ICON["arrow"]}</div></div>
<div class="card">{ph("category-bottoms", style="aspect-ratio:1/1")}<div class="meta"><div class="disp" style="font-size:44px">Bottoms</div>{ICON["arrow"]}</div></div>
<div class="card">{ph("category-accessories", style="aspect-ratio:1/1")}<div class="meta"><div class="disp" style="font-size:44px">Accessories</div>{ICON["arrow"]}</div></div></div></div>
<div style="display:flex;border-top:1px solid #2A2A33;border-bottom:1px solid #2A2A33">
<div style="width:56%;position:relative">{ph("lookbook", style="height:860px")}
<div style="position:absolute;left:38%;top:30%;width:28px;height:28px;border-radius:14px;background:#C6FF3D;border:5px solid rgba(11,11,15,.6)"></div><div style="position:absolute;left:58%;top:62%;width:28px;height:28px;border-radius:14px;background:#C6FF3D;border:5px solid rgba(11,11,15,.6)"></div></div>
<div style="flex:1;padding:96px 64px;display:flex;flex-direction:column;justify-content:space-between"><div><div class="lbl acid" style="margin-bottom:16px">Lookbook</div><div class="disp" style="font-size:88px">Parking<br>level −2</div><p class="muted" style="font-size:16px;line-height:1.6;margin-top:24px;max-width:420px">Shot after midnight in Berlin. Tap the dots to shop every piece in the frame.</p></div>
<div><div style="display:flex;gap:16px;align-items:center;padding:16px 0;border-top:1px solid #2A2A33"><div style="width:72px">{ph("lb-item-1", style="height:90px")}</div><div style="flex:1"><div style="font-weight:600">Nylon puffer</div><div class="muted" style="font-size:14px">€320</div></div><div class="btn ghost" style="height:40px;padding:0 16px;font-size:12px">Add</div></div>
<div style="display:flex;gap:16px;align-items:center;padding:16px 0;border-top:1px solid #2A2A33"><div style="width:72px">{ph("lb-item-2", style="height:90px")}</div><div style="flex:1"><div style="font-weight:600">Utility cargo</div><div class="muted" style="font-size:14px">€210</div></div><div class="btn ghost" style="height:40px;padding:0 16px;font-size:12px">Add</div></div></div></div></div>
<div class="sec"><div class="sechead"><div><div class="lbl acid" style="margin-bottom:12px">Seen on you</div><div class="disp" style="font-size:72px">#AfterHoursFit</div></div><div class="lbl muted">Tag us to get featured</div></div>
<div class="row">{"".join(f'<div class="card">{ph("ugc-"+str(i), style="aspect-ratio:9/16")}<div style="position:absolute;top:14px;right:14px;width:36px;height:36px;border-radius:18px;background:#C6FF3D;display:flex;align-items:center;justify-content:center">{ICON["play"]}</div></div>' for i in range(1,6))}</div></div>
<div style="background:#16161D;border-top:1px solid #2A2A33;border-bottom:1px solid #2A2A33;padding:40px 0;white-space:nowrap;overflow:hidden"><div class="disp" style="font-size:96px;color:#16161D;-webkit-text-stroke:1.5px #C6FF3D">No restocks ✦ Made after dark ✦ No restocks ✦ Made after dark</div></div>
{footer()}</div>'''

# ---------------- COLLECTION desktop ----------------
col_cards = [("product-hoodie","Shift hoodie","€180","new",(),),("product-cargo","Utility cargo","€210",None,("28",)),("product-jacket","Lime track jacket","€240","last",("S","M")),("product-tee","Boxy tee 280g","€75","sold",("S","M","L","XL")),
             ("product-sneaker","Runner 02","€260",None,()),("product-cap","Six-panel cap","€55",None,()),("product-puffer","Nylon puffer","€320","soon",()),("product-hoodie-2","Zip hoodie","€195",None,("XL",))]
def ccard(c):
    slot,n,p,b,xs = c[0],c[1],c[2],c[3],c[4] if len(c)>4 else ()
    return card(slot,n,p,b,("S","M","L","XL"),xs)
grid = "".join(f'<div class="row" style="margin-bottom:16px">{"".join(ccard(c) for c in col_cards[i:i+4])}</div>' for i in (0,4))
collection = f'''<div class="screen d" id="collection-desktop">{header()}
<div style="padding:64px 32px 40px;display:flex;justify-content:space-between;align-items:flex-end;border-bottom:1px solid #2A2A33"><div><div class="lbl muted" style="margin-bottom:16px">Home / Drop 07</div><div class="disp" style="font-size:120px">Night shift</div></div><p class="muted" style="width:420px;font-size:16px;line-height:1.55">14 pieces in washed black and acid lime. Limited runs, no restocks — when a size is gone, it is gone.</p></div>
<div style="display:flex;justify-content:space-between;align-items:center;padding:20px 32px;border-bottom:1px solid #2A2A33"><div class="row" style="gap:8px"><div class="chip">Availability {ICON["chev"]}</div><div class="chip">Size {ICON["chev"]}</div><div class="chip">Color {ICON["chev"]}</div><div class="chip">Price {ICON["chev"]}</div><div class="chip">Product type {ICON["chev"]}</div><div class="chip on">In stock ✕</div></div>
<div style="display:flex;gap:24px;align-items:center"><span class="muted" style="font-size:14px">14 products</span><div class="chip">Sort: Featured {ICON["chev"]}</div><div class="chip">Hide sold out</div></div></div>
<div style="padding:24px 32px">{grid}</div>
<div style="display:flex;justify-content:center;padding:24px 0 96px"><div class="btn ghost">Load more · 8 of 14</div></div>
{footer()}</div>'''

# ---------------- PRODUCT desktop ----------------
product = f'''<div class="screen d" id="product-desktop">{header()}
<div style="display:flex">
<div style="width:880px;display:grid;grid-template-columns:1fr 1fr;gap:4px">{ph("pdp-1", style="grid-column:1/3;aspect-ratio:4/5;height:auto")}{ph("pdp-2", style="aspect-ratio:4/5")}{ph("pdp-3", style="aspect-ratio:4/5")}</div>
<div style="flex:1;padding:48px 48px 48px 56px">
<div class="lbl muted">Home / Drop 07 / Tops</div>
<div style="display:flex;gap:8px;margin:28px 0 18px"><div class="badge" style="position:static">New</div><div class="badge cs" style="position:static">Drop 07</div></div>
<div class="disp" style="font-size:72px">Shift hoodie</div>
<div style="display:flex;align-items:baseline;gap:14px;margin:18px 0 6px"><div style="font-size:26px;font-weight:700">€180</div><div class="muted" style="font-size:13px">Taxes included. Shipping calculated at checkout.</div></div>
<div class="muted" style="font-size:14px;margin-bottom:28px">Pay in 4 interest-free payments of €45 with <b style="color:#F4F4F0">Shop Pay</b></div>
<div class="lbl" style="margin-bottom:12px">Color — Washed black</div>
<div class="row" style="gap:10px;margin-bottom:28px"><div style="width:52px;height:52px;background:#1A1A1F;border:2px solid #C6FF3D"></div><div style="width:52px;height:52px;background:#C6FF3D;border:1.5px solid #3A3A44"></div><div style="width:52px;height:52px;background:#B9B4A8;border:1.5px solid #3A3A44"></div></div>
<div style="display:flex;justify-content:space-between;margin-bottom:12px"><div class="lbl">Size — M</div><div class="lbl acid" style="display:flex;gap:8px;align-items:center">{ICON["ruler"]} Size guide</div></div>
<div class="row" style="gap:8px;margin-bottom:12px"><div class="sz x">XS</div><div class="sz">S</div><div class="sz on">M</div><div class="sz">L</div><div class="sz">XL</div><div class="sz x">XXL</div></div>
<div class="muted" style="font-size:13px;margin-bottom:28px">Model is 186 cm and wears M · Oversized fit, size down for regular</div>
<div class="btn" style="width:100%;justify-content:center;height:60px;font-size:15px">Add to bag — €180</div>
<div style="margin-top:10px;height:56px;background:#5A31F4;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:16px">Buy with Shop Pay</div>
<div class="muted" style="text-align:center;font-size:13px;margin:12px 0 28px;text-decoration:underline">More payment options</div>
<div style="display:flex;gap:12px;align-items:center;padding:16px;background:#16161D;margin-bottom:28px"><div style="width:8px;height:8px;border-radius:4px;background:#C6FF3D"></div><div style="font-size:14px">Pickup available at <b>Berlin Mitte store</b> · usually ready in 2 hours</div></div>
<div class="acc"><span>Details</span><span>+</span></div><div class="acc"><span>Fit and sizing</span><span>+</span></div><div class="acc"><span>Shipping and returns</span><span>+</span></div><div class="acc" style="border-bottom:1px solid #2A2A33"><span>Care</span><span>+</span></div>
</div></div>
<div class="sec"><div class="sechead"><div class="disp" style="font-size:56px">Complete the look</div><div class="lbl muted">From the same drop</div></div><div class="row">{card("product-cargo","Utility cargo","€210")}{card("product-cap","Six-panel cap","€55")}{card("product-sneaker","Runner 02","€260")}{card("product-jacket","Lime track jacket","€240","last",("S","M","L","XL"),("S","M"))}</div></div>
{footer()}</div>'''

# ---------------- CART DRAWER (over collection) ----------------
def line(slot, n, v, p):
    return f'<div style="display:flex;gap:16px;padding:20px 0;border-bottom:1px solid #2A2A33"><div style="width:96px">{ph(slot, style="height:120px")}</div><div style="flex:1;display:flex;flex-direction:column;justify-content:space-between"><div><div style="display:flex;justify-content:space-between"><div style="font-weight:700;font-size:15px;text-transform:uppercase">{n}</div><div style="font-weight:700">{p}</div></div><div class="muted" style="font-size:13px;margin-top:6px">{v}</div></div><div style="display:flex;justify-content:space-between;align-items:center"><div style="display:flex;border:1.5px solid #3A3A44;height:38px;align-items:center"><span style="width:38px;text-align:center">−</span><span style="width:30px;text-align:center;font-weight:600">1</span><span style="width:38px;text-align:center">+</span></div><span class="muted" style="font-size:13px;text-decoration:underline">Remove</span></div></div></div>'
cart = f'''<div class="screen d" id="cart-drawer-desktop" style="height:1000px">{header()}
<div style="position:absolute;inset:108px 0 0 0;background:rgba(5,5,10,.72)"></div>
<div style="position:absolute;top:0;right:0;width:480px;height:1000px;background:#0B0B0F;border-left:1px solid #2A2A33;display:flex;flex-direction:column">
<div style="display:flex;justify-content:space-between;align-items:center;padding:24px 28px;border-bottom:1px solid #2A2A33"><div class="disp" style="font-size:32px">Your bag (2)</div>{ICON["close"]}</div>
<div style="padding:18px 28px;border-bottom:1px solid #2A2A33"><div style="font-size:14px;margin-bottom:10px">You are <b class="acid">€30</b> away from free shipping</div><div style="height:6px;background:#2A2A33"><div style="width:80%;height:6px;background:#C6FF3D"></div></div></div>
<div style="padding:0 28px;flex:1">{line("product-hoodie","Shift hoodie","Washed black / M","€180")}{line("product-cap","Six-panel cap","Black / One size","€55")}
<div class="lbl muted" style="margin:24px 0 14px">Pairs well with</div><div class="row" style="gap:12px">{"".join(f'<div style="flex:1;background:#16161D">{ph(s, style="height:120px")}<div style="padding:10px"><div style="font-size:13px;font-weight:600">{n}</div><div class="muted" style="font-size:12px">{p}</div></div></div>' for s,n,p in [("product-tee","Boxy tee","€75"),("product-cargo","Utility cargo","€210"),("product-sneaker","Runner 02","€260")])}</div></div>
<div style="padding:24px 28px;border-top:1px solid #2A2A33"><div class="muted" style="font-size:13px;text-decoration:underline;margin-bottom:16px">Add order note</div><div style="display:flex;justify-content:space-between;font-size:18px;font-weight:700;margin-bottom:6px"><span>Subtotal</span><span>€235</span></div><div class="muted" style="font-size:13px;margin-bottom:18px">Taxes included. Discounts and shipping calculated at checkout.</div><div class="btn" style="width:100%;justify-content:center;height:58px">Checkout</div><div class="row" style="gap:8px;margin-top:10px"><div style="flex:1;height:48px;background:#5A31F4;display:flex;align-items:center;justify-content:center;font-weight:700">Shop Pay</div><div style="flex:1;height:48px;background:#F4F4F0;color:#0B0B0F;display:flex;align-items:center;justify-content:center;font-weight:700"> Pay</div></div></div></div></div>'''

# ---------------- PASSWORD / DROP GATE ----------------
gate = f'''<div class="screen d" id="password-drop-desktop" style="height:900px">{ph("drop-gate", style="position:absolute;inset:0;height:900px")}
<div style="position:absolute;inset:0;background:rgba(11,11,15,.55)"></div>
<div style="position:absolute;top:32px;left:32px;right:32px;display:flex;justify-content:space-between;align-items:center"><div class="logo">AFTER<b>/</b>HOURS</div><div class="lbl muted">Store password →</div></div>
<div style="position:absolute;left:0;right:0;top:230px;text-align:center"><div class="lbl acid" style="margin-bottom:24px">Drop 08 · members first</div><div class="disp" style="font-size:200px">Blackout</div>
<div style="display:flex;justify-content:center;gap:56px;margin:36px 0 44px"><div><div class="lbl muted">Release</div><div class="disp" style="font-size:36px;margin-top:8px">Fri 07 Nov</div></div><div><div class="lbl muted">Time</div><div class="disp" style="font-size:36px;margin-top:8px">18:00 CET</div></div><div><div class="lbl muted">Access</div><div class="disp" style="font-size:36px;margin-top:8px">List only</div></div></div>
<div style="display:flex;width:560px;margin:0 auto"><div class="input" style="background:rgba(11,11,15,.6)">Email for early access</div><div class="btn">Join the list</div></div>
<div class="muted" style="font-size:13px;margin-top:16px">Members get the link 1 hour before everyone else.</div></div></div>'''

# ---------------- MOBILE ----------------
mhdr = f'''<div class="ticker" style="font-size:12px;height:32px"><span>Drop 07 out now ✦ Free shipping over €150 ✦</span></div><div class="hdr" style="padding:0 16px;height:60px"><div class="l" style="width:80px;gap:16px">{ICON["menu"]}{ICON["search"]}</div><div class="logo" style="font-size:20px">AFTER<b>/</b>HOURS</div><div class="r" style="width:80px;gap:16px">{ICON["user"]}{ICON["bag"]}</div></div>'''
mcard = lambda s,n,p,b=None: card(s,n,p,b,("S","M","L"))
m_home = f'''<div class="screen m" id="home-mobile">{mhdr}
<div style="position:relative;height:640px">{ph("home-hero-mobile", style="position:absolute;inset:0;height:640px")}<div style="position:absolute;inset:0;background:linear-gradient(180deg,transparent 30%,rgba(11,11,15,.9))"></div>
<div style="position:absolute;left:16px;right:16px;bottom:28px"><div class="lbl acid" style="margin-bottom:12px">Drop 07 — out now</div><div class="disp" style="font-size:84px">Night<br>shift</div><div class="btn" style="width:100%;justify-content:center;margin-top:20px">Shop the drop</div></div></div>
<div style="padding:48px 16px"><div class="disp" style="font-size:44px;margin-bottom:20px">The drop</div><div class="row" style="gap:8px;margin-bottom:20px"><div class="chip on">All</div><div class="chip">Tops</div><div class="chip">Bottoms</div></div>
<div class="row" style="gap:8px;margin-bottom:8px">{mcard("product-hoodie","Shift hoodie","€180","new")}{mcard("product-cargo","Utility cargo","€210")}</div><div class="row" style="gap:8px">{mcard("product-jacket","Track jacket","€240","last")}{mcard("product-tee","Boxy tee","€75","sold")}</div></div>
<div style="margin:0 16px 48px;background:#C6FF3D;color:#0B0B0F;padding:28px"><div class="lbl">Next drop · members first</div><div class="disp" style="font-size:56px;margin:14px 0">Drop 08<br>Blackout</div><div class="disp" style="font-size:24px;margin-bottom:20px">Fri 07 Nov · 18:00 CET</div><div class="input" style="border-color:#0B0B0F;color:#3A4A10;margin-bottom:8px">Email for early access</div><div class="btn dark" style="width:100%;justify-content:center">Get access</div></div>
<div style="display:flex;justify-content:space-around;height:64px;align-items:center;border-top:1px solid #2A2A33;background:#0B0B0F"><span class="lbl acid">Shop</span><span class="lbl muted">Drops</span><span class="lbl muted">Search</span><span class="lbl muted">Bag (2)</span></div></div>'''
m_pdp = f'''<div class="screen m" id="product-mobile">{mhdr}
<div style="position:relative">{ph("pdp-1-mobile", style="aspect-ratio:4/5")}<div style="position:absolute;bottom:16px;left:0;right:0;display:flex;justify-content:center;gap:6px"><span style="width:22px;height:3px;background:#C6FF3D"></span><span style="width:22px;height:3px;background:#55555E"></span><span style="width:22px;height:3px;background:#55555E"></span></div></div>
<div style="padding:24px 16px 120px"><div class="row" style="gap:6px;margin-bottom:14px"><div class="badge" style="position:static">New</div><div class="badge cs" style="position:static">Drop 07</div></div><div class="disp" style="font-size:48px">Shift hoodie</div><div style="font-size:22px;font-weight:700;margin:12px 0 4px">€180</div><div class="muted" style="font-size:13px;margin-bottom:22px">Taxes included · or 4 × €45 with Shop Pay</div>
<div style="display:flex;justify-content:space-between;margin-bottom:10px"><div class="lbl">Size — M</div><div class="lbl acid">Size guide</div></div><div class="row" style="gap:6px;margin-bottom:10px"><div class="sz x" style="width:56px">XS</div><div class="sz" style="width:56px">S</div><div class="sz on" style="width:56px">M</div><div class="sz" style="width:56px">L</div><div class="sz" style="width:56px">XL</div></div><div class="muted" style="font-size:12px;margin-bottom:22px">Model is 186 cm and wears M</div>
<div class="acc"><span>Details</span><span>+</span></div><div class="acc"><span>Fit and sizing</span><span>+</span></div><div class="acc" style="border-bottom:1px solid #2A2A33"><span>Shipping and returns</span><span>+</span></div></div>
<div style="position:absolute;left:0;right:0;bottom:0;padding:12px 16px;background:#0B0B0F;border-top:1px solid #2A2A33;display:flex;gap:8px"><div class="btn" style="flex:1;justify-content:center">Add to bag — €180</div></div></div>'''

html = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{home}{collection}{product}{cart}{gate}{m_home}{m_pdp}</body></html>'
open(OUT, "w").write(html)
json.dump(SLOTS, open(os.path.join(os.path.dirname(__file__), "slots.json"), "w"), indent=1)
print(len(html), "bytes,", len(SLOTS), "placeholders")
