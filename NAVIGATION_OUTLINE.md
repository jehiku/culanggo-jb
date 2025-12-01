# Navigation Sidebar Outline for GitHub Pages

This document shows what your navigation sidebar will look like when deployed.

## Visual Structure

```
┌─────────────────────────────────────────────┐
│  📚 My JupyterBook                          │
│  Kein Jake Culanggo                         │
│  [Logo]                                     │
├─────────────────────────────────────────────┤
│                                             │
│  🏠 Welcome                                 │ ← Root page (intro.md)
│                                             │
│  ┌─ 📖 LECTURES ─────────────────────────┐ │
│  │  ▼ Lecture 1                         │ │
│  │  ▼ Lecture 2                         │ │
│  │  ▼ Lecture 3                         │ │
│  │  ▼ Lecture 4                         │ │
│  │  ▼ Lecture 5                         │ │
│  │  ▼ Lecture 6                         │ │
│  └───────────────────────────────────────┘ │
│                                             │
│  ┌─ 🧪 LABS ─────────────────────────────┐ │
│  │  ▼ DL-Lab1                           │ │
│  │  ▼ DL-Lab2                           │ │
│  │  ▼ DL-Lab3                           │ │
│  │  ▼ DL-Lab4                           │ │
│  │  ▼ DL-Lab5                           │ │
│  │  ▼ DL-Lab6                           │ │
│  │  ▼ DL-Lab201                          │ │
│  │  ▼ Homework201                        │ │
│  └───────────────────────────────────────┘ │
│                                             │
│  ┌─ 📄 NARRATIVE REPORTS ────────────────┐ │
│  │  ▼ Phase 1                           │ │
│  │  ▼ Phase 2                           │ │
│  │  ▼ Phase 3                           │ │
│  └───────────────────────────────────────┘ │
│                                             │
│  ┌─ 📝 DEEP LEARNING BLOG POST ──────────┐ │
│  │  (empty - no chapters)                │ │
│  └───────────────────────────────────────┘ │
│                                             │
│  [Search icon]                              │
│  [GitHub icon]                              │
│  [Settings icon]                            │
└─────────────────────────────────────────────┘
```

## Detailed Breakdown

### Top Section
- **Title**: "My JupyterBook"
- **Author**: "Kein Jake Culanggo"
- **Logo**: Your logo.png file

### Main Navigation

1. **Welcome** (Root page)
   - This is your `intro.md` file
   - Always visible at the top
   - Contains the welcome message and table of contents

2. **📖 LECTURES** (Part 1)
   - Lecture 1 (`lectures/lesson1/lesson1`)
   - Lecture 2 (`lectures/lesson2/lesson2`)
   - Lecture 3 (`lectures/lesson3/lesson3`)
   - Lecture 4 (`lectures/lesson4/lesson4`)
   - Lecture 5 (`lectures/lesson5/lesson5`)
   - Lecture 6 (`lectures/lesson6/lesson6`)

3. **🧪 LABS** (Part 2)
   - DL-Lab1 (`labs/DL-Lab1`)
   - DL-Lab2 (`labs/DL-Lab2`)
   - DL-Lab3 (`labs/DL-Lab3`)
   - DL-Lab4 (`labs/DL-Lab4`)
   - DL-Lab5 (`labs/DL-Lab5`)
   - DL-Lab6 (`labs/DL-Lab6`)
   - DL-Lab201 (`labs/DL-Lab201`)
   - Homework201 (`labs/Homework201`)

4. **📄 NARRATIVE REPORTS** (Part 3)
   - Phase 1 (`narrative-reports/phase1`) - Links to Phase 1 PDF
   - Phase 2 (`narrative-reports/phase2`) - Links to Phase 2 PDF
   - Phase 3 (`narrative-reports/phase3`) - Links to Phase 3 PDF

5. **📝 DEEP LEARNING BLOG POST** (Part 4)
   - Currently empty (homework_201 is excluded)
   - This section will appear but have no chapters

## Notes

- **Exercises section**: Commented out (file not found)
- **Deep Learning Blog Post**: Empty because homework_201 is excluded
- Each part can be expanded/collapsed by clicking the section header
- The active page will be highlighted in the sidebar
- Icons may vary based on the Jupyter Book theme you're using

## How It Will Look in Browser

The sidebar will be:
- **Left side** of the page (or collapsible on mobile)
- **Sticky** - stays visible when scrolling
- **Expandable sections** - click to expand/collapse parts
- **Active page highlighted** - current page is bold/highlighted
- **Search functionality** - search icon at top/bottom
- **GitHub links** - repository and issue buttons

