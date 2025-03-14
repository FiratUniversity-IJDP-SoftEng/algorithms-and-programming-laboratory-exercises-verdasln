# Your Student ID: 220543016
# Your Name and Surname: Verda Aslan

# hango dinusumu istiyosun
choice = input("Choose conversion (C to F or F to C): ").strip().lower()

# sicakligi sec
temperature = float(input("Enter the temperature value: "))

# donusum
if choice == "c to f":
    converted = (temperature * 9/5) + 32
    print(f"{temperature}°C is {converted:.2f}°F")
elif choice == "f to c":
    converted = (temperature - 32) * 5/9
    print(f"{temperature}°F is {converted:.2f}°C")
else:
    print("Invalid choice. Please enter 'C to F' or 'F to C'.")
