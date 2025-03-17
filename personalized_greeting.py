# Task 2: Personalized Greeting

# Taking user input for first and last name
first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()

# Combining names to form full name
full_name = f"{first_name} {last_name}"

# Printing personalized greeting
print(f"\nHello, {full_name}! Welcome to the Python learning journey!")
