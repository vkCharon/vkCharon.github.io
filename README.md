# ChR 平面誌

A Traditional Chinese field journal at <https://vkcharon.github.io/>. Read the [articles](https://vkcharon.github.io/posts/), browse the [case studies](https://vkcharon.github.io/projects/), or subscribe via [RSS](https://vkcharon.github.io/feed.xml).

## Repository analysis

The starting checkout contained only `README.md`. Pages was already enabled for `main` at `/` without a custom domain. No article database or article URLs needed migration. `main` received unrelated changes during implementation, so the clean `journal` branch is the site's source of truth. This preserves the public address without merging, overwriting, or publishing the later contents of `main`.

## Recommended architecture

GitHub Pages' native Jekyll build fits this repository better than introducing an Astro build and a second deployment pipeline. Markdown and Liquid generate standalone HTML, RSS and a sitemap. The reader needs no account, token, server, or JavaScript framework. JavaScript progressively adds local search, a heading-linked table of contents and a persistent theme control. Graphite is the first-visit theme; Canvas is opt-in. Navigation, posts and project pages remain usable without scripting.

Homepage activity is a **publication snapshot**, not a browser-side API feed: it shows the build time, the published revision when Pages supplies it, and links to repository activity. Project source links target the relevant code in this repository. No third-party activity widgets, analytics or remote font services are loaded.

## Folder structure

```text
_config.yml           Site metadata, routes, collections and plugins
_layouts/             Page shell and shared reading layout
components/           Reusable article card and reading-time estimate
_posts/               Dated Markdown articles → /posts/<slug>/
_projects/            Markdown case studies → /projects/<name>/
about/index.md        Biography, practice timeline and contact
posts/index.html      Searchable article index
projects/index.html   Portfolio index
assets/               Site CSS, JavaScript, fonts, favicon and share image
scripts/check.py      Offline check of generated routes, links and metadata
index.html            Homepage
404.html              Not-found page
feed.xml, robots.txt  Feed template and crawler entry point
Gemfile, Gemfile.lock Local preview dependencies
```

## Implementation steps

1. Retain the domain and native publishing method; introduce an explicit homepage in place of the README fallback.
2. Render the shell, typography, two themes, geometric artwork and reading layout using site-specific CSS. Only public, newly implemented site assets belong in Git.
3. Generate indexes and discovery metadata from articles and case studies. Article dates, labels and descriptions have a single source of truth.
4. Enhance the static archive with URL-addressable search and filters. Check keyboard interactions, mobile reflow, restored filters, the no-JavaScript reading path, feeds and canonical links.
5. Push to `journal`. Check the **Pages build and deployment** result before treating the work as published.

## Files created and modified

The site source and local build files in the tree above are new. Also new: `.gitignore` and the two open-font licenses under `assets/fonts/`. `README.md` is the only pre-existing file that changed. `_site/` is generated, not committed. GitHub provides the Pages workflow; no custom `.github/workflows` file or deployment secret is required.

## Complete source code

The individual files in this repository are the complete editable sources. To export them, including the binary font subsets and 1200×630 social image:

```sh
git archive --format=zip --output=../chr-site-source.zip HEAD
```

## Deployment guide

Use **Settings → Pages → Build and deployment → Deploy from a branch → `journal` / `(root)`**. Edit on `journal` (`git switch journal` after cloning). Every accepted push to this branch triggers the managed build. Check the `github-pages` deployment in Actions. Do not upload `_site/`, the local dependency directory or design reference archives. If moving to a project-site URL later, update `url` and `baseurl` in `_config.yml` first.

**Local preview** (Ruby 3.3, Bundler, compiler for native gems):

```sh
bundle config set --local path vendor/bundle
bundle install
JEKYLL_ENV=production bundle exec jekyll build
python3 scripts/check.py
bundle exec jekyll serve --host 127.0.0.1
```

Open `http://127.0.0.1:4000/`. For a regression, revert the affected site change on `journal` and push the revert; do not rewrite history. Do not switch publication back to another branch without reviewing everything it would publish.

### Publish an article

Create `_posts/YYYY-MM-DD-stable-slug.md`. The filename controls the permanent address; changing the title need not change inbound links.

```yaml
---
title: 一張紙的兩面
description: 一兩句可以獨立閱讀的摘要。
date: 2026-11-20 04:00:00 +0000
categories: [構成]
tags: [CSS, 排版]
serial: "04"
featured: false
---
```

Write the body below the front matter. Use `##`/`###` headings for the TOC, a single category per post and short tags. Reading time is a character-based estimate for Chinese prose. Select `featured: true` for up to three homepage picks; the newest featured articles are shown first. Optional `cover` and `cover_alt` fields replace the category motif; author small 16:9 WebP/AVIF thumbnails. Use meaningful alt text for informative images (empty for decorative ones). For body images supply intrinsic `width` and `height` and `loading="lazy"` below the fold.

### Publish a case study

Copy a Markdown file in `_projects/`. Set `title`, `description`, `date`, a quoted two-digit `serial`, `stack`, and `repository_link` pointing at the case's public source. The filename becomes the case-study slug. Experience and contact details are edited separately in `about/index.md`.

## Future enhancements

Keep the archive server-rendered while it is small. If the HTML grows substantially, paginate first, then load a generated full-text index on search intent. Re-run mobile Lighthouse after changing fonts or adding covers; keep first-viewport artwork free of large image downloads. Confirm real Core Web Vitals with field data once traffic is sufficient—lab scores alone cannot establish them.
