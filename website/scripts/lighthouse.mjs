import { createServer } from 'node:http';
import { readFile, stat, mkdir } from 'node:fs/promises';
import { resolve, extname, sep } from 'node:path';
import { spawn } from 'node:child_process';
const root=resolve('dist');
const mime={'.html':'text/html','.css':'text/css','.js':'text/javascript','.svg':'image/svg+xml','.png':'image/png','.xml':'application/xml','.txt':'text/plain','.zip':'application/zip'};
const server=createServer(async(req,res)=>{try{let pathname=decodeURIComponent(new URL(req.url,'http://localhost').pathname);let file=resolve(root,'.'+pathname);if(file!==root&&!file.startsWith(root+sep)){res.writeHead(403);res.end();return}if((await stat(file)).isDirectory())file=resolve(file,'index.html');res.setHeader('Content-Type',mime[extname(file)]||'application/octet-stream');res.end(await readFile(file))}catch{res.writeHead(404);res.end('Not found')}});
await new Promise(r=>server.listen(0,'127.0.0.1',r));
const port=server.address().port;
await mkdir('.lighthouseci',{recursive:true});
let failed=false;
try{
 for(const [slug,path] of [['home','/'],['english','/en/'],['game','/juego/'],['roadmap','/hoja-de-ruta/']]){
  const output=resolve('.lighthouseci',slug);
  await new Promise((ok,no)=>{const c=spawn(process.execPath,['node_modules/lighthouse/cli/index.js',`http://127.0.0.1:${port}${path}`,'--output=json','--output=html',`--output-path=${output}`,'--chrome-flags=--headless --no-sandbox --disable-dev-shm-usage','--quiet'],{stdio:'inherit',env:process.env});c.on('exit',code=>code===0?ok():no(new Error(`Lighthouse exited ${code}`)));c.on('error',no)});
  const report=JSON.parse(await readFile(output+'.report.json','utf8'));
  const scores=Object.fromEntries(Object.entries(report.categories).map(([key,val])=>[key,Math.round(val.score*100)]));
  console.log(JSON.stringify({page:path,scores,lcp:report.audits['largest-contentful-paint'].numericValue}));
  for(const category of ['performance','accessibility','best-practices'])if(scores[category]<95)failed=true;
  if(scores.seo<95)console.warn(`${path}: SEO below W1 target; W0 deliberately blocks indexing.`);
 }
}finally{server.close()}
if(failed)process.exitCode=1;
