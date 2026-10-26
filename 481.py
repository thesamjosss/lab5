words = [w.strip() for w in input().split(",")]
words.sort(key=lambda x: x.lower(), reverse=True)
print(" ".join(words))

