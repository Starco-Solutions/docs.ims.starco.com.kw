(() => {
  const menu = document.querySelector('[data-mobile-nav]');
  const sidebar = document.querySelector('.sidebar');
  if (menu && sidebar) {
    const primary = document.querySelector('.topnav');
    if (primary) {
      const categories = primary.cloneNode(true);
      categories.className = 'compact-primary';
      categories.setAttribute('aria-label', 'Primary categories');
      sidebar.prepend(categories);
    }
    sidebar.id = sidebar.id || 'documentation-navigation';
    menu.setAttribute('aria-controls', sidebar.id);
    menu.setAttribute('aria-expanded', 'false');
    menu.addEventListener('click', () => {
      const open = sidebar.classList.toggle('open');
      menu.setAttribute('aria-expanded', String(open));
    });
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && sidebar.classList.contains('open')) {
        sidebar.classList.remove('open');
        menu.setAttribute('aria-expanded', 'false');
        menu.focus();
      }
    });
  }

  const search = document.querySelector('[data-doc-search]');
  if (!search) return;

  const main = document.querySelector('main');
  let searchItems = [...document.querySelectorAll('[data-search-item]')];

  // Search topic content blocks; retain headings so filtered matches keep section context.
  if (!searchItems.length && main) {
    searchItems = [...main.querySelectorAll('p, li, tr, .callout, .doc-link')];
  }

  const empty = document.querySelector('[data-search-empty]');

  search.addEventListener('input', () => {
    const q = search.value.trim().toLowerCase();
    document.body.classList.toggle('searching', !!q);
    let visible = 0;

    searchItems.forEach(el => {
      const hay = (el.getAttribute('data-search-item') || el.textContent || '').toLowerCase();
      const hit = !q || hay.includes(q);
      el.classList.toggle('search-hidden', !hit);
      if (hit && q) visible++;
    });

    if (empty) empty.classList.toggle('visible', !!q && visible === 0);
  });
})();
