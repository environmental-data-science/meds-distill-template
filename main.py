# macros.py

def define_env(env):
    @env.macro
    def get_metadata(page, key, default=""):
        """Retrieve metadata from page front matter."""
        return page.meta.get(key, default)
    
    @env.macro
    def get_title(page):
        """Retrieve page title from page front matter."""
        return page.meta.get("title", "")
    
    @env.macro
    def get_description(page):
        """Retrieve page description from page front matter."""
        return page.meta.get("description", "")

    # macros.add_macro('title', get_page_title)
    # macros.add_macro('description', get_page_description)
    # macros.add_macro('metadata', get_metadata)
