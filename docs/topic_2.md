---
title: "Topic 2: Update site title and subtitle"
---

<p style="color: #ba5e00"><b>TO UPDATE THIS PAGE:</b> Open and edit the <b>topic_2.md</b> file, in the <code>docs/</code> folder, to delete this placeholder text and customize with your own!</p>

One of the first things you'll want to do is update your site title, and description. 

Here's how:

- The main title and subtitle for the home page live in the YAML of the `mkdocs.yml` file. Open it in your project, update the `site_name` and `site_description` fields in the YAML. 

- While editing this file, you should also update the `site_url` to match the base url that the site will have on github. This will mean changing the template `site_url` from `https://environmental-data-science.github.io/meds-mkdocs-template/` to your site's url, which will be:

```md
https://<your-github-username>.github.io/<your_site_repository>/
```
Save, then build and serve your site (run `mkdocs serve`) to see the updated title. Using `mkdocs serve -o` will automatically open a new web browser window. 

**Note**: The `site_name` field in the `mkdocs.yml` file is also used to determine the label for the short link at the top of the page and text text at the top of your navigation menu. 
