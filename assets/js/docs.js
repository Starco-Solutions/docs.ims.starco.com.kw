(() => {
  const menu = document.querySelector('[data-mobile-nav]');
  const sidebar = document.querySelector('.sidebar');
  if (menu && sidebar) {
    menu.addEventListener('click', () => sidebar.classList.toggle('open'));
  }

  const search = document.querySelector('[data-doc-search]');
  if (!search) return;

  const main = document.querySelector('main');
  let searchItems = [...document.querySelectorAll('[data-search-item]')];

  // On topic pages without explicit search cards, search the major content blocks.
  if (!searchItems.length && main) {
    searchItems = [...main.querySelectorAll('h2, p, li, tr, .callout, .doc-link')];
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
