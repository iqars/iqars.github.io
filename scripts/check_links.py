#!/usr/bin/env python3
"""Check local href/src targets and HTML fragments in a built Jekyll site."""

import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class PageLinks(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.ids = set()
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "a" and "name" in attrs:
            self.ids.add(attrs["name"])
        for attr in ("href", "src"):
            if attrs.get(attr):
                self.links.append(attrs[attr])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site_dir", nargs="?", default="_site")
    parser.add_argument("--baseurl", default="", help="Jekyll baseurl, if set")
    args = parser.parse_args()
    root = Path(args.site_dir).resolve()
    pages = {path: PageLinks(path) for path in sorted(root.rglob("*.html"))}
    if not pages or not (root / "index.html").is_file():
        parser.error(f"No built homepage in {root}; run bundle exec jekyll build first")

    baseurl = "/" + args.baseurl.strip("/") if args.baseurl.strip("/") else ""
    failures = []
    checked = 0
    for page, parsed in pages.items():
        page_url = baseurl + "/" + page.relative_to(root).as_posix()
        for link in parsed.links:
            parts = urlsplit(link)
            if parts.scheme or parts.netloc:
                continue  # External URLs, email, and data are outside this check.
            resolved = urlsplit(urljoin(page_url, link))
            path = unquote(resolved.path)
            if baseurl:
                if not path.startswith(baseurl + "/"):
                    failures.append(f"{page.relative_to(root)}: outside baseurl: {link}")
                    continue
                path = path[len(baseurl):]
            target = (root / path.lstrip("/")).resolve()
            checked += 1
            if not target.is_relative_to(root):
                failures.append(f"{page.relative_to(root)}: outside site: {link}")
                continue
            if target.is_dir():
                target /= "index.html"
            if not target.is_file():
                failures.append(f"{page.relative_to(root)}: missing target: {link}")
            elif resolved.fragment and target in pages:
                if unquote(resolved.fragment) not in pages[target].ids:
                    failures.append(f"{page.relative_to(root)}: missing fragment: {link}")
    for failure in failures:
        print(failure)
    print(f"Checked {checked} internal links across {len(pages)} HTML pages; "
          f"{len(failures)} failures.")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
