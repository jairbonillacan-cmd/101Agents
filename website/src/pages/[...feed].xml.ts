import { getCollection } from 'astro:content';
import { path } from '../data/site';
export function getStaticPaths(){return ['es','en'].flatMap(lang=>['diarios','cambios'].map(channel=>({params:{feed:`${lang==='en'?'en/':''}${channel}/rss`},props:{lang,channel}})))}
const escape=(s:string)=>s.replace(/[<>&"']/g,c=>({'<':'&lt;','>':'&gt;','&':'&amp;','"':'&quot;',"'":'&apos;'}[c]!));
export async function GET({ props, site }){
 const {lang,channel}=props;
 const entries=channel==='diarios'?(await getCollection('diaries')).filter(e=>e.data.lang===lang&&e.data.status==='published'):(await getCollection('changes')).filter(e=>e.data.status==='published');
 const title=`101 Agents Games · ${channel==='diarios'?(lang==='es'?'Diarios':'Dev diaries'):(lang==='es'?'Cambios':'Changelog')}`;
 const items=entries.map(e=>{const url=new URL(path(lang,channel==='diarios'?`diarios/${e.data.translationKey}`:'cambios'),site).href;const id=channel==='diarios'?url:`${url}#${e.id}`;return `<item><title>${escape(e.data.title)}</title><link>${url}</link><guid isPermaLink="${channel==='diarios'}">${id}</guid><pubDate>${new Date(`${e.data.date}T12:00:00Z`).toUTCString()}</pubDate><description>${escape(channel==='diarios'?e.data.description:e.data.summary[lang])}</description></item>`}).join('');
 return new Response(`<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>${escape(title)}</title><link>${new URL(path(lang,channel),site)}</link><description>${lang==='es'?'Solo publicaciones aprobadas. Los borradores quedan fuera de este canal.':'Approved publications only. Drafts are excluded from this feed.'}</description><language>${lang}</language>${items}</channel></rss>`,{headers:{'Content-Type':'application/rss+xml; charset=utf-8'}});
}
