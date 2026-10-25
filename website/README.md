# 101 Agents Games — website

Prototipo privado W0, construido con Astro a partir del plan del sitio v0.1 y del documento maestro v0.7. No equivale al lanzamiento público W1 ni a una build del juego.

## Desarrollo

Requiere Node.js 22.23.4+ o 24. Ejecutar desde esta carpeta:

```sh
npm ci
npm run dev
npm run build
npm run check
npm run preview
```

`npm run dev` sirve en http://127.0.0.1:4321. El resultado estático está en `dist/`. No necesita backend ni claves para navegar.

## Contenido

- `src/data/estado.yaml`: estado, fecha de referencia y servicios opcionales. Los enlaces externos permanecen nulos hasta confirmación.
- `src/data/roadmap.yaml`: fases 0–7, periodos, entregables y puertas de salida en ES/EN; validación Zod al compilar.
- `src/data/site.ts`: textos compartidos, rutas, épocas, sistemas y FAQ.
- `src/content/diarios/{es,en}/*.mdx`: artículos con metadatos y estado editorial.
- `src/content/cambios/*.md`: entradas bilingües de diseño, juego y sitio.
- `src/content.config.ts`: esquemas de las colecciones. Los datos inválidos detienen la build.
- `src/components/SectionPage.astro`: vistas de las secciones; las etapas W2–W4 están marcadas como futuras.
- `public/images/atlas.svg`: atlas esquemático original, sin fronteras históricas verificadas. La misma imagen se presenta con tratamientos cartográficos por época.

Todas las rutas tienen espejo `/en/`. La navegación y el contenido están generados como HTML estático y se pueden leer sin JavaScript. JS se limita a menú móvil, tema y filtros. RSS en `/diarios/rss.xml`, `/cambios/rss.xml` y espejos en inglés; excluye borradores. Al aprobar contenido, actualizar el test de RSS para comprobar que solo aparezcan entradas con `status: published`.

## Privacidad e integraciones

No se incluye analítica, cookies de seguimiento, fuentes externas ni formularios que recojan correos. El tema utiliza almacenamiento local opcional. La infraestructura privada de Sites puede gestionar autenticación y registros técnicos fuera de este código.

El boletín muestra un estado cerrado honesto. Para activarlo: seleccionar proveedor, verificar doble opt-in, completar responsable/contacto/retención/baja y añadir su formulario alojado a `newsletterUrl`. No basta con cambiar la etiqueta del botón.

## Verificación

`npm run check` inspecciona HTML compilado, enlaces y anclas locales, espejos ES/EN, encabezados, metadatos, imágenes, exclusión de borradores de RSS y presupuesto de JS. CI ejecuta compilación, validación y Lighthouse con objetivo 95 para rendimiento, accesibilidad y buenas prácticas. SEO queda como advertencia durante W0 porque `robots.txt` bloquea intencionadamente la indexación; debe convertirse en requisito 95 al aprobar W1.

## Publicación

La identidad privada de Sites está en `.openai/hosting.json`; no crear otra para el mismo sitio. Ese archivo se queda en local (lo ignora el `.gitignore` de la raíz porque el repositorio es público). El helper del plugin empaqueta `dist/` junto al manifiesto y sincroniza el código. `astro.config.mjs` contiene el origen de revisión privado; cambiarlo al dominio definitivo antes de una publicación pública y regenerar RSS/sitemap/metadatos.

El código también puede desplegarse como estático en Cloudflare Pages con `npm run build` y salida `dist`, una vez conectada una cuenta y aprobado el lanzamiento.

## Pendientes humanos antes de W1

- Verificar dominio, marca y cuentas; confirmar identidad visual.
- Aprobar textos, traducciones, hoja de ruta y contenido histórico.
- Aportar titular legal, jurisdicción y contacto; revisar políticas.
- Elegir y verificar el proveedor de boletín; analítica sin cookies solo si se decide usarla.
- Exigir revisión en la protección de rama. El propietario de `website/` ya está asignado en el `.github/CODEOWNERS` de la raíz del repositorio.
- Ejecutar la prueba de comprensión con cinco personas y comprobar 4/5 resultados correctos.
- Completar recursos y permisos del kit de prensa antes de anunciarlo como definitivo.
- Abrir indexación y acceso público solo después de estas decisiones.

Las fechas orientativas del juego y las etapas futuras no se marcan como cumplidas por haber construido sus páginas.
