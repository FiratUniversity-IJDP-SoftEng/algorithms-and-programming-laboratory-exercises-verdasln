# Your Student ID: 220543016
# Your Name and Surname: Verda Aslan

while True:
    # iki sayı sec
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # hangi islem
    operation = input("Choose an operation (+, -, *, /): ")

    # yap islemi
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            continue  # Yeniden giriş istemek için döngüye devam et
        result = num1 / num2
    else:
        print("Invalid operation. Please choose +, -, *, or /.")
        continue  # Yeniden giriş istemek için döngüye devam et

    # sonuc 
    print(f"Result: {result}")

    # tekrar hesap yapmak isteyip istemediğini sor
    again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if again != "yes":
        print("Goodbye!")
        break  # Döngüyü sonlandır
