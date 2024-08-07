---
title: "Topic 8: Creating a dropdown list in the navigation bar"
---

<p style="color: #ba5e00"><b>TO UPDATE THIS PAGE:</b> Open and edit the <b>topic_8.md</b> file, in <code>docs/</code> folder, to delete this placeholder text and customize with your own!</p>

If you look at this MkDocs template, you'll notice that some navigation bar items link directly to a single page, while the "Topics" item takes you to a dropdown menu.

### Creating Dropdown Menus

To create a dropdown menu of pages in MkDocs:

1. **Create and Save Pages**:
   - Create and save your pages as individual Markdown (`.md`) documents. Make sure each Markdown file has a YAML front matter at the top specifying the page title, like this:

```yaml
---
title: "Your Page Title"
---

## Content of your page

```

2. **Edit `mkdocs.yml`**:
   - Open the `mkdocs.yml` file in the root of your MkDocs project.
   - In the `nav` section, create a menu with the pages by specifying only the filename. MkDocs will automatically read the page title from the YAML front matter in each Markdown file:

```yaml
    nav:
    - Home: index.md
    - Dropdown menu:
        - item_1.md
        - item_2.md
```

   - This approach allows MkDocs to dynamically populate the menu titles based on the content of each Markdown file, making it easier to manage titles directly within the pages.

3. **File Naming**:
   - Ensure that your new pages are correctly named, such as `item_1.md` and `item_2.md` (or any names you choose), to match the links specified in the `mkdocs.yml` file.

4. **Save Changes and Build the Site**:
   - Save your changes to the `mkdocs.yml` file.
   - Run `mkdocs serve` to preview your site locally and ensure the dropdown menu works as expected.
   - Once you're satisfied, deploy your site using `mkdocs gh-deploy`.
