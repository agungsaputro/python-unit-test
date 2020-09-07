def trim_text(text, int):
    if text == int:
        raise TypeError
    
    new_text = text[:int]
    return new_text+ "..."

text = trim_text("ini adalah tulisan yang sangat panjang",8)
print(text)