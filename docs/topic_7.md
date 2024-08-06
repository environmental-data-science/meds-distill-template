---
title: "Topic 7: Remove tables of contents"
---

# {{ get_title(page) }}
{{ get_description(page) }}

<p style="color: #ba5e00"><b>TO UPDATE THIS PAGE:</b> Open and edit the <b>topic_7.md</b> file, in <code>docs/</code> folder, to delete this placeholder text and customize with your own!</p>

In this template, you'll notice that a Table of Contents is automatically created on pages with headings (starting with Level 2 headers as top-level items). 

To remove the auto-table of contents, open the `_site.yml` file. In the `output` section, change the `toc: ` and `toc_float: ` fields to `false`. 

That section in `_site.yml` would then look like this, and the table of contents won't appear: 

```
output:
  distill::distill_article:
    toc: false
    toc_float: false
```
