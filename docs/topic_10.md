---
title: "Topic 10: Inserting tables"
---

<p style="color: #ba5e00"><b>TO UPDATE THIS PAGE:</b> Open and edit the <b>topic_10.md</b> file, in <code>docs/</code> folder, to delete this placeholder text and customize with your own!</p>

## Use a Visual Editor

If you want to create a table in your Markdown from scratch that is easily editable (e.g., a table of Assignment due dates or something), it might be easiest to just make the thing manually right in your Markdown document.

To do that, I strongly recommend using one of the visual editor options presented in [Topic 5](topic_5.md). Many have an "Insert Table" option, as well as tools for formatting tables. 
Here's the updated text with both the Markdown code and rendered examples, along with an explanation of how `---` is used to divide header rows:

---

## Other Options for Creating Tables

There are several ways to create and format tables in Markdown. These options can be used to create tables for your MkDocs site or any other Markdown-based platform.

### Tutorials for Making Tables in Markdown

- [Markdown Guide: Tables](https://www.markdownguide.org/extended-syntax/#tables): This guide provides a straightforward tutorial on creating tables using Markdown syntax.
- [GitHub Flavored Markdown: Tables](https://github.github.com/gfm/#tables-extension-): GitHub's official documentation on how tables work in GitHub Flavored Markdown (GFM).
- [CommonMark: Tables](https://commonmark.org/help/tutorial/10-tables.html): CommonMark's tutorial on creating tables, which is compatible with many Markdown processors.

### Basic Instructions for Making Tables

To create a simple table in Markdown, follow these steps:

1. **Define the Header**:
   - Use pipes (`|`) to separate columns in the header row.
   - Use `---` to divide header rows and define column alignment.

2. **Add Rows**:
   - Add additional rows by using pipes to separate column values.

3. **Align Text**:
   - Use colons (`:`) in the separator row to align text within columns:
     - `:---` for left alignment.
     - `:---:` for center alignment.
     - `---:` for right alignment.

Here's how the Markdown code looks and its rendered output:

#### Example 1: Simple Table

**Markdown Code:**
```markdown
| Header 1 | Header 2 | Header 3 |
| -------- | -------- | -------- |
| Row 1    | Data 1   | Data 2   |
| Row 2    | Data 3   | Data 4   |
```

**Rendered Table:**

| Header 1 | Header 2 | Header 3 |
| -------- | -------- | -------- |
| Row 1    | Data 1   | Data 2   |
| Row 2    | Data 3   | Data 4   |

**Explanation:**  
- `---` is used below the header to separate it from the rest of the table and to define the column headers. It indicates the beginning of the data rows.

#### Example 2: Aligned Text

**Markdown Code:**
```markdown
| Left Align | Center Align | Right Align |
| :--------- | :----------: | ----------: |
| Data       | Data         | Data        |
| Data       | Data         | Data        |
```

**Rendered Table:**

| Left Align | Center Align | Right Align |
| :--------- | :----------: | ----------: |
| Data       |     Data     |        Data |
| Data       |     Data     |        Data |

**Explanation:**  
- The colons (`:`) in the separator row indicate the text alignment for each column:
  - `:---` for left-aligned text.
  - `:---:` for centered text.
  - `---:` for right-aligned text.

### Additional Formatting

If you want to enhance the appearance of your tables beyond the basic Markdown syntax, you can apply custom CSS styles in your MkDocs `theme.css` file. This allows you to style tables to better match your site's design.
