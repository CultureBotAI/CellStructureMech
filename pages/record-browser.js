/* Enhance the fully rendered catalogue without a fetch or a framework. */
(function () {
  'use strict';
  var form = document.getElementById('record-filters');
  if (!form) return;
  var query = document.getElementById('record-query');
  var category = document.getElementById('record-category');
  var kind = document.getElementById('record-kind');
  var status = document.getElementById('record-status');
  var sort = document.getElementById('record-sort');
  var count = document.getElementById('record-count');
  var empty = document.getElementById('record-empty');
  var records = Array.from(document.querySelectorAll('#record-table tbody tr')).map(function (row, idx) {
    return {
      row: row,
      idx: idx,
      label: (row.dataset && row.dataset.label) || row.textContent.toLowerCase(),
      id: (row.dataset && row.dataset.id) || '',
      text: (row.textContent + ' ' + ((row.dataset && row.dataset.synonyms) || '')).toLowerCase()
    };
  });
  function syncUrl() {
    if (!window.history || !window.history.replaceState || !window.location) return;
    var url = new URL(window.location.href);
    var q = query.value.trim();
    if (q) url.searchParams.set('q', q); else url.searchParams.delete('q');
    if (category && category.value) url.searchParams.set('category', category.value); else url.searchParams.delete('category');
    if (kind && kind.value) url.searchParams.set('kind', kind.value); else url.searchParams.delete('kind');
    if (status && status.value) url.searchParams.set('status', status.value); else url.searchParams.delete('status');
    if (sort && sort.value) url.searchParams.set('sort', sort.value); else url.searchParams.delete('sort');
    window.history.replaceState(null, '', url);
  }
  function apply() {
    syncUrl();
    if (sort && records.length) {
      var mode = sort.value || '';
      var ordered = records.slice().sort(function (a, b) {
        if (mode === 'label-asc') return a.label.localeCompare(b.label) || (a.idx - b.idx);
        if (mode === 'label-desc') return b.label.localeCompare(a.label) || (a.idx - b.idx);
        if (mode === 'id-asc') return a.id.localeCompare(b.id) || (a.idx - b.idx);
        if (mode === 'kind-asc') return (a.row.dataset.kind || '').localeCompare(b.row.dataset.kind || '') || a.label.localeCompare(b.label);
        if (mode === 'status-asc') return (a.row.dataset.status || '').localeCompare(b.row.dataset.status || '') || a.label.localeCompare(b.label);
        // The rendered order: grouped by category, then file name. It was
        // labelled "Label (A-Z)" though it is not alphabetical across groups.
        return a.idx - b.idx;
      });
      var parent = ordered[0].row && ordered[0].row.parentNode;
      if (parent && parent.appendChild) {
        ordered.forEach(function (item) { parent.appendChild(item.row); });
      }
    }
    var term = query.value.trim().toLowerCase();
    var visible = 0;
    records.forEach(function (record) {
      var match = record.text.indexOf(term) !== -1 &&
        (!category.value || record.row.dataset.category === category.value) &&
        (!kind.value || record.row.dataset.kind === kind.value) &&
        (!status || !status.value || record.row.dataset.status === status.value);
      record.row.hidden = !match;
      if (match) visible += 1;
    });
    count.textContent = visible + ' of ' + records.length + ' records shown';
    empty.hidden = visible !== 0;
  }
  form.addEventListener('submit', function (event) { event.preventDefault(); apply(); });
  form.addEventListener('input', apply);
  form.addEventListener('change', apply);
  // Native reset restores controls after the event has been dispatched.
  form.addEventListener('reset', function () { setTimeout(apply, 0); });
  form.hidden = false;
  if (window.location && window.location.search) {
    var params = new URLSearchParams(window.location.search);
    if (params.get('q')) query.value = params.get('q');
    if (category && params.get('category')) category.value = params.get('category');
    if (kind && params.get('kind')) kind.value = params.get('kind');
    if (status && params.get('status')) status.value = params.get('status');
    if (sort && params.get('sort')) sort.value = params.get('sort');
  }
  // pageshow fires after browser-restored controls, including reload-style Back.
  window.addEventListener('pageshow', apply);
  apply();
})();
