---
title: "Topic 7: Remove tables of contents"
---

<p style="color: #ba5e00"><b>TO UPDATE THIS PAGE:</b> Open and edit the <b>topic_7.md</b> file, in <code>docs/</code> folder, to delete this placeholder text and customize with your own!</p>

In this MkDocs template, you'll notice that a Table of Contents is automatically created on pages with headings (starting with Level 2 headers as top-level items).

To remove the automatic Table of Contents, open the `mkdocs.yml` file. In the `theme` section, adjust the `toc` settings to disable it.

That section in `mkdocs.yml` would then look like this, and the Table of Contents won't appear:

```yaml
theme:
  name: 'material'
  toc:
    enabled: false
```

### Steps to Disable the Table of Contents in MkDocs

1. **Open `mkdocs.yml`**:
   - Locate your `mkdocs.yml` configuration file in the root of your MkDocs project.

2. **Modify the Theme Section**:
   - Add or update the `theme` section to include the `toc` settings with `enabled: false`.

3. **Save Changes**:
   - Save the file to apply the changes.

4. **Rebuild Your Site**:
   - Run `mkdocs serve` to test the changes locally and ensure the Table of Contents is no longer appearing on your pages.
   - Once satisfied, deploy your site using `mkdocs gh-deploy`.

### Removing the Table of Contents for a single page

If you want to remove the Table of Contents (ToC) for a specific page in MkDocs, you can do this by using the `md`-specific metadata at the top of your Markdown file. Here’s how you can achieve this:

1. **Open the Markdown File**:
   - Locate the Markdown file for the page where you want to disable the Table of Contents.

2. **Add Metadata to Disable ToC**:
   - At the top of the Markdown file, add the following YAML front matter to disable the ToC for that page:

```markdown
---
title: Page Title
description: Page description
hide:
  - toc
---

# Your Page Title

Your content goes here...
```

3. **Save Changes**:
   - Save the Markdown file with the added front matter.

4. **Rebuild and Test Your Site**:
   - Run `mkdocs serve` to view the changes locally and confirm that the ToC is not appearing on that specific page.
   - Deploy your site using `mkdocs gh-deploy` once you are satisfied with the results.

#### How does this work?

- **YAML Front Matter**: The YAML front matter (`---` block) is used to set page-specific options in MkDocs. The `hide: - toc` setting specifically instructs MkDocs to hide the Table of Contents for that page.

To learn more about MkDocs YAML front matter and page-specific options, you can refer to the following resources:

1. **MkDocs Official Documentation**:  
   The MkDocs documentation provides a comprehensive guide on configuring your site, including YAML front matter options for individual pages. [MkDocs Configuration](https://www.mkdocs.org/user-guide/configuration/)

2. **MkDocs-Material Theme Documentation**:  
   If you are using the MkDocs-Material theme, it offers additional options and detailed explanations of YAML front matter specific to this theme. It includes various customization options like hiding elements, setting metadata, and more. [MkDocs-Material Theme](https://squidfunk.github.io/mkdocs-material/reference/metadata/)
