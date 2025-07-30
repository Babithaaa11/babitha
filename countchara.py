n = input("enter the characters")
char_count = {}
for char in n:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print("character frequencies:")
for char , count in char_count.items():
    print(f"'{char}':{count}")