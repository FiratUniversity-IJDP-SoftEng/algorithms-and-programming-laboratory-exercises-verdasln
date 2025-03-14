# Your Student ID: 220543016
# Your Name and Surname: Verda Aslan

text = input("Enter a string: ")

char_count = {}

for char in text:
    if char in char_count:
        char_count[char] += 1  # Eğer harf zaten varsa sayıyı artır
    else:
        char_count[char] = 1  # Eğer harf yoksa 1 olarak ekle

print("Character frequencies:")
for char in sorted(char_count):
    print(f"{char}: {char_count[char]}")
