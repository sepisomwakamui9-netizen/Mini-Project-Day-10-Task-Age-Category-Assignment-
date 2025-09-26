# multiplication_table.py

num = int(input("Enter a number: "))

# Single multiplication table (1 to 10)
print(f"\nMultiplication Table for {num}")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

print("\n--- Bonus: Tables for 1 to 5 ---")
for n in range(1, 6): 
    print(f"\nMultiplication Table for {n}")
    for i in range(1, 11): 
        print(f"{n} x {i} = {n * i}")
