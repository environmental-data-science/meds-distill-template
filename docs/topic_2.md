---
title: "Topic 2: Update site title and subtitle"
---

# {{ get_title(page) }}
{{ get_description(page) }}


<p style="color: #ba5e00"><b>TO UPDATE THIS PAGE:</b> Open and edit the <b>topic_2.md</b> file, in the <code>docs/</code> folder, to delete this placeholder text and customize with your own!</p>

One of the first things you'll want to do is update your site title, subtitle, and the short link on the right side of the navbar. 

Here's how:

- The main title and subtitle for the home page live in the YAML of the `mkdocs.yml` file. Open it in your project, update the `title` and `description` fields in the YAML, save, then build your site (run `mkdocs build` at the command line in your project root directory) to see the updated title.

- The label for the short link in the upper right of the page (right side of the navigation bar) is specified in the `mkdocs.yml` page. Open the `mkdocs.yml` file in your project, update the `site_name` field, save, and rebuild the site to see your update.
