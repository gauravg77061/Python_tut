import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey There! My name is Gaurav"
token=enc.encode(text)

decoded=enc.decode([25216, 3274, 0, 3673, 1308, 382, 499, 4178, 407])
print("decoded",decoded)

print("Token",token)