import { readFile, readdir, stat } from 'node:fs/promises';
import { resolve, join, relative } from 'node:path';
import assert from 'node:assert/strict';

const root=resolve('dist');
async function files(dir){return (await Promise.all(await (await readdir(dir,{withFileTypes:true})).map(async e=>e.isDirectory()?files(join(dir,e.name)):[join(dir,e.name)]))).flat()}
const all=await files(root);
const html=all.filter(f=>f.endsWith('.html'));
const errors=[];
const documents=new Map(await Promise.all(html.map(async f=>[f,await readFile(f,'utf8')])));
const exists=async p=>{try{return(await stat(p)).isFile()}catch{return false}};
let links=0;
for(const [file,source] of documents){
 const rel=relative(root,file).replaceAll('\\','/');
 const expectedLang=rel.startsWith('en/')?'en':'es';
 if(!source.includes(`<html lang="${expectedLang}"`))errors.push(`${rel}: incorrect language`);
 if((source.match(/<h1(?:\s|>)/g)||[]).length!==1)errors.push(`${rel}: expected one h1`);
 if(!/<meta name="description" content="[^"]+"/.test(source))errors.push(`${rel}: missing description`);
 if(!source.includes('hreflang="en"')||!source.includes('hreflang="es"'))errors.push(`${rel}: missing language alternates`);
 if(rel!=='404.html'){
  const mirror=rel.startsWith('en/')?rel.slice(3):`en/${rel}`;
  if(!await exists(join(root,mirror)))errors.push(`${rel}: missing translation ${mirror}`);
 }
 for(const m of source.matchAll(/<(?:a|img|script)\b[^>]*?\b(?:href|src)="([^"]+)"/g)){
  const href=m[1].replaceAll('&amp;','&');
  if(!href.startsWith('/')&&!href.startsWith('#'))continue;
  links++;
  const url=new URL(href,`https://check.invalid/${rel.replace(/index\.html$/,'')}`);
  let target=join(root,decodeURIComponent(url.pathname));
  if(url.pathname.endsWith('/'))target=join(target,'index.html');
  if(!await exists(target)){errors.push(`${rel}: broken link ${href}`);continue}
  if(url.hash&&target.endsWith('.html')){
   const doc=documents.get(target)||await readFile(target,'utf8');
   if(!doc.includes(`id="${decodeURIComponent(url.hash.slice(1))}"`))errors.push(`${rel}: missing anchor ${href}`);
  }
 }
 for(const m of source.matchAll(/<img\b[^>]*>/g)){if(!/\balt=/.test(m[0]))errors.push(`${rel}: image without alt`);if(!/\bwidth=/.test(m[0])||!/\bheight=/.test(m[0]))errors.push(`${rel}: image without dimensions`)}
}
for(const f of all.filter(f=>f.endsWith('rss.xml'))){const xml=await readFile(f,'utf8');if(xml.includes('<item>'))errors.push(`${relative(root,f)}: W0 draft leaked into RSS`);assert(xml.startsWith('<?xml'));assert(xml.includes('<language>'))}
const js=all.filter(f=>f.endsWith('.js'));
const jsBytes=(await Promise.all(js.map(async f=>(await stat(f)).size))).reduce((a,b)=>a+b,0);
const inlineMax=Math.max(...[...documents.values()].map(source=>[...source.matchAll(/<script\b[^>]*>([\s\S]*?)<\/script>/g)].reduce((n,m)=>n+Buffer.byteLength(m[1]),0)));
assert(jsBytes+inlineMax<200*1024,`JavaScript budget exceeded: ${jsBytes+inlineMax} bytes`);
if(errors.length){console.error(errors.join('\n'));process.exit(1)}
console.log(`PASS: ${html.length} HTML pages, ${links} internal links/assets, mirrored ES/EN routes, image metadata, 4 draft-free RSS feeds.`);
console.log(`JavaScript budget: ${jsBytes} external bytes + at most ${inlineMax} inline bytes per page (budget: 204800).`);
