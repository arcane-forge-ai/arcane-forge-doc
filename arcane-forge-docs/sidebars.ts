import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  docs: [
    {
      type: 'category',
      label: 'Getting Started',
      collapsed: false,
      items: ['getting-started/intro', 'getting-started/install'],
    },
    {
      type: 'category',
      label: 'Guide',
      collapsed: false,
      items: ['guide/overview'],
    },
    {
      type: 'category',
      label: 'API',
      collapsed: false,
      items: ['api/reference'],
    },
    {
      type: 'category',
      label: 'FAQ',
      collapsed: false,
      items: ['faq/common-questions'],
    },
  ],
};

export default sidebars;
