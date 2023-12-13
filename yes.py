hashmap = {}

string = "The quick brown fox jumps over the lazy dog"

for char in string.lower():
    if char != " ":
        hashmap[char] = True

string ="abcbaa"
if string[::-1] == string:
    print("true")