"""Verify generated Pages output without network access or third-party packages."""
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
from xml.etree import ElementTree as ET

root = Path(__file__).resolve().parents[1] / "_site"
origin = "https://vkcharon.github.io"


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.tags = []
        self.ids = set()
        self.ld = []
        self.in_ld = False
        self.feed(path.read_text(encoding="utf-8"))
        self.close()

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        self.tags.append((tag, data))
        if "id" in data:
            assert data["id"] not in self.ids, f"duplicate id {data['id']}"
            self.ids.add(data["id"])
        if tag == "script":
            self.in_ld = data.get("type") == "application/ld+json"

    def handle_endtag(self, tag):
        if tag == "script":
            self.in_ld = False

    def handle_data(self, data):
        if self.in_ld:
            self.ld.append(json.loads(data))


pages = {file: Page(file) for file in root.rglob("*.html")}
assert root / "index.html" in pages, "build the site first"
for file, page in pages.items():
    url = origin + "/" + str(file.relative_to(root)).removesuffix("index.html")
    assert sum(tag == "h1" for tag, _ in page.tags) == 1, file
    assert page.ld and all(isinstance(item, dict) for item in page.ld), file
    assert any(d.get("property") == "og:image" for _, d in page.tags), file
    assert any(d.get("name", d.get("property")) == "twitter:card" for _, d in page.tags), file
    assert any(d.get("rel") == "canonical" and d.get("href") == url for _, d in page.tags), file
    for _, data in page.tags:
        for attr in ("href", "src"):
            if attr not in data:
                continue
            target = urlsplit(urljoin(url, data[attr]))
            if target.hostname != urlsplit(origin).hostname:
                continue
            dest = root / unquote(target.path).lstrip("/")
            if dest.is_dir():
                dest = dest / "index.html"
            assert dest.is_file(), f"{file.name}: missing {data[attr]}"
            if dest in pages and target.fragment:
                assert unquote(target.fragment) in pages[dest].ids, f"{url}: {data[attr]}"

feed = ET.parse(root / "feed.xml")
items = feed.findall("./channel/item/link")
assert items, "RSS needs published articles"
ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
locations = {node.text for node in ET.parse(root / "sitemap.xml").findall("s:url/s:loc", ns)}
for link in items:
    assert link.text in locations and (root / urlsplit(link.text).path[1:] / "index.html") in pages
for private in ("README.md", "Gemfile", "components", "scripts"):
    assert not (root / private).exists(), f"unexpected public source: {private}"
print(f"Verified {len(pages)} HTML pages, internal links, metadata and {len(items)} RSS entries.")
