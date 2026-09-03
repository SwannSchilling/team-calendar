// @ts-check
import { defineConfig, fontProviders } from 'astro/config';
import glsl from 'vite-plugin-glsl';

// https://astro.build/config
export default defineConfig({
  site: 'https://ibaliqbal.github.io/codrops-barbajs-page-transition',
  base: '/codrops-barbajs-page-transition/',
  vite: {
    plugins: [glsl()],
    build: {
      rollupOptions: {
        output: {
          manualChunks(id) {
            if (id.includes('node_modules')) {
              if (id.includes('three')) return 'three';
              return 'vendor';
            }
          },
        },
      },
    },
  },
  devToolbar: {
    enabled: false,
  },
});
