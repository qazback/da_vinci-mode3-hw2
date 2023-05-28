import emoji

def emojize_text(text):
    emojized_text = emoji.emojize(text, use_aliases=True)
    return emojized_text

user_input = input("Enter a string in English: ")
emojized_string = emojize_text(user_input)
print("Emojized string:", emojized_string)
