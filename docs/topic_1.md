---
title: "Topic 1: Add/remove a site page"
description: "Basic information on managing site pages"
---


# {{ get_title(page) }}
{{ get_description(page) }}

**NOTE:** There are 10 toy Topic sections here, expecting that some teachers may want to have one page per week (for a 10 week course). You are encouraged to structure your course **however works best for your class**. All of your course information could be on a single page, or you might have a different number of topics, or organize weekly, or any other organization that works for you.

<p style="color: #ba5e00"><b>TO UPDATE THIS PAGE:</b> Open and edit the <b>topic_1.md</b> file, in <code>docs/</code> folder, to delete this placeholder text and customize with your own!</p>

## Add a site page

### The quick version: 

- Make a new Markdown document, save
- Add the `.md` to `mkdocs.yaml` so the page exists on the site
- Build to see updated site

Below for a bit more detail...

### Make each page a Markdown document

To make a new page:

1. Within your website `docs/` folder, create a new `.md` file. Save it in the `docs/` folder. For this example, let's say you've saved it as `new_page.md.`

2. In that .md file, remove everything but the title (which you can change) from the YAML - that's the top section of the .md, where by default it has title, author, date, etc.

3. Update the .md to contain whatever you want to have on that page. Don't know a lot about markdown? Considering switching over to VSCode, which has built in support for .md files, including previews. 

4. Save the .md

### Add it to your navigation bar

5. Open the `mkdocs.yml` file in your Project

6. Add the information to the YAML `nav` section, which will almost always be the text that you want to appear in the navigation bar, and the file name of the **Markdown (md) file** that will be the source for the the page on your website. That would be `new_page.md` for this example . So in the `mkdocs.yml` I would need to add this to the nav section: 

```
    - 'A New Page': new_page.md
```
Note: If the new page is part of the list of Topics, you would add it within the `Topic` subsection of the nav section in the same way as above. You can, of course, even add new subsections to the nav. For example, `Assignments` could become a subsection instead of a single page, with each Assignment having its own .md file (`assignment_1.md`, `assignment_2.md`, etc...)

<p style="color: #ba5e00"><b>Note:</b> YAML is space & indentation specific. Follow the structure that already exists in this template to avoid YAML errors.</p>

How is the website finding the html? By default, `mkdocs` assumes that files are stored in the `docs` folder. That means when we run the 'build' command (`mkdocs build` at the command line), our .md pages are render to HTML & sent to the `site` folder. This is also important because when we deploy the site (make it live), we will want to deploy **from that site folder** using GitHub pages.

Take a look at some other pages in this template (Resources, Assignments, etc.) to see the structure, & give it a shot!

## Delete/disappear a site page

The safest thing to do if you don't want a page to *show up* is to remove it from the `mkdocs.yml` nav listings. That way, the material on the page still exists as a file in your project, but doesn't show up on the website -- don't delete a page file unless you are REALLY SURE that you're never going to want the material on that page ever again.


