# Scrappy Kin Website

Public source for [scrappykin.com](https://scrappykin.com).

The site is intentionally small: static HTML, CSS, JavaScript, and images live
under `public/`. Runtime and production deployment configuration live in the
private infrastructure repository and are not part of this project.

The `.com` consent panel and footer control live in
`public/js/analytics-consent.js`; shared copy, choice state, and the event gate
come from the public `scrappy-kin-analytics` repository's
`/_analytics/script.js`. Release them with the matching collector and Privacy
Policy text. The website source alone does not prove what production serves.

## Local preview

From the repository root:

```bash
python3 -m http.server 8000 --directory public
```

Then open <http://localhost:8000>.

## Making changes

Edit the reviewed files under `public/` directly. The legal pages are canonical
HTML; there is no separate Markdown-to-HTML generator.

Product Ops supplies the files under `public/shared/design-foundation/` and the
generated agent surfaces. Do not edit those vendored files directly here.

Production releases remain human-approved. A release imports one exact commit
from this repository into the private infrastructure repository; this repository
contains no VPS credentials or deployment authority.

## License and marks

Code is licensed under the GNU Affero General Public License v3.0; see
[`LICENSE`](LICENSE). Scrappy Kin names, logos, and other brand identifiers are
not licensed as trademarks; see [`TRADEMARKS.md`](TRADEMARKS.md).
