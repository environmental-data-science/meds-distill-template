---
title: "Topic 8: Dropdown list from a navigation bar item"
---

# {{ get_title(page) }}
{{ get_description(page) }}

<p style="color: #ba5e00"><b>TO UPDATE THIS PAGE:</b> Open and edit the <b>topic_8.md</b> file, in <code>docs/</code> folder, to delete this placeholder text and customize with your own!</p>

If you look at this template, you'll notice that some navigation bar items go directly to a single page, while the Modules item takes you to a dropdown menu. 

To create a dropdown menu of pages: 

1. Create and save the pages as individual R Markdown documents as described [here](topic_1.md).

2. Open the `_site.yml` file. In the `navbar` section, create a menu with the pages as linked items using a structure like this: 

```
   - text: "Dropdown menu"
      menu:
        - text: "First dropdown item"
          href: item_1.html
        - text: "Second dropdown item"
          href: item_2.html
```

The example above would only work if the new pages were created as `item_1.md` and `item_2.md`, so that when the site is built the rendered `item_1.html` and `item_2.html` files exist in the `docs` output directory.
