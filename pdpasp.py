text = "th, k, n, w, x, l, p, u, e, 11, 8"
words = [word.strip() for word in slovar.split(",")]  # Split the text into words and remove any leading/trailing whitespace
quoted_words = [f'"{word}"' for word in words]  # Add quotes around each word

result = ", ".join(quoted_words)
print(result)