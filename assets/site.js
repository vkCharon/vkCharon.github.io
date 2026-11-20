const root = document.documentElement;
const theme = document.querySelector('#theme');
theme.hidden = false;
theme.setAttribute('aria-pressed', String(root.dataset.theme === 'light'));
theme.addEventListener('click', () => {
  root.dataset.theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
  theme.setAttribute('aria-pressed', String(root.dataset.theme === 'light'));
  try { localStorage.setItem('chr-theme', root.dataset.theme); }
  catch (error) { console.info('Theme preference not saved:', error.name); }
});

const toc = document.querySelector('.toc');
if (toc) {
  const headings = document.querySelectorAll('.prose h2[id], .prose h3[id]');
  for (const heading of headings) {
    const item = document.createElement('li');
    const link = document.createElement('a');
    link.href = '#' + encodeURIComponent(heading.id);
    link.textContent = heading.textContent;
    item.append(link);
    toc.querySelector('ol').append(item);
  }
  toc.hidden = headings.length === 0;
}

const form = document.querySelector('.filters');
if (form) {
  const { q, category, tag } = form.elements;
  const clean = value => value.normalize('NFKC').toLowerCase().trim();
  const cards = Array.from(document.querySelectorAll('[data-entry]'), element => {
    const tags = JSON.parse(element.dataset.tags);
    return { element, tags, text: clean(element.textContent + ' ' + tags.join(' ')) };
  });
  const fields = [q, category, tag];
  const params = new URLSearchParams(location.search);
  for (const field of fields) field.value = params.get(field.name) || '';
  function filter(updateUrl) {
    let visible = 0;
    for (const { element, tags, text } of cards) {
      element.hidden = !text.includes(clean(q.value)) ||
        Boolean(category.value && element.dataset.category !== category.value) ||
        Boolean(tag.value && !tags.includes(tag.value));
      if (!element.hidden) visible++;
    }
    document.querySelector('#count').textContent = `共 ${visible} 篇文章`;
    document.querySelector('#empty').hidden = visible !== 0;
    if (updateUrl) {
      const url = new URL(location.href);
      for (const field of fields) {
        if (field.value) url.searchParams.set(field.name, field.value);
        else url.searchParams.delete(field.name);
      }
      history.replaceState(null, '', url);
    }
  }
  form.hidden = false;
  filter(false);
  form.addEventListener('input', () => filter(true));
  form.addEventListener('submit', event => { event.preventDefault(); filter(true); });
  form.addEventListener('reset', () => requestAnimationFrame(() => filter(true)));
}
