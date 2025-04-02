def reverse_text(text: str):
    idx = len(text) - 1
    while idx >= 0:
        yield text[idx]
        idx -= 1


