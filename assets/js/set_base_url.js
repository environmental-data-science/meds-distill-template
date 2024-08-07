// Example script to ensure paths respect the base URL when using the MkDocs Material theme
// This script should be included in the MkDocs configuration file (mkdocs.yml) as a custom script
document.addEventListener("DOMContentLoaded", function () {
    const images = document.querySelectorAll('img');
    const basePath = '/meds-mkdocs-template';

    images.forEach((img) => {
        if (!img.src.includes(basePath)) {
            img.src = `${basePath}${img.getAttribute('src')}`;
        }
    });
});
