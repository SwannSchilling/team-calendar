// @ts-check
import { defineConfig, fontProviders } from 'astro/config';
import glsl from 'vite-plugin-glsl';

// https://astro.build/config
export default defineConfig({
  site: 'https://SwannSchilling.github.io/team-calendar',
  base: '/team-calendar/',
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
