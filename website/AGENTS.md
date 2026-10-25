# Website instructions

This folder contains the Astro website for 101 Agents Games, inside the public `101Agents` monorepo. It is independent of the Rust engine; the root `AGENTS.md` rules also apply. Source: website plan v0.1 and master design document v0.7 (both in `docs/master/`). CI lives in `.github/workflows/website.yml` at the repository root.

- Keep the default Spanish routes and their `/en/` mirrors. The working title must remain explicitly provisional.
- Edit roadmap and project status in `src/data/*.yaml`; validate with the shared schemas. Do not mark milestones complete without evidence.
- Content is a draft until human editorial approval. Historical details must be checked against the historical bible; do not invent releases, metrics, contacts, prices, dates or links.
- Keep future-stage pages visibly labeled. Draft diaries and changes must not enter public RSS feeds.
- Public launch requires human review of copy, translations, legal information, roadmap and release claims. Private review previews are permitted. Do not merge your own PR.
- Never collect newsletter addresses until the provider and privacy details are configured and double opt-in is verified. Do not create fake subscription success states.
- Preserve no-JavaScript reading/navigation and reduced-motion behavior. Keep local fonts and lightweight scripts. Test keyboard access and small screens.
- Run `npm run build` and `npm run check`. Run representative browser and Lighthouse checks after visual or behavior changes. Keep results honest.
- Do not commit credentials, runtime state, node_modules or build output. Preserve Site identity and audience; `.openai/hosting.json` stays local and is git-ignored because the repository is public.
