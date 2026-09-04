import gsap from 'gsap';
import WebGLPageTransition from './components/webgl-page-transition';
import { select, selectAll } from './utils';

class App {
  constructor() {
    const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    this.splitMotionText();
    this.runLoadIn(reduced);
    this.initReveal();
    this.initScrollSpy();
    this.initInventory();
    this.initDiff();
  }

  /* ---------- motion text (lightweight word split, no SplitText) ---------- */
  splitMotionText() {
    selectAll('[data-mtext]').forEach((el) => {
      const words = el.textContent.trim().split(/\s+/);
      el.textContent = '';
      words.forEach((w, i) => {
        const outer = document.createElement('span');
        outer.className = 'word';
        const inner = document.createElement('span');
        inner.textContent = w;
        outer.appendChild(inner);
        el.appendChild(outer);
        if (i < words.length - 1) el.appendChild(document.createTextNode(' '));
      });
      el.classList.add('mtext');
    });
  }

  /* ---------- signature noise load-in (the old transition, as a one-shot) ---------- */
  runLoadIn(reduced) {
    const animateText = () => {
      gsap.to('.mtext .word > span', {
        y: 0,
        duration: 0.9,
        stagger: 0.055,
        ease: 'power3.out',
      });
      gsap.from('.hero__sub, .hero__ctas, .hero__stats, .hero__visual', {
        autoAlpha: 0,
        y: 18,
        duration: 0.9,
        stagger: 0.09,
        delay: 0.25,
        ease: 'power2.out',
      });
    };

    if (reduced || !window.WebGLRenderingContext) {
      animateText();
      return;
    }

    try {
      const webgl = new WebGLPageTransition();
      gsap.set(webgl.material.uniforms.uProgress, { value: -0.75 });
      gsap.set('#webgl', { visibility: 'visible', autoAlpha: 1 });

      let rafId = 0;
      const loop = () => {
        webgl.render();
        rafId = requestAnimationFrame(loop);
      };
      loop();

      gsap.delayedCall(0.18, () => {
        gsap.to(webgl.material.uniforms.uProgress, {
          value: 1.5,
          duration: 1.5,
          ease: 'power2.inOut',
          onComplete: () => {
            cancelAnimationFrame(rafId);
            gsap.set('#webgl', { autoAlpha: 0, visibility: 'hidden' });
          },
        });
        animateText();
      });
    } catch (e) {
      // WebGL unavailable — fall back to text-only reveal
      animateText();
    }
  }

  /* ---------- scroll reveal ---------- */
  initReveal() {
    const els = selectAll('[data-reveal]');
    if (!('IntersectionObserver' in window)) {
      els.forEach((el) => el.classList.add('is-revealed'));
      return;
    }
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-revealed');
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: '0px 0px -8% 0px' }
    );
    els.forEach((el) => io.observe(el));
  }

  /* ---------- nav scroll-spy ---------- */
  initScrollSpy() {
    const links = selectAll('.frame__link[data-spy]');
    const sections = [...links].map((l) => document.getElementById(l.dataset.spy)).filter(Boolean);
    if (!('IntersectionObserver' in window) || !sections.length) return;
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          links.forEach((l) => l.classList.toggle('is-active', l.dataset.spy === entry.target.id));
        });
      },
      { rootMargin: '-30% 0px -60% 0px' }
    );
    sections.forEach((s) => io.observe(s));
  }

  /* ---------- differentiator expand/collapse ---------- */
  initDiff() {
    selectAll('.diff').forEach((btn) => {
      btn.addEventListener('click', () => {
        const open = btn.classList.toggle('is-open');
        btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      });
    });
  }

  /* ---------- inventory filters + row expand ---------- */
  initInventory() {
    const table = select('#inv-table');
    if (!table) return;
    const rows = selectAll('#inv-table .inv-row');
    const search = select('#inv-search');
    const cat = select('#inv-cat');
    const statusBtns = selectAll('.inv-filter[data-status]');
    const roleBtns = selectAll('.inv-filter[data-role]');
    const count = select('#inv-count');
    const empty = select('#inv-empty');

    const state = { q: '', cat: '', statuses: new Set(), roles: new Set() };

    const apply = () => {
      let shown = 0;
      rows.forEach((row) => {
        const status = row.dataset.status.split(' ');
        const roles = row.dataset.roles.split(' ');
        const ok =
          (!state.q || row.dataset.text.includes(state.q)) &&
          (!state.cat || row.dataset.cat === state.cat) &&
          (state.statuses.size === 0 || status.some((s) => state.statuses.has(s))) &&
          (state.roles.size === 0 || roles.some((r) => state.roles.has(r)));
        row.classList.toggle('is-hidden', !ok);
        if (ok) shown += 1;
      });
      const isDe = document.documentElement.lang === 'de';
      count.textContent = isDe
        ? `Zeige ${shown} von ${rows.length} Funktionen`
        : `Showing ${shown} of ${rows.length} features`;
      empty.style.display = shown === 0 ? 'block' : 'none';
    };

    search.addEventListener('input', () => {
      state.q = search.value.trim().toLowerCase();
      apply();
    });

    cat.addEventListener('change', () => {
      state.cat = cat.value;
      apply();
    });

    const wire = (btns, set) => {
      btns.forEach((btn) => {
        btn.addEventListener('click', () => {
          const key = btn.dataset.status || btn.dataset.role;
          const on = set.has(key);
          on ? set.delete(key) : set.add(key);
          btn.classList.toggle('is-on', !on);
          btn.setAttribute('aria-pressed', !on ? 'true' : 'false');
          apply();
        });
      });
    };
    wire(statusBtns, state.statuses);
    wire(roleBtns, state.roles);

    rows.forEach((row) => {
      const toggle = () => {
        const open = row.classList.toggle('is-open');
        row.setAttribute('aria-expanded', open ? 'true' : 'false');
      };
      row.addEventListener('click', toggle);
      row.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          toggle();
        }
      });
    });

    apply();
  }
}

document.addEventListener('DOMContentLoaded', () => {
  new App();
});
