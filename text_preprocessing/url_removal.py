import re

def remove_urls(text: str) -> str:
    """
    Removes all URLs from the given text using regex.
    """
    pattern = re.compile(r"https?://\S+|www\.\S+")
    return re.sub(pattern, "", text)

# Example usage
text = "Visit https://example.com or www.test.com for details."
print(remove_urls(text))  # Output: Visit  or  for details.
