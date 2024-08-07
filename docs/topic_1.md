---
title: "Topic 1: Add/remove a site page"
description: "Basic information on managing site pages"
---


**NOTE:** There are 10 toy Topic sections here, expecting that some teachers may want to have one page per week (for a 10 week course). You are encouraged to structure your course **however works best for your class**. All of your course information could be on a single page, or you might have a different number of topics, or organize weekly, or any other organization that works for you.

<p style="color: #ba5e00"><b>TO UPDATE THIS PAGE:</b> Open and edit the <b>topic_1.md</b> file, in <code>docs/</code> folder, to delete this placeholder text and customize with your own!</p>

## Add a site page

### The quick version: 

- Make a new Markdown document, save
- Add the `.md` to `mkdocs.yaml` so the page exists on the site
- Build to see updated site

Below for a bit more detail...

### Make Each Page a Markdown Document

To create a new page for your MkDocs site:

1. **Create a New Markdown File**:
   - Within your website's `docs/` folder, create a new `.md` file. Save it in the `docs/` folder. For this example, let's say you've saved it as `new_page.md`.

2. **Add YAML Front Matter**:
   - At the top of your `.md` file, add YAML front matter to define the page title and any other metadata you need. The YAML front matter is the section enclosed between `---` lines at the top of the file. Here's a basic example:

```yaml
---
title: "Your Page Title"
---

```

   - You can customize the `title` field to match what you want to appear in the navigation bar and the page title. You may include other optional metadata like `description` or `author` if needed.

3. **Update the Content**:
   - After the YAML front matter, add the content you want on that page. Write your content using Markdown syntax. If you're not familiar with Markdown, consider using a text editor like VSCode, which offers built-in support for Markdown files, including previews.

   - Here’s a simple Markdown example:

```markdown
---
title: "Your Page Title"
---

# Welcome to New Page

This is your new page content. You can add text, images, lists, and more using Markdown syntax.

## Subheading

Add more detailed information under different sections as needed.
```

4. **Save the File**:
   - Save the `.md` file with your changes.

5. **Preview Your Site**:
   - Run `mkdocs serve` in your terminal to preview your site locally and ensure your new page appears correctly with the specified title.

By following these steps, you can effectively create and manage pages for your MkDocs site, using the YAML front matter to control page titles and other metadata. This approach ensures consistency and clarity across your documentation project.

### Add it to your navigation bar

5. Open the `mkdocs.yml` file in your Project

6. Add the information to the YAML `nav` section, which will almost always be simply the file name of the **markdown (md) file** that will be the source for the the page on your website. `mkdocs` will determine the text in the navigation bar from the file's `title` that you set in the YAML front matter. That would be `new_page.md` for this example . So in the `mkdocs.yml` I would need to add this to the nav section: 

```md
    - new_page.md
```
Note: If the new page is part of the list of Topics, you would add it within the `Topic` subsection of the nav section in the same way as above. You can, of course, even add new subsections to the nav. For example, `Assignments` could become a subsection heading instead of a markdown page, with each Assignment having its own .md file (`assignment_1.md`, `assignment_2.md`, etc...)

<p style="color: #ba5e00"><b>Note:</b> YAML is space & indentation specific. Follow the structure that already exists in this template to avoid YAML errors.</p>

How is the website finding the html? By default, `mkdocs` assumes that files are stored in the `docs` folder. That means when we run the 'build' command (`mkdocs build` at the command line), our .md pages are render to HTML & sent to the `site` folder. This is also important because when we deploy the site (make it live), we will want to deploy **from that site folder** using GitHub pages.

Take a look at some other pages in this template (Resources, Assignments, etc.) to see the structure, & give it a shot!

## Delete/disappear a site page

The safest thing to do if you don't want a page to *show up* is to remove it from the `mkdocs.yml` nav listings. That way, the material on the page still exists as a file in your project, but doesn't show up on the website -- don't delete a page file unless you are REALLY SURE that you're never going to want the material on that page ever again.


