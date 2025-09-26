# age_category.py

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 0 and age <= 12:
    category = "Child"
elif age >= 13 and age <= 19:
    category = "Teen"
elif age >= 20 and age <= 59:
    category = "Adult"
elif age >= 60:
    category = "Senior"
else:
    category = "Invalid age"

print("\n--- Age Category Summary ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Category: {category}")
