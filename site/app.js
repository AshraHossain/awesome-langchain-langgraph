// Searchable directory. Loads the same resources.json the README is built from.
const STAGE_EMOJI = { build: "🔨", observe: "🔭", evaluate: "📊", deploy: "🚀" };

const state = { data: null, q: "", stages: new Set(), group: "all" };

const $ = (sel) => document.querySelector(sel);

async function init() {
  try {
    const res = await fetch("resources.json", { cache: "no-cache" });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    state.data = await res.json();
  } catch (e) {
    $("#results").innerHTML = `<p class="empty">Could not load resources.json (${e.message}).<br>Run <code>python scripts/build_site.py</code> first.</p>`;
    return;
  }
  buildFilters();
  wireSearch();
  render();
}

function buildFilters() {
  const lc = $("#lifecycle-filters");
  for (const stage of Object.keys(state.data.lifecycle_stages)) {
    const b = document.createElement("button");
    b.className = "chip";
    b.textContent = `${STAGE_EMOJI[stage] || ""} ${stage}`;
    b.title = state.data.lifecycle_stages[stage];
    b.onclick = () => {
      state.stages.has(stage) ? state.stages.delete(stage) : state.stages.add(stage);
      b.classList.toggle("active");
      render();
    };
    lc.appendChild(b);
  }
  const gf = $("#group-filters");
  for (const [label, value] of [["All", "all"], ["Ecosystem", "ecosystem"], ["Community", "community"]]) {
    const b = document.createElement("button");
    b.className = "chip" + (value === "all" ? " active" : "");
    b.textContent = label;
    b.onclick = () => {
      state.group = value;
      gf.querySelectorAll(".chip").forEach((c) => c.classList.remove("active"));
      b.classList.add("active");
      render();
    };
    gf.appendChild(b);
  }
}

function wireSearch() {
  const input = $("#search");
  input.addEventListener("input", (e) => { state.q = e.target.value.trim().toLowerCase(); render(); });
  document.addEventListener("keydown", (e) => {
    if (e.key === "/" && document.activeElement !== input) { e.preventDefault(); input.focus(); }
  });
}

function matches(res) {
  if (state.stages.size && !res.lifecycle.some((s) => state.stages.has(s))) return false;
  if (!state.q) return true;
  return (res.name + " " + res.description).toLowerCase().includes(state.q);
}

function highlight(text) {
  if (!state.q) return escapeHtml(text);
  const i = text.toLowerCase().indexOf(state.q);
  if (i < 0) return escapeHtml(text);
  return escapeHtml(text.slice(0, i)) + "<mark>" + escapeHtml(text.slice(i, i + state.q.length)) + "</mark>" + escapeHtml(text.slice(i + state.q.length));
}

function escapeHtml(s) {
  return s.replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}

function render() {
  const root = $("#results");
  root.innerHTML = "";
  let shown = 0;
  for (const cat of state.data.categories) {
    if (state.group !== "all" && cat.group !== state.group) continue;
    const visible = cat.resources.filter(matches);
    if (!visible.length) continue;
    shown += visible.length;

    const section = document.createElement("section");
    section.className = "category";
    section.innerHTML = `<h2>${escapeHtml(cat.title)}</h2><p class="cat-desc">${escapeHtml(cat.description)}</p>`;
    const cards = document.createElement("div");
    cards.className = "cards";
    for (const res of visible) {
      const card = document.createElement("article");
      card.className = "card";
      const stages = res.lifecycle.map((s) => `<span class="tag stage">${STAGE_EMOJI[s] || ""} ${s}</span>`).join("");
      const official = res.official ? `<span class="tag official">⭐ official</span>` : "";
      card.innerHTML =
        `<a class="title" href="${escapeHtml(res.url)}" target="_blank" rel="noopener">${highlight(res.name)}</a>` +
        `<p class="desc">${highlight(res.description)}</p>` +
        `<div class="meta">${official}${stages}</div>`;
      cards.appendChild(card);
    }
    section.appendChild(cards);
    root.appendChild(section);
  }
  if (!shown) root.innerHTML = `<p class="empty">No resources match your filters.</p>`;
  $("#count").textContent = `${shown} resource${shown === 1 ? "" : "s"} shown`;
}

init();
