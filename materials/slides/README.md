# Presentation slides and materials

These files accompany the [Winter–Spring 2026 program]({{ '/2026-winter-spring/' | relative_url }}).

{% assign slides = site.static_files | sort: 'path' %}
{% for slide in slides %}
{% if slide.path contains '/materials/slides/' and slide.extname == '.pdf' %}
- [{{ slide.name }}]({{ slide.path | relative_url | uri_escape }})
{% endif %}
{% endfor %}

[Fall 2026 materials]({{ '/materials/2026-fall/' | relative_url }}) · [Related papers]({{ '/materials/papers.html' | relative_url }})
