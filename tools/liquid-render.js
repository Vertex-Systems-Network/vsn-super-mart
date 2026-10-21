const { Liquid } = require('liquidjs');
const fs = require('fs');
const engine = new Liquid();
const src = fs.readFileSync(process.argv[2], 'utf8').replace(/{%\s*doc\s*%}[\s\S]*?{%\s*enddoc\s*%}/, '');
const p = JSON.parse(process.argv[3]);
engine.parseAndRender(src, p).then(css => { process.stdout.write(css); });
