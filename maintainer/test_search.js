// Offline documentation-script checks using minimal DOM doubles, not IMS tests.
const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
function element(text) {
  const classes = new Set();
  return {textContent:text, classes, getAttribute:()=>null,
    classList:{toggle:(c,on)=>{if(on)classes.add(c);else classes.delete(c);}}};
}
for (const explicit of [false,true]) {
  const items=[element('Inventory balance'),element('Sales receipt')];
  const empty=element('');let onInput;
  const search={value:'',addEventListener:(event,fn)=>{assert.equal(event,'input');onInput=fn;}};
  const body=element('');
  const main={querySelectorAll:selector=>{assert.ok(!selector.split(', ').includes('h2'));return items;}};
  const document={body,querySelector:s=>({'[data-doc-search]':search,main,'[data-search-empty]':empty}[s]||null),querySelectorAll:()=>explicit?items:[]};
  vm.runInNewContext(fs.readFileSync('assets/js/docs.js','utf8'),{document});
  search.value=' inventory ';onInput();
  assert.equal(items[0].classes.has('search-hidden'),false);
  assert.equal(items[1].classes.has('search-hidden'),true);
  search.value='no-match';onInput();assert.ok(empty.classes.has('visible'));
  search.value='';onInput();assert.ok(items.every(x=>!x.classes.has('search-hidden')));
  assert.ok(!body.classes.has('searching'));assert.ok(!empty.classes.has('visible'));
}
console.log('PASS explicit and fallback search matching, empty result and reset (DOM doubles; no browser rendering)');
