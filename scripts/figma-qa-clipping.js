// Figma QA — clipping audit (team rule 14). Run with the Figma MCP `use_figma` tool.
// Set SCREEN_IDS to the frame ids from banks/design/specs/<niche>/spec.json → figma.frames.
// Returns, per screen, every node that is cut by a clipping ancestor or by the screen edge.
// A passing design returns an empty list for every screen.
const SCREEN_IDS = [/* "107:2", "108:2", ... */];
const TOL = 1.5; // px
const res = {};
for (const id of SCREEN_IDS) {
  const s = await figma.getNodeByIdAsync(id);
  const out = [];
  const walk = (node, clips) => {
    if (!("children" in node)) return;
    for (const ch of node.children) {
      if (ch.visible === false) continue;
      const b = ch.absoluteBoundingBox;
      if (b && b.width > 0 && b.height > 0) {
        for (const c of clips) {
          const cut = { left: c.x - b.x, right: b.x + b.width - (c.x + c.width), top: c.y - b.y, bottom: b.y + b.height - (c.y + c.height) };
          const m = Math.max(...Object.values(cut));
          if (m > TOL) {
            out.push({ node: ch.id, what: ch.type === "TEXT" ? "TEXT: " + ch.characters.slice(0, 40) : ch.type + " " + ch.name.slice(0, 30), cutBy: Math.round(m), sides: Object.keys(cut).filter(k => cut[k] > TOL) });
            break;
          }
        }
      }
      const next = ch.type === "FRAME" && ch.clipsContent && b ? [...clips, b] : clips;
      walk(ch, next);
    }
  };
  walk(s, [s.absoluteBoundingBox]);
  res[s.name] = out;
}
return res;
