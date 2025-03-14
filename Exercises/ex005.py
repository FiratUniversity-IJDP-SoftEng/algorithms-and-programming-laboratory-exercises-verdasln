# Your Student ID:
# Your Name and Surname:

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print("Hi".ljust(10) + last_name) ## ljust(10)  "Hi" kelimesini sola yaslayıp boşluk ekliyoruz.
print(first_name.rjust(10)) ## rjust(10)  Adı sağa hizalayarak soyadın altına denk gelmesini sağlıyoruz.
