import re

def strip_html_tags(text: str) -> str:

    # Pattern to match HTML tags
    clean_pattern = re.compile(r'<.*?>', re.DOTALL)
    return re.sub(clean_pattern, '', text).strip()

# Example 1: Basic HTML removal
sample_text = "<html><body>This is a <b>sample</b> text with <p>HTML tags</p>.</body></html>"
print("🔹 Original Text:", sample_text)
print("✅ Cleaned Text:", strip_html_tags(sample_text))
