# Arcane Forge Docs

This is the Docusaurus 3 documentation site for Arcane Forge.

## Getting started

```bash
npm install
npm run start
```

Open `http://localhost:3000/docs` to view the docs locally.

## Building for production

```bash
npm run build
npm run serve
```

The build output is generated in the `build/` directory.

## Deploying to Vercel

1. Push this project to your Git repository.
2. Create a new Vercel project and import the repository.
3. Use **Build Command** `npm run build` and **Output Directory** `build`.
4. Set **Install Command** to `npm install` (or `pnpm install` if you prefer pnpm).

## Notes

- Local search is powered by `@cmfcmf/docusaurus-search-local`.
- Update the placeholder docs in `docs/` as you build out content.
- Customize site navigation in `docusaurus.config.ts` and `sidebars.ts`.
