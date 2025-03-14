# Your Student ID: 220543016
# Your Name and Surname: Verda Aslan

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    spaces = ' ' * (n - i)  # Boşlukları oluştur
    stars = '*' * (2 * i - 1)  # Yıldızları oluştur
    print(spaces + stars)  # Boşluk + yıldızları yazdır
