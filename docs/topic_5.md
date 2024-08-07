---
title: "Topic 5: Basic formatting"
---

<p style="color: #ba5e00"><b>TO UPDATE THIS PAGE:</b> Open and edit the <b>topic_5.md</b> file, in <code>docs/</code> folder, to delete this placeholder text and customize with your own!</p>

If you're familiar with markdown, use standard syntax to update font styles, add bulleted lists, subscripts/superscripts, etc. (or learn more from the [Markdown cheatsheet](https://github.com/im-luka/markdown-cheatsheet)). 

## Visual Editors

If you're not familiar with markdown and want an easier way to update formatting, there are plenty of visual editors. You can use:

1. **Typora** - A minimalist Markdown editor that provides a seamless live preview feature, allowing you to edit and see the results visually in real-time. [Download Typora](https://typora.io/)
  
2. **Mark Text** - An open-source Markdown editor that focuses on speed and usability with an interface that hides Markdown formatting symbols unless you need them. [Download Mark Text](https://marktext.app/)
  
3. **StackEdit** - A free, open-source in-browser Markdown editor that's great for those who prefer working directly within their web browser. [Use StackEdit](https://stackedit.io/)
  
4. **Zettlr** - A Markdown editor designed for researchers, it supports complex integrations and features like Zettelkasten and citation management. [Download Zettlr](https://www.zettlr.com/)
  
5. **Ghostwriter** - A distraction-free Markdown editor for Windows and Linux, offering a clean interface and useful features like live HTML preview. [Download Ghostwriter](https://wereturtle.github.io/ghostwriter/)
  
6. **iA Writer** - Known for its focus mode, which helps you concentrate on one sentence at a time, it's available for Mac, iOS, and Android. [Download iA Writer](https://ia.net/writer)

These editors simplify the process of using Markdown by providing friendly interfaces and visual previews, making them great choices for both beginners and experienced users alike.

## IDE Visual Editors

Both [RStudio](https://posit.co/downloads/) and Visual Studio Code ([VSCode](https://code.visualstudio.com)) are powerful tools that support Markdown editing with features that enhance visual editing and provide a more user-friendly experience. Here’s how you can use these environments effectively for Markdown editing:

### RStudio

RStudio is particularly well-suited for Markdown editing. Here's how to use it:

1. **Open/Create a Markdown File**:
   - Start RStudio and either open an existing Markdown file or create a new one by going to **File > New File > R Markdown**.

2. **Edit and Write Markdown**:
   - You can write standard Markdown for use in this template; `mkdocs` cannot parse RMarkdown documents that contain R code blocks. RStudio's editor supports syntax highlighting for Markdown and R code, making it easier to distinguish text from code (again, don't try to use R code on pages for this template).

3. **Use the RStudio Toolbar**:
   - RStudio includes a Markdown toolbar that provides buttons for common formatting options like headers, bold, italics, bullet lists, and more. This toolbar simplifies formatting without needing to remember Markdown syntax.

4. **Live Preview**:
   - Use the **Knit** button (the yarn ball icon) in RStudio to compile your Markdown document into a HTML, PDF, or Word document. This action also provides a preview of how your document will look.
   - For plain Markdown files, you can use the **Preview** button (next to the Knit button) to see a live HTML preview of your document.


### Visual Studio Code (VSCode)

VSCode, a lightweight but powerful source code editor, supports Markdown editing through its built-in features and extensive extension ecosystem:

1. **Install Markdown Extensions**:
   - Open the Extensions view by clicking on the square icon on the sidebar, or pressing `Ctrl+Shift+X`.
   - Install extensions such as **Markdown All in One** by Yu Zhang for enhanced Markdown support (like table formatting, list editing, and more) and **Markdown Preview Enhanced** by Yiyi Wang for a powerful preview feature.

2. **Open/Create a Markdown File**:
   - Open an existing Markdown file or create a new one with a `.md` extension. VSCode recognizes the file type and enables Markdown-specific features.

3. **Edit and Preview Markdown**:
   - Write your Markdown content in the editor. With the Markdown Preview Enhanced extension, you can open a side-by-side preview by clicking on the preview icon in the top right of the editor or by pressing `Ctrl+K V`. This live preview updates as you edit the Markdown file.

4. **Use Markdown Shortcuts and Commands**:
   - VSCode supports various Markdown shortcuts and commands which can be accessed via `Ctrl+Shift+P` to open the Command Palette and typing `Markdown`. You'll find commands for styling, navigating, and managing Markdown content.

5. **Customize Your Experience**:
   - Customize the Markdown preview styles by modifying the VSCode settings or adding custom CSS styles for the preview.
