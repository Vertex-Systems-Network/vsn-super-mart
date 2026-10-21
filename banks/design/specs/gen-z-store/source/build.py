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
 "heart": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#F4F4F0" stroke-width="1.8"><path d="M12 20s-7-4.4-9-9a4.8 4.8 0 0 1 9-3 4.8 4.8 0 0 1 9 3c-2 4.6-9 9-9 9Z"/></svg>',
 "heartf": '<svg width="18" height="18" viewBox="0 0 24 24" fill="#C6FF3D" stroke="#C6FF3D" stroke-width="1.8"><path d="M12 20s-7-4.4-9-9a4.8 4.8 0 0 1 9-3 4.8 4.8 0 0 1 9 3c-2 4.6-9 9-9 9Z"/></svg>',
 "heartS": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#F4F4F0" stroke-width="1.8"><path d="M12 20s-7-4.4-9-9a4.8 4.8 0 0 1 9-3 4.8 4.8 0 0 1 9 3c-2 4.6-9 9-9 9Z"/></svg>',
 "compare": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#F4F4F0" stroke-width="1.8"><path d="M7 4v16M17 4v16M3 8l4-4 4 4M13 16l4 4 4-4"/></svg>',
 "eye": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#F4F4F0" stroke-width="1.8"><path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12Z"/><circle cx="12" cy="12" r="3"/></svg>',
 "tag": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#0B0B0F" stroke-width="2"><path d="M3 12V3h9l9 9-9 9-9-9Z"/><circle cx="8" cy="8" r="1.5"/></svg>',
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
.hdr .l,.hdr .r{display:flex;gap:22px;align-items:center;width:300px}.hdr .r{justify-content:flex-end}
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
.ico{position:absolute;top:12px;right:12px;display:flex;flex-direction:column;gap:6px}
.ico span{width:36px;height:36px;background:rgba(11,11,15,.7);border:1px solid #2A2A33;display:flex;align-items:center;justify-content:center}
.ico span.on{border-color:#C6FF3D}
.qv{position:absolute;left:12px;right:12px;bottom:118px;height:40px;background:#F4F4F0;color:#0B0B0F;display:flex;align-items:center;justify-content:center;gap:8px;font-size:12px;font-weight:700;letter-spacing:.1em;text-transform:uppercase}
.was{color:#77777F;text-decoration:line-through;font-weight:500;margin-left:8px}
.sale{color:#FF3D6E}
.badge.sl{background:#FF3D6E;color:#0B0B0F}
.ovl{position:absolute;inset:0;background:rgba(5,5,10,.78)}
.pay{display:flex;gap:8px}.pay span{width:44px;height:28px;background:#F4F4F0;color:#0B0B0F;font-size:9px;font-weight:800;display:flex;align-items:center;justify-content:center}
"""

def header(cart=2):
    return f'''<div class="ticker"><span>Drop 07 "Night Shift" — Fri 24 Oct, 18:00 CET</span><span>✦</span><span>Free shipping over €150</span><span>✦</span><span>Early access for members</span><span>✦</span><span>Drop 07 "Night Shift" — Fri 24 Oct, 18:00 CET</span><span>✦</span><span>Free shipping over €150</span></div>
<div class="hdr"><div class="l">{ICON["menu"]}<span class="lbl">Menu</span>{ICON["search"]}</div><div class="logo">AFTER<b>/</b>HOURS</div><div class="r"><span class="lbl muted" style="display:flex;gap:6px;align-items:center">{ICON["globe"]} EN · EUR</span>{ICON["heart"]}<span class="count">3</span>{ICON["user"]}{ICON["bag"]}<span class="count">{cart}</span></div></div>'''

def card(slot, name, price, badge=None, sizes=("S","M","L","XL"), xs=(), was=None, wish=False, cmp=False, qv=False):
    b = ""
    if was:
        pct = round(100 - 100*float(price.strip("€"))/float(was.strip("€")))
        b = f'<div class="badge sl">-{pct}%</div>'
        price = f'<span class="sale">{price}</span><span class="was">{was}</span>'
    ico = f'<div class="ico"><span class="{"on" if wish else ""}">{ICON["heartf"] if wish else ICON["heartS"]}</span><span class="{"on" if cmp else ""}">{ICON["compare"]}</span><span>{ICON["eye"]}</span></div>'
    q = f'<div class="qv">{ICON["eye"].replace("#F4F4F0","#0B0B0F")} Quick view</div>' if qv else ""
    if badge == "new": b = '<div class="badge">New</div>'
    if badge == "sold": b = '<div class="badge so">Sold out</div>'
    if badge == "soon": b = '<div class="badge cs">Coming soon</div>'
    if badge == "last": b = '<div class="badge">Last sizes</div>'
    sz = "".join(f'<span class="{"x" if s in xs else ""}">{s}</span>' for s in sizes)
    return f'<div class="card">{ph(slot)}{b}{ico}{q}<div class="meta"><div><div class="nm">{name}</div><div class="pr">{price}</div><div class="sizes">{sz}</div></div></div></div>'

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
<div class="row">{card("product-hoodie","Shift hoodie","€180","new",wish=True)}{card("product-cargo","Utility cargo","€210",None,("28","30","32","34"),("28",),qv=True,cmp=True)}{card("product-jacket","Lime track jacket","€240","last",("S","M","L","XL"),("S","M"))}{card("product-tee","Boxy tee 280g","€75","sold",("S","M","L","XL"),("S","M","L","XL"))}</div></div>
<div class="sec" style="padding-top:0;padding-bottom:48px"><div style="display:flex;gap:16px">
<div style="flex:2;position:relative;height:420px">{ph("promo-archive", style="position:absolute;inset:0;height:420px")}<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(11,11,15,.92),rgba(11,11,15,.2))"></div>
<div style="position:absolute;left:48px;top:48px;bottom:48px;display:flex;flex-direction:column;justify-content:space-between"><div><div style="display:inline-flex;align-items:center;gap:8px;background:#FF3D6E;color:#0B0B0F;padding:6px 10px" class="lbl">{ICON["tag"]} Archive sale</div><div class="disp" style="font-size:104px;margin-top:20px">Up to <span class="acid">40%</span> off</div></div>
<div style="display:flex;align-items:center;gap:28px"><div class="btn">Shop the sale {ICON["arrow"]}</div><div class="lbl muted">Past drops only · ends Sun 26 Oct, 23:59 CET</div></div></div></div>
<div style="flex:1;display:flex;flex-direction:column;gap:16px">
<div style="flex:1;background:#C6FF3D;color:#0B0B0F;padding:32px;display:flex;flex-direction:column;justify-content:space-between"><div class="lbl">Members deal</div><div class="disp" style="font-size:56px">Free express<br>shipping</div><div class="lbl">On every drop for list members</div></div>
<div style="flex:1;background:#16161D;border:1px solid #2A2A33;padding:32px;display:flex;flex-direction:column;justify-content:space-between"><div class="lbl acid">Bundle and save</div><div class="disp" style="font-size:44px">Hoodie + cargo<br>save 15%</div><div class="lbl muted">Applied automatically at checkout →</div></div></div></div></div>
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
grid = (f'<div class="row" style="margin-bottom:16px">{card("product-hoodie","Shift hoodie","€180","new",wish=True,cmp=True)}{card("product-cargo","Utility cargo","€210",None,xs=("S",),cmp=True,qv=True)}{card("product-jacket","Lime track jacket","€240","last",xs=("S","M"),cmp=True)}{card("product-tee","Boxy tee 280g","€75","sold",xs=("S","M","L","XL"))}</div>'
  f'<div class="row" style="margin-bottom:16px">{card("product-sneaker","Runner 02","€182",None,("40","41","42","43"),was="€260")}'
  f'<div class="card" style="background:#C6FF3D;color:#0B0B0F;padding:28px;display:flex;flex-direction:column;justify-content:space-between"><div class="lbl" style="display:flex;gap:8px;align-items:center">{ICON["tag"]} Archive sale</div><div class="disp" style="font-size:72px">40%<br>off</div><div><div style="font-size:15px;font-weight:600;margin-bottom:16px">Past drops, final sizes. Ends Sun 26 Oct.</div><div class="btn dark" style="width:100%;justify-content:center">Shop sale</div></div></div>'
  f'{card("product-puffer","Nylon puffer","€320","soon")}{card("product-hoodie-2","Zip hoodie","€137",None,xs=("XL",),was="€195")}</div>')
cmpbar = f'''<div style="position:absolute;left:0;right:0;bottom:0;height:96px;background:#16161D;border-top:2px solid #C6FF3D;display:flex;align-items:center;gap:20px;padding:0 32px">
<div class="lbl acid" style="width:140px">Compare (3/4)</div>
{"".join(f'<div style="display:flex;gap:12px;align-items:center;border:1px solid #2A2A33;padding:8px 12px;width:230px"><div style="width:48px">{ph(s_, style="height:60px")}</div><div style="flex:1"><div style="font-size:13px;font-weight:700;text-transform:uppercase">{n_}</div><div class="muted" style="font-size:12px">{p_}</div></div>{ICON["close"]}</div>' for s_,n_,p_ in [("product-hoodie","Shift hoodie","€180"),("product-cargo","Utility cargo","€210"),("product-jacket","Track jacket","€240")])}
<div style="width:230px;height:78px;border:1px dashed #3A3A44;display:flex;align-items:center;justify-content:center" class="lbl muted">+ Add product</div>
<div style="flex:1"></div><div class="lbl muted" style="text-decoration:underline">Clear</div><div class="btn">Compare now</div></div>'''
collection = f'''<div class="screen d" id="collection-desktop">{header()}
<div style="padding:64px 32px 40px;display:flex;justify-content:space-between;align-items:flex-end;border-bottom:1px solid #2A2A33"><div><div class="lbl muted" style="margin-bottom:16px">Home / Drop 07</div><div class="disp" style="font-size:120px">Night shift</div></div><p class="muted" style="width:420px;font-size:16px;line-height:1.55">14 pieces in washed black and acid lime. Limited runs, no restocks — when a size is gone, it is gone.</p></div>
<div style="display:flex;justify-content:space-between;align-items:center;padding:20px 32px;border-bottom:1px solid #2A2A33"><div class="row" style="gap:8px"><div class="chip">Availability {ICON["chev"]}</div><div class="chip">Size {ICON["chev"]}</div><div class="chip">Color {ICON["chev"]}</div><div class="chip">Price {ICON["chev"]}</div><div class="chip">Product type {ICON["chev"]}</div><div class="chip on">In stock ✕</div></div>
<div style="display:flex;gap:24px;align-items:center"><span class="muted" style="font-size:14px">14 products</span><div class="chip">Sort: Featured {ICON["chev"]}</div><div class="chip">Hide sold out</div></div></div>
<div style="padding:24px 32px">{grid}</div>
<div style="display:flex;justify-content:center;padding:24px 0 96px"><div class="btn ghost">Load more · 8 of 14</div></div>
{footer()}{cmpbar}</div>'''

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
<div class="muted" style="text-align:center;font-size:13px;margin:12px 0 18px;text-decoration:underline">More payment options</div>
<div class="row" style="gap:8px;margin-bottom:28px"><div class="btn ghost" style="flex:1;justify-content:center;height:46px;font-size:12px">{ICON["heartS"]} Add to wishlist</div><div class="btn ghost" style="flex:1;justify-content:center;height:46px;font-size:12px">{ICON["compare"]} Compare</div></div>
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


# =============== NEW SCREENS (rule 12 + remaining templates) ===============
def scr(id_, body, h=None, m=False):
    st = f' style="height:{h}px"' if h else ""
    return f'<div class="screen {"m" if m else "d"} nb" id="{id_}"{st}>{body}</div>'

# Quick view modal over collection
qv = scr("quick-view-desktop", f'''{header()}<div class="ovl"></div>
<div style="position:absolute;left:200px;top:150px;width:1040px;height:640px;background:#0B0B0F;border:1px solid #2A2A33;display:flex">
<div style="width:500px;position:relative">{ph("product-cargo", style="height:640px")}<div style="position:absolute;bottom:16px;left:0;right:0;display:flex;justify-content:center;gap:6px"><span style="width:22px;height:3px;background:#C6FF3D"></span><span style="width:22px;height:3px;background:#55555E"></span><span style="width:22px;height:3px;background:#55555E"></span></div></div>
<div style="flex:1;padding:40px;position:relative"><div style="position:absolute;top:20px;right:20px">{ICON["close"]}</div><div class="lbl acid">Quick view</div><div class="disp" style="font-size:56px;margin:16px 0 12px">Utility cargo</div><div style="font-size:22px;font-weight:700;margin-bottom:4px">€210</div><div class="muted" style="font-size:13px;margin-bottom:24px">Taxes included · or 4 × €52.50 with Shop Pay</div>
<div class="lbl" style="margin-bottom:10px">Waist — 32</div><div class="row" style="gap:8px;margin-bottom:24px"><div class="sz x">28</div><div class="sz">30</div><div class="sz on">32</div><div class="sz">34</div><div class="sz">36</div></div>
<div class="btn" style="width:100%;justify-content:center;height:56px">Add to bag — €210</div><div class="row" style="gap:8px;margin-top:10px"><div class="btn ghost" style="flex:1;justify-content:center;height:46px;font-size:12px">{ICON["heartS"]} Wishlist</div><div class="btn ghost" style="flex:1;justify-content:center;height:46px;font-size:12px">{ICON["compare"]} Compare</div></div>
<div class="lbl acid" style="margin-top:28px;text-decoration:underline">View full details →</div></div></div>''', 940)

# Wishlist page
wl_items = [("product-hoodie","Shift hoodie","€180",None),("product-puffer","Nylon puffer","€320","soon"),("product-sneaker","Runner 02","€182","sale"),("product-cap","Six-panel cap","€55",None)]
def wcard(sl,n,p_,t):
    if t=="sale": return card(sl,n,p_,None,("40","41","42"),was="€260",wish=True)
    return card(sl,n,p_,t,wish=True)
wishlist = scr("wishlist-desktop", f'''{header()}<div style="padding:64px 32px 32px;display:flex;justify-content:space-between;align-items:flex-end;border-bottom:1px solid #2A2A33"><div><div class="lbl muted" style="margin-bottom:16px">Account / Wishlist</div><div class="disp" style="font-size:120px">Wishlist <span class="acid">(4)</span></div></div><div class="row"><div class="btn ghost">Share list</div><div class="btn">Add all to bag</div></div></div>
<div style="padding:24px 32px 12px;display:flex;gap:12px;align-items:center"><div style="width:10px;height:10px;border-radius:5px;background:#FF3D6E"></div><span style="font-size:14px">1 item is on sale · 1 drops Fri 07 Nov — we will email you.</span></div>
<div style="padding:24px 32px 96px"><div class="row">{"".join(wcard(*i) for i in wl_items)}</div></div>{footer()}''')

# Compare page
rows=[("Price","€180","€210","€240"),("Material","100% cotton, 480g","Ripstop nylon","Recycled nylon"),("Fit","Oversized","Relaxed, tapered","Regular"),("Sizes in stock","S, M, L, XL","30–36","L, XL"),("Care","Wash cold, inside out","Machine wash 30°","Hand wash"),("Drop","07 Night Shift","07 Night Shift","07 Night Shift"),("Rating","★★★★★ 4.9","★★★★☆ 4.6","★★★★★ 4.8")]
cmpcols="".join(f'<div style="flex:1;padding:0 12px">{card(sl,n,p_)}<div class="btn" style="width:100%;justify-content:center;margin-top:12px">Add to bag</div></div>' for sl,n,p_ in [("product-hoodie","Shift hoodie","€180"),("product-cargo","Utility cargo","€210"),("product-jacket","Track jacket","€240")])
cmprows="".join(f'<div style="display:flex;border-top:1px solid #2A2A33;padding:18px 0"><div class="lbl muted" style="width:260px;padding-top:2px">{r[0]}</div>{"".join(f"<div style=\'flex:1;padding:0 12px;font-size:15px\'>{v}</div>" for v in r[1:])}</div>' for r in rows)
compare = scr("compare-desktop", f'''{header()}<div style="padding:64px 32px 32px"><div class="lbl muted" style="margin-bottom:16px">Compare</div><div class="disp" style="font-size:120px">Side by side</div><div class="row" style="margin-top:24px;gap:8px"><div class="chip on">Show all</div><div class="chip">Only differences</div></div></div>
<div style="padding:0 32px"><div style="display:flex"><div style="width:260px"></div>{cmpcols}</div><div style="margin-top:32px;margin-bottom:96px">{cmprows}</div></div>{footer()}''')

# Search + predictive search open
search = scr("search-desktop", f'''{header()}<div style="padding:48px 32px;border-bottom:1px solid #2A2A33"><div style="display:flex;align-items:center;gap:16px;border-bottom:2px solid #C6FF3D;padding-bottom:16px">{ICON["search"]}<div class="disp" style="font-size:64px">Hood<span class="muted">ie</span></div><div style="flex:1"></div>{ICON["close"]}</div>
<div style="display:flex;gap:48px;margin-top:32px"><div style="width:260px"><div class="lbl muted" style="margin-bottom:16px">Suggestions</div>{"".join(f'<div style="font-size:16px;margin-bottom:14px">{x}</div>' for x in ["<b>hood</b>ie","<b>hood</b>ie zip","washed black <b>hood</b>ie","<b>hood</b>ed puffer"])}<div class="lbl muted" style="margin:28px 0 16px">Pages</div><div style="font-size:16px;margin-bottom:14px">Size guide</div><div style="font-size:16px">Shipping and returns</div></div>
<div style="flex:1"><div class="lbl muted" style="margin-bottom:16px">Products</div><div class="row">{card("product-hoodie","Shift hoodie","€180","new")}{card("product-hoodie-2","Zip hoodie","€137",None,was="€195")}{card("product-puffer","Nylon puffer","€320","soon")}</div></div></div></div>
<div style="padding:40px 32px 96px"><div class="sechead"><div class="disp" style="font-size:56px">6 results for “hoodie”</div><div class="row" style="gap:8px"><div class="chip on">Products (4)</div><div class="chip">Journal (1)</div><div class="chip">Pages (1)</div></div></div><div class="row">{card("product-hoodie","Shift hoodie","€180","new",wish=True)}{card("product-hoodie-2","Zip hoodie","€137",None,was="€195")}{card("product-jacket","Lime track jacket","€240","last")}{card("product-tee","Boxy tee 280g","€75","sold")}</div></div>{footer()}''')

# Cart page
def cline(sl,n,v,p_,was=None):
    pr = f'<span class="sale">{p_}</span><span class="was">{was}</span>' if was else p_
    return f'<div style="display:flex;gap:24px;padding:28px 0;border-top:1px solid #2A2A33;align-items:center"><div style="width:120px">{ph(sl, style="height:150px")}</div><div style="flex:1"><div class="disp" style="font-size:28px">{n}</div><div class="muted" style="font-size:14px;margin-top:8px">{v}</div><div class="lbl muted" style="margin-top:16px;text-decoration:underline">Move to wishlist · Remove</div></div><div style="display:flex;border:1.5px solid #3A3A44;height:44px;align-items:center"><span style="width:44px;text-align:center">−</span><span style="width:30px;text-align:center;font-weight:600">1</span><span style="width:44px;text-align:center">+</span></div><div style="width:160px;text-align:right;font-weight:700;font-size:18px">{pr}</div></div>'
cartpage = scr("cart-page-desktop", f'''{header()}<div style="padding:64px 32px 96px;display:flex;gap:64px"><div style="flex:1"><div class="disp" style="font-size:120px;margin-bottom:24px">Bag (3)</div>
<div style="background:#16161D;padding:18px;margin-bottom:8px"><div style="font-size:14px;margin-bottom:10px">You unlocked <b class="acid">free shipping</b></div><div style="height:6px;background:#C6FF3D"></div></div>
{cline("product-hoodie","Shift hoodie","Washed black / M","€180")}{cline("product-sneaker","Runner 02","Black lime / 42","€182","€260")}{cline("product-cap","Six-panel cap","Black / One size","€55")}
<div style="border-top:1px solid #2A2A33;padding-top:24px"><div class="lbl muted" style="margin-bottom:12px">Order note</div><div class="input" style="height:96px;align-items:flex-start;padding-top:16px">Gift message or delivery note</div></div></div>
<div style="width:440px"><div style="background:#16161D;border:1px solid #2A2A33;padding:32px;margin-top:148px"><div class="disp" style="font-size:32px;margin-bottom:24px">Summary</div>
<div style="display:flex;justify-content:space-between;margin-bottom:12px"><span class="muted">Subtotal</span><span>€495</span></div><div style="display:flex;justify-content:space-between;margin-bottom:12px"><span class="muted">Archive sale</span><span class="sale">−€78</span></div><div style="display:flex;justify-content:space-between;margin-bottom:12px"><span class="muted">Bundle: hoodie + cargo</span><span class="muted">add cargo to save 15%</span></div><div style="display:flex;justify-content:space-between;margin-bottom:20px"><span class="muted">Shipping</span><span class="acid">Free</span></div>
<div style="display:flex;justify-content:space-between;font-size:22px;font-weight:700;border-top:1px solid #2A2A33;padding-top:20px"><span>Total</span><span>€417</span></div><div class="muted" style="font-size:13px;margin:6px 0 24px">Taxes included. Discount codes are added at checkout.</div>
<div class="btn" style="width:100%;justify-content:center;height:60px">Checkout</div><div class="row" style="gap:8px;margin-top:10px"><div style="flex:1;height:50px;background:#5A31F4;display:flex;align-items:center;justify-content:center;font-weight:700">Shop Pay</div><div style="flex:1;height:50px;background:#F4F4F0;color:#0B0B0F;display:flex;align-items:center;justify-content:center;font-weight:700"> Pay</div><div style="flex:1;height:50px;background:#FFC439;color:#0B0B0F;display:flex;align-items:center;justify-content:center;font-weight:700">PayPal</div></div></div></div></div>
<div class="sec" style="padding-top:0"><div class="sechead"><div class="disp" style="font-size:56px">You might also like</div></div><div class="row">{card("product-cargo","Utility cargo","€210",qv=True)}{card("product-tee","Boxy tee 280g","€75")}{card("product-jacket","Lime track jacket","€240","last")}{card("product-puffer","Nylon puffer","€320","soon")}</div></div>{footer()}''')

# Promo popup over home hero
popup = scr("promo-popup-desktop", f'''{header()}{ph("home-hero", style="height:828px")}<div class="ovl" style="top:108px"></div>
<div style="position:absolute;left:300px;top:230px;width:840px;height:500px;display:flex;background:#0B0B0F;border:1px solid #C6FF3D">
<div style="width:380px">{ph("drop-next", style="height:500px")}</div><div style="flex:1;padding:44px;position:relative"><div style="position:absolute;top:20px;right:20px">{ICON["close"]}</div><div class="lbl acid">Join the list</div><div class="disp" style="font-size:64px;margin:16px 0">10% off your<br>first order</div><p class="muted" style="font-size:15px;line-height:1.5;margin-bottom:24px">Plus early access to every drop. No spam, unsubscribe anytime.</p><div class="input" style="margin-bottom:10px">Email address</div><div class="btn" style="width:100%;justify-content:center">Get my code</div><div class="lbl muted" style="margin-top:16px;text-decoration:underline">No thanks</div></div></div>''', 936)

# List collections
lc = scr("list-collections-desktop", f'''{header()}<div style="padding:64px 32px 40px"><div class="disp" style="font-size:120px">All collections</div></div>
<div style="padding:0 32px 96px"><div class="row" style="margin-bottom:16px">{"".join(f'<div class="card">{ph(sl, style="aspect-ratio:1/1")}<div class="meta"><div><div class="disp" style="font-size:44px">{n}</div><div class="muted" style="font-size:14px;margin-top:6px">{c} products</div></div>{ICON["arrow"]}</div></div>' for sl,n,c in [("lookbook","Drop 07 · Night Shift","14"),("drop-next","Drop 08 · Blackout","09"),("category-tops","Tops","22")])}</div>
<div class="row">{"".join(f'<div class="card">{ph(sl, style="aspect-ratio:1/1")}<div class="meta"><div><div class="disp" style="font-size:44px">{n}</div><div class="muted" style="font-size:14px;margin-top:6px">{c} products</div></div>{ICON["arrow"]}</div>{b}</div>' for sl,n,c,b in [("category-bottoms","Bottoms","15",""),("category-accessories","Accessories","18",""),("promo-archive","Archive sale","31",'<div class="badge sl">-40%</div>')])}</div></div>{footer()}''')

# Contact
contact = scr("contact-desktop", f'''{header()}<div style="display:flex;padding:64px 32px 96px;gap:64px"><div style="flex:1"><div class="disp" style="font-size:120px">Contact</div><p class="muted" style="font-size:16px;line-height:1.6;margin:24px 0 40px;max-width:460px">Order questions, sizing help or collabs — we reply within 24 hours, Monday to Friday.</p>
<div style="display:flex;flex-direction:column;gap:20px;max-width:460px">{"".join(f'<div><div class="lbl muted" style="margin-bottom:6px">{a}</div><div style="font-size:17px">{b}</div></div>' for a,b in [("Email","support@afterhours.store"),("Studio","Torstraße 101, 10119 Berlin"),("Hours","Mon–Fri, 10:00–18:00 CET")])}</div></div>
<div style="width:640px;background:#16161D;border:1px solid #2A2A33;padding:40px"><div class="disp" style="font-size:36px;margin-bottom:24px">Send a message</div><div class="row" style="gap:12px;margin-bottom:12px"><div class="input">Name</div><div class="input">Email</div></div><div class="input" style="margin-bottom:12px">Order number (optional)</div><div class="input" style="height:160px;align-items:flex-start;padding-top:16px;margin-bottom:20px">Message</div><div class="btn">Send message</div></div></div>
<div class="sec" style="padding-top:0"><div class="disp" style="font-size:56px;margin-bottom:24px">FAQ</div>{"".join(f'<div class="acc"><span>{q}</span><span>+</span></div>' for q in ["When do drops go live?","Do you restock sold-out sizes?","How long is shipping to the US and EU?","How do returns work?"])}</div>{footer()}''')

# Blog
posts=[("lookbook","Lookbook","Parking level −2: shooting Drop 07","12 Oct 2026"),("ugc-3","Community","#AfterHoursFit: your best fits this month","05 Oct 2026"),("drop-gate","Behind the drop","How we build a no-restock drop","28 Sep 2026")]
blog = scr("blog-desktop", f'''{header()}<div style="padding:64px 32px 40px;display:flex;justify-content:space-between;align-items:flex-end"><div class="disp" style="font-size:120px">Journal</div><div class="row" style="gap:8px"><div class="chip on">All</div><div class="chip">Lookbook</div><div class="chip">Community</div><div class="chip">Behind the drop</div></div></div>
<div style="padding:0 32px 96px"><div style="position:relative;margin-bottom:32px">{ph("home-hero", style="height:560px")}<div style="position:absolute;inset:0;background:linear-gradient(transparent 40%,rgba(11,11,15,.9))"></div><div style="position:absolute;left:40px;bottom:40px;max-width:760px"><div class="lbl acid">Featured · 18 Oct 2026</div><div class="disp" style="font-size:88px;margin:14px 0">Night shift: the film</div><p style="font-size:16px;color:#D9D9DE">Three nights, one city, fourteen pieces. Read the story behind the drop.</p></div></div>
<div class="row" style="gap:24px">{"".join(f'<div style="flex:1">{ph(sl, style="aspect-ratio:4/3")}<div class="lbl acid" style="margin:18px 0 10px">{t} · {d}</div><div class="disp" style="font-size:32px;line-height:1">{h}</div><p class="muted" style="font-size:15px;line-height:1.5;margin-top:12px">A short excerpt of the story so readers know what to expect before opening it.</p></div>' for sl,t,h,d in posts)}</div>
<div style="display:flex;justify-content:center;margin-top:56px"><div class="btn ghost">Load more stories</div></div></div>{footer()}''')

# Article
article = scr("article-desktop", f'''{header()}<div style="padding:64px 32px 0;text-align:center"><div class="lbl acid">Lookbook · 12 Oct 2026 · 4 min read</div><div class="disp" style="font-size:112px;margin:24px auto;max-width:1100px">Parking level −2: shooting Drop 07</div></div>
<div style="padding:24px 32px">{ph("lookbook", style="height:760px")}</div>
<div style="max-width:720px;margin:48px auto 0;font-size:18px;line-height:1.75;color:#D9D9DE"><p>We shot Drop 07 across three nights in an underground garage in Berlin, using only a flash and one lime tube light.</p><p style="margin-top:24px">Every piece is cut heavier than usual so it holds its shape under harsh light — and on a cold walk home.</p>
<div style="border-left:3px solid #C6FF3D;padding:8px 0 8px 24px;margin:40px 0" class="disp"><span style="font-size:40px;color:#F4F4F0">“Made for the hours nobody photographs.”</span></div></div>
<div style="max-width:720px;margin:0 auto;padding-bottom:40px"><div class="lbl muted" style="margin-bottom:16px">Shop this story</div><div class="row">{card("product-puffer","Nylon puffer","€320","soon")}{card("product-cargo","Utility cargo","€210")}</div></div>
<div style="max-width:720px;margin:0 auto;padding:40px 0 96px;border-top:1px solid #2A2A33"><div class="disp" style="font-size:32px;margin-bottom:20px">Comments (2)</div>{"".join(f'<div style="padding:18px 0;border-bottom:1px solid #2A2A33"><div style="font-weight:700">{n} <span class="muted" style="font-weight:400;font-size:13px">· {d}</span></div><div style="margin-top:8px;color:#D9D9DE">{c}</div></div>' for n,d,c in [("Lena K.","13 Oct","The flash shots are unreal. Need that puffer."),("Marco","14 Oct","Is the cargo true to size?")])}
<div class="input" style="height:120px;align-items:flex-start;padding-top:16px;margin-top:24px">Write a comment</div><div class="row" style="gap:12px;margin-top:12px"><div class="input">Name</div><div class="input">Email</div><div class="btn">Post comment</div></div></div>{footer()}''')

# Account login
login = scr("account-login-desktop", f'''{header()}<div style="display:flex;height:820px"><div style="flex:1;position:relative">{ph("ugc-5", style="height:820px")}<div style="position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(11,11,15,.6))"></div></div>
<div style="width:640px;padding:96px 80px"><div class="disp" style="font-size:88px">Sign in</div><p class="muted" style="font-size:15px;margin:16px 0 32px">Members get early access, saved wishlists and order tracking.</p>
<div style="height:54px;background:#5A31F4;display:flex;align-items:center;justify-content:center;font-weight:700;margin-bottom:20px">Sign in with Shop</div><div class="lbl muted" style="text-align:center;margin-bottom:20px">or continue with email</div>
<div class="input" style="margin-bottom:12px">Email address</div><div class="btn" style="width:100%;justify-content:center">Send login code</div><div class="muted" style="font-size:13px;margin-top:16px">We email a one-time code — no password needed.</div></div></div>{footer()}''')

# Account orders
orders = scr("account-orders-desktop", f'''{header()}<div style="padding:64px 32px 96px;display:flex;gap:64px"><div style="width:260px"><div class="disp" style="font-size:44px;margin-bottom:28px">Hi, Sam</div>{"".join(f'<div style="padding:14px 0;border-top:1px solid #2A2A33;font-weight:600;{"color:#C6FF3D" if i==0 else ""}">{x}</div>' for i,x in enumerate(["Orders","Wishlist (4)","Addresses","Early access: active","Sign out"]))}</div>
<div style="flex:1"><div class="disp" style="font-size:88px;margin-bottom:32px">Orders</div>{"".join(f'<div style="display:flex;align-items:center;gap:24px;padding:24px 0;border-top:1px solid #2A2A33"><div style="width:80px">{ph(sl, style="height:100px")}</div><div style="flex:1"><div style="font-weight:700;font-size:16px">{o}</div><div class="muted" style="font-size:14px;margin-top:6px">{d} · {it}</div></div><div class="lbl" style="padding:6px 10px;{st}">{s_}</div><div style="width:110px;text-align:right;font-weight:700">{p_}</div><div class="btn ghost" style="height:40px;font-size:12px;padding:0 16px">View</div></div>' for sl,o,d,it,s_,st,p_ in [("product-hoodie","#AH-10482","18 Oct 2026","2 items","On the way","background:#C6FF3D;color:#0B0B0F","€235"),("product-sneaker","#AH-10211","02 Oct 2026","1 item","Delivered","border:1px solid #3A3A44","€182"),("product-cap","#AH-09877","14 Sep 2026","3 items","Delivered","border:1px solid #3A3A44","€330")])}</div></div>{footer()}''')

# 404
p404 = scr("not-found-desktop", f'''{header()}<div style="position:relative;height:760px">{ph("drop-gate", style="height:760px")}<div class="ovl" style="background:rgba(11,11,15,.6)"></div><div style="position:absolute;left:0;right:0;top:170px;text-align:center"><div class="disp acid" style="font-size:260px">404</div><div class="disp" style="font-size:56px;margin:12px 0 20px">Lost after hours</div><p class="muted" style="font-size:16px;margin-bottom:32px">This page does not exist. Search for it or head back to the drop.</p><div style="display:flex;justify-content:center;gap:12px"><div class="input" style="flex:none;width:420px;background:rgba(11,11,15,.6)">Search products</div><div class="btn">Back to home</div></div></div></div>{footer()}''')

# Gift card
giftcard = scr("gift-card-desktop", f'''<div style="padding:40px 32px;display:flex;justify-content:center"><div class="logo">AFTER<b>/</b>HOURS</div></div><div style="display:flex;justify-content:center;padding-bottom:96px"><div style="width:620px;text-align:center"><div class="disp" style="font-size:72px">Your gift card</div><p class="muted" style="margin:16px 0 32px">Here is your €100 gift card. Use the code at checkout.</p>
<div style="height:340px;background:#C6FF3D;color:#0B0B0F;padding:36px;display:flex;flex-direction:column;justify-content:space-between;text-align:left"><div style="display:flex;justify-content:space-between"><div class="logo" style="color:#0B0B0F">AFTER/HOURS</div><div class="disp" style="font-size:56px">€100</div></div><div class="lbl">Gift card</div></div>
<div style="display:flex;gap:24px;align-items:center;margin:28px 0;padding:24px;border:1px solid #2A2A33"><div style="width:130px;height:130px;background:#F4F4F0"></div><div style="text-align:left;flex:1"><div class="lbl muted">Code</div><div class="disp" style="font-size:36px;margin:8px 0">X7KQ 2MPL 9RTA</div><div class="lbl acid">Copy code</div></div></div>
<div class="row" style="justify-content:center;gap:8px"><div style="height:52px;padding:0 24px;background:#F4F4F0;color:#0B0B0F;display:flex;align-items:center;font-weight:700">Add to Apple Wallet</div><div class="btn">Start shopping</div><div class="btn ghost">Print</div></div></div></div>''')

# ---- mobile ----
m_col = scr("collection-mobile", f'''{mhdr}<div style="padding:28px 16px 16px"><div class="lbl muted">Home / Drop 07</div><div class="disp" style="font-size:56px;margin-top:10px">Night shift</div></div>
<div style="display:flex;gap:8px;padding:0 16px 16px"><div class="chip" style="flex:1;justify-content:center">Filter (1)</div><div class="chip" style="flex:1;justify-content:center">Sort</div></div>
<div style="padding:0 16px"><div class="row" style="gap:8px;margin-bottom:8px">{card("product-hoodie","Shift hoodie","€180","new",("S","M","L"),wish=True)}{card("product-cargo","Utility cargo","€210",None,("30","32","34"),cmp=True)}</div>
<div style="background:#FF3D6E;color:#0B0B0F;padding:20px;margin-bottom:8px"><div class="lbl">Archive sale</div><div class="disp" style="font-size:44px;margin:8px 0">Up to 40% off</div><div class="lbl">Ends Sun 26 Oct →</div></div>
<div class="row" style="gap:8px;padding-bottom:110px">{card("product-sneaker","Runner 02","€182",None,("41","42","43"),was="€260")}{card("product-tee","Boxy tee","€75","sold",("S","M","L"))}</div></div>
<div style="position:absolute;left:0;right:0;bottom:0;padding:12px 16px;background:#16161D;border-top:2px solid #C6FF3D;display:flex;align-items:center;gap:10px"><div class="lbl acid" style="flex:1">Compare (2)</div><div class="btn" style="height:44px;padding:0 18px">Compare</div></div>''', m=True)
m_cart = scr("cart-drawer-mobile", f'''<div style="display:flex;justify-content:space-between;align-items:center;padding:20px 16px;border-bottom:1px solid #2A2A33"><div class="disp" style="font-size:30px">Bag (2)</div>{ICON["close"]}</div>
<div style="padding:16px;border-bottom:1px solid #2A2A33"><div style="font-size:14px;margin-bottom:10px"><b class="acid">€30</b> away from free shipping</div><div style="height:6px;background:#2A2A33"><div style="width:80%;height:6px;background:#C6FF3D"></div></div></div>
<div style="padding:0 16px">{line("product-hoodie","Shift hoodie","Washed black / M","€180")}{line("product-cap","Six-panel cap","Black / One size","€55")}<div class="lbl muted" style="margin:20px 0 12px">Pairs well with</div><div class="row" style="gap:8px">{"".join(f'<div style="flex:1;background:#16161D">{ph(s_, style="height:110px")}<div style="padding:8px"><div style="font-size:12px;font-weight:600">{n_}</div><div class="muted" style="font-size:12px">{p_}</div></div></div>' for s_,n_,p_ in [("product-tee","Boxy tee","€75"),("product-cargo","Cargo","€210")])}</div></div>
<div style="padding:20px 16px;margin-top:20px;border-top:1px solid #2A2A33"><div style="display:flex;justify-content:space-between;font-size:18px;font-weight:700"><span>Subtotal</span><span>€235</span></div><div class="muted" style="font-size:12px;margin:6px 0 16px">Taxes included. Shipping at checkout.</div><div class="btn" style="width:100%;justify-content:center">Checkout</div><div style="height:48px;background:#5A31F4;display:flex;align-items:center;justify-content:center;font-weight:700;margin-top:8px">Shop Pay</div></div>''', m=True)
m_menu = scr("menu-drawer-mobile", f'''<div style="display:flex;justify-content:space-between;align-items:center;padding:20px 16px"><div class="logo" style="font-size:20px">AFTER<b>/</b>HOURS</div>{ICON["close"]}</div>
<div style="padding:8px 16px">{"".join(f'<div style="display:flex;justify-content:space-between;align-items:center;padding:16px 0;border-bottom:1px solid #2A2A33"><div class="disp" style="font-size:40px;{c}">{t}</div>{ICON["arrow"]}</div>' for t,c in [("Drop 07","color:#C6FF3D"),("Tops",""),("Bottoms",""),("Accessories",""),("Archive sale","color:#FF3D6E"),("Journal","")])}</div>
<div style="margin:16px;position:relative">{ph("drop-next", style="height:200px")}<div style="position:absolute;left:16px;bottom:16px"><div class="lbl acid">Next drop</div><div class="disp" style="font-size:32px">Blackout · 07 Nov</div></div></div>
<div style="padding:16px;display:flex;flex-direction:column;gap:14px"><div style="display:flex;gap:10px;align-items:center">{ICON["user"]} Account</div><div style="display:flex;gap:10px;align-items:center">{ICON["heart"]} Wishlist (3)</div><div class="lbl muted" style="display:flex;gap:6px;align-items:center;margin-top:8px">{ICON["globe"]} Germany (EUR €) · English</div></div>''', m=True)

screens_b = [qv, wishlist, compare, search, cartpage, popup, lc, contact, blog, article, login, orders, p404, giftcard, m_col, m_cart, m_menu]

html = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{home}{collection}{product}{cart}{gate}{m_home}{m_pdp}{''.join(screens_b)}</body></html>'
open(OUT, "w").write(html)
json.dump(SLOTS, open(os.path.join(os.path.dirname(__file__), "slots.json"), "w"), indent=1)
print(len(html), "bytes,", len(SLOTS), "placeholders")
