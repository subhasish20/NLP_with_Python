import emoji

def remove_emoji(text:str)->str:
    
    
    return emoji.replace_emoji(text,replace="")

text = "I am very happy today! 😊👍"
print(f"Original text is : {text}")
clean_emoji = remove_emoji(text)
print(f"Deemoji text is : {clean_emoji}")