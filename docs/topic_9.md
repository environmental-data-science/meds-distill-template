---
title: "Topic 9: Changing site fonts"
---

<p style="color: #ba5e00"><b>TO UPDATE THIS PAGE:</b> Open and edit the <b>topic_9.md</b> file, in <code>docs/</code> folder, to delete this placeholder text and customize with your own!</p>

You are welcome to use any fonts you want on your website. Here, only using Google fonts is described (there are other methods for downloading fonts and adding, not included here).

## Fonts are Imported and Specified in `theme.css`

In your MkDocs project, open the `theme.css` file located in your `docs/assets/css` directory (or wherever you have your custom CSS if you have moved it).

Near the top, you'll see some lines that look like this:

```css
/* Import Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Sanchez&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@300;400&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@300;400&display=swap');

```

These are the import commands to get three different Google fonts (Sanchez, Nunito Sans, and Roboto Mono). You can explore many different Google fonts [here](https://fonts.google.com/).

## Use Different Fonts

1. **Find a [Google Font](https://fonts.google.com/)**:
   - Browse and select a font you like.

2. **Select Font Styles**:
   - Click on the font. To the right of the font example text, you should see an option to '+ Select this style'. Click the one(s) you want to select.

3. **Access Your Selected Styles**:
   - This will probably bring up a side menu. If you *don't* see that side menu, you can access your selected styles by clicking on the top-right menu icon that is a grid with 3 squares and a plus sign - hovering reveals this is to 'View your selected families'.
   - In the *Use on the web* section of the side menu, **select the radio button for @import**. It’ll look like this (for the Zen Dots Google Font):

```css
<style>
@import url('https://fonts.googleapis.com/css2?family=Zen+Dots&display=swap');
</style> 
```

4. **Copy the Import Line**:
   - Copy everything **between** (but excluding) the `<style>` and `</style>` tags.

5. **Paste into `theme.css`**:
   - Paste the `@import` line you've copied into the top section of your `theme.css` file near the other font imports. Add a comment so you can remember what this font is and how you are using it.

6. **Update CSS with New Fonts**:
   - Replace the existing font names in your CSS with the name you've imported. Use Find & Replace All to ensure you update the font everywhere it appears in the current theme.

7. **Repeat for Additional Fonts**:
   - Repeat the above steps for as many different fonts as you want to update in your theme.
