# 1. Ask the user for their name, write it to name.txt
name = input("Enter name: ")
out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()

# 2. Open name.txt, read the name, and print greeting
in_file = open("name.txt", "r")
name_from_file = in_file.read().strip()
in_file.close()
print(f"Hi {name_from_file}!")

# 3. Read only the first two numbers from numbers.txt, add and print the result (59)
with open("numbers.txt", "r") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
print(number1 + number2)

# 4. Read all numbers from numbers.txt, calculate and print the total
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        total += int(line)
print(total)
