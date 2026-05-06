# تقرير العمليات التشغيلية لمشروع بطاقات نسك (موسم الحج ١٤٤٧)

**Operational Report — Nusuk Cards Project**

A fully self-contained, interactive HTML report for managing and visualizing Nusuk card operations. No server or backend required.

## Features

- **Interactive report** with dynamic data entry fields, searchable dropdowns, and auto-calculated statistics.
- **Data visualizations** powered by Chart.js:
  - Horizontal bar chart for employee trip distribution.
  - Donut chart with KPI cards for trip statistics.
- **Print / PDF export** with proper multi-page A4 layout.
- **Mobile responsive** — works on phones, tablets, and desktops.
- **Fully offline** — all assets are embedded; only Chart.js is loaded from CDN.

---

## Deployment on GitHub Pages

### Option 1 — Automatic (GitHub Actions)

1. Push this repository to GitHub.
2. GitHub Actions will automatically deploy the `index.html` to the `gh-pages` branch on every push to `main`.
3. Enable GitHub Pages in your repository settings:
   - Go to **Settings → Pages**.
   - Set **Source** to `gh-pages` branch, root `/`.
4. Your report will be live at: `https://mofaq-01.github.io/Hajj-1447-Nusuk/`

---

## Local Usage

Simply open `index.html` in any modern browser — no installation required.

```bash
# Open directly in browser
open index.html        # macOS
xdg-open index.html    # Linux
start index.html       # Windows
```

---

## File Structure

```
.
├── index.html              # Main report file (fully self-contained)
├── README.md               # This file
└── .github/
    └── workflows/
        └── deploy.yml      # GitHub Actions auto-deploy workflow
```


## Credits
Developed by Tamim Al Faiz for
**شجميع الحقوق محفوظة — شركة رحلات ومنافع للسياحة — المدينة المنورة © 2026**
