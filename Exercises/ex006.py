# Your Student ID: 220543016
# Your Name and Surname: Verda Aslan

#Print the original list
numbers = list(range(1, 11))
print("Original list:", numbers)

#Reverse the list and print it
numbers.reverse()
print("Reversed list:", numbers)

#Add the numbers 11, 12, and 13 to the list and print it
numbers.extend([11, 12, 13])
print("List after adding 11, 12, and 13:", numbers)

#Print the list's length
print("List length:", len(numbers))

#Remove the first and last elements, then print the list
numbers.pop(0)  # İlk elemanı kaldır
numbers.pop(-1)  # Son elemanı kaldır
print("List after removing first and last elements:", numbers)

#Create and print a new sorted list containing only even numbers from the original list
even_numbers = sorted([num for num in range(1, 11) if num % 2 == 0])
print("Sorted list with only even numbers:", even_numbers)
