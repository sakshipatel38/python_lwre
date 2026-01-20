print("------secret code communication mini system------")

st = input("Enter the word for code-decode: ")
choice = input("Enter your choice (code/decode): ")

def code(st):
    if len(st) <= 3:
        # swap first and last character
        return st[2] + st[1] + st[0]
    else:
        return "Word length is long"

def decode(st):
    if len(st) <= 3:
        # swap back
        return st[2] + st[1] + st[0]
    else:
        return "Word length is long"

if choice == "code":
    print(code(st))
elif choice == "decode":
    print(decode(st))
else:
    print("Invalid choice")
