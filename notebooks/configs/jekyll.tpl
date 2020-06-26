{% extends 'markdown.tpl' %}

{% set notebook_name = resources['metadata']['name'] %}
{% set post_date, post_name = notebook_name.split(maxsplit=1) %}

{%- block header -%}
---
title: "{{ post_name }}"
date: {{ post_date }}
layout: post
{% for cell in nb.cells %}
{% if "Description" in cell.metadata.tags %}
description: "{{ cell.source }}"
{% break %}
{% endif %}
{% endfor %}
{% for cell in nb.cells %}
{% if "articleTags" in cell.metadata %}
tags: {{ cell.metadata.articleTags }}
{% break %}
{% endif %}
{% endfor %}
comments: true
share: true
---

{%- endblock header -%}

{% block in_prompt %}
{% endblock in_prompt %}

{% block input %}
{# Don't need it yet
{% if cell.source.strip() %}
<div>
<a href="javscript:void(0)" onclick="showSourceCode(this)">Show source code</a>
<div data-type="source-code" style="display: none;">
{{ '{% highlight python %}' }}
{{ cell.source }}
{{ '{% endhighlight %}' }}
</div>
</div>
{% endif %}
#}
{% endblock input %}

{% block data_svg %}
![svg]({{ output.metadata.filenames['image/svg+xml'] | path2support }})
{% endblock data_svg %}

{% block data_png %}
![png]({{ output.metadata.filenames['image/png'] | path2support }})
{% endblock data_png %}

{% block data_jpg %}
![jpeg]({{ output.metadata.filenames['image/jpeg'] | path2support }})
{% endblock data_jpg %}

{% block markdowncell scoped %}
{% if "Description" not in cell.metadata.tags and "Tags" not in cell.metadata.tags %}
{{ cell.source | wrap_text(80) }}
{% endif %}
{% endblock markdowncell %}

{% block headingcell scoped %}
{{ '#' * cell.level }} {{ cell.source | replace('\n', ' ') }}
{% endblock headingcell %}
