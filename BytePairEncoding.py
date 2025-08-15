import importlib
import tiktoken

tokenizer = tiktoken.get_encoding("gpt2")

text = ("Hi, do you like tea? <|endoftext|> in the realm of dreams, "
        "of someunknownplace")
integers = tokenizer.encode(text, allowed_special={"<|endoftext|>"})
print(integers)

strings = tokenizer.decode(integers)
print(strings)