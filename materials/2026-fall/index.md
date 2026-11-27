---
permalink: /materials/2026-fall/
---

# Fall 2026 materials

These slides follow the Fall 2026 seminar schedule.

The [research paper collection]({{ '/materials/papers.html' | relative_url }}) is shared across semesters.


{% assign slides = site.static_files | sort: 'path' %}
{% for slide in slides %}
{% if slide.path contains '/materials/2026-fall/' and slide.extname == '.pdf' %}
- [{{ slide.name }}]({{ slide.path | relative_url | uri_escape }})
{% endif %}
{% endfor %}

