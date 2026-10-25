import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
export default defineConfig({
  site: 'https://atlas-101-agents-games.silkycivet19.chatgpt.site',
  output: 'static',
  trailingSlash: 'always',
  i18n: { defaultLocale: 'es', locales: ['es', 'en'], routing: { prefixDefaultLocale: false } },
  integrations: [mdx(), sitemap({ i18n: { defaultLocale: 'es', locales: { es: 'es', en: 'en' } } })],
});
