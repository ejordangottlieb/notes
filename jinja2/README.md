# Python Notes Page
Various Jinja2 snippets 

```
{% set my_list = [ "a", "b", "c", "d" ] %}

{% for letters in my_list %}
{{ letters }}
{% endfor %}

{{ my_list|join(", ") }}

{{ my_list|join() }}
```
