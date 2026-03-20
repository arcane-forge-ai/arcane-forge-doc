import type {Config} from '@docusaurus/types';
import type {Preset} from '@docusaurus/preset-classic';

const config: Config = {
  title: 'Arcane Forge Docs',
  tagline: 'Your Game AI Framework Documentation',
  url: 'https://docs.arcaforge.ai',
  baseUrl: '/',
  favicon: 'img/logo.svg',
  organizationName: 'arcane-forge',
  projectName: 'arcane-forge-docs',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },
  future: {
    experimental_faster: true,
  },
  themes: [],
  plugins: [
    [
      '@cmfcmf/docusaurus-search-local',
      {
        indexDocs: true,
        indexPages: true,
        language: 'en',
        highlightSearchTermsOnTargetPage: true,
        searchResultContextMaxLength: 120,
      },
    ],
  ],
  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars'),
          editUrl: undefined,
          routeBasePath: '/docs',
          showLastUpdateTime: true,
        },
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
        sitemap: {
          changefreq: 'weekly',
          priority: 0.5,
        },
      } satisfies Preset.Options,
    ],
  ],
};

export default config;
