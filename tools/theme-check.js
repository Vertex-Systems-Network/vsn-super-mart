// Runs Shopify Theme Check (theme-check:recommended) on ./theme and prints offenses.
// Usage: node tools/theme-check.js   (needs: npm i -g @shopify/theme-check-node)
const path = require('node:path');
const { execSync } = require('node:child_process');
const root = execSync('npm root -g').toString().trim();
const { check } = require(path.join(root, '@shopify/theme-check-node'));
(async () => {
  const offenses = await check(path.resolve(__dirname, '..', 'theme'));
  const sev = ['error', 'warning', 'info'];
  for (const o of offenses) console.log(`${sev[o.severity] || o.severity} ${o.check} ${o.uri.split('/theme/')[1]}:${o.start?.line ?? ''} ${o.message}`);
  const errors = offenses.filter(o => o.severity === 0).length;
  console.log(`\n${offenses.length} offenses (${errors} errors)`);
  process.exit(errors ? 1 : 0);
})();
