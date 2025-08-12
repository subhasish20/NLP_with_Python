import re

def remove_html_tag(text: str) -> str:
    """
    Removes HTML tags from the input text.
    """
    # Regex to match anything between < and >
    cleaner = re.compile(r"<[^>]+>")
    clean_text = re.sub(cleaner, "", text)
    return clean_text

text = "<h>hello</><b>world</b>"

cleaned_text = remove_html_tag(text)

print(cleaned_text)  

