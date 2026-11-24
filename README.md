# UltraVena project site

The public site for UltraVena, an ultrasound-guided cannulation system for dialysis (Team 7, Penn ESE senior design).

## How it is organised

| Folder | What it holds |
| --- | --- |
| `content/` | The pages, as Markdown files, plus `home.json` for the overview page |
| `docs/assets/` | Stylesheet, images, PDFs, CAD download and the 3D model files |
| `build.py` | Turns `content/` into the pages in `docs/` |
| `docs/` | The finished site. GitHub Pages serves this folder. The `.html` files in it are generated, so edit `content/` instead. |

## Changing something

1. Edit the Markdown file in `content/` (or `home.json` for the overview page).
2. Run `python3 build.py` (needs `pip install markdown`).
3. Commit and push. The live site updates a minute or so later.

To log a change, add a section at the top of `content/updates.md` in the form `## 24 Nov 2026 · Title` followed by a paragraph. The three newest entries appear on the overview page.

To add a page, create a new Markdown file in `content/` with the same header block as the others (`title`, `nav`, `order`, `summary`, `updated`). It appears in the menu automatically.

## Turning on GitHub Pages (once)

In the repository on GitHub, open Settings, then Pages. Under "Build and deployment" choose "Deploy from a branch", pick the `main` branch and the `/docs` folder, and save.
