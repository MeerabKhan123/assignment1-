#  Bank Account Management System

# -----------------------------
# 1 Variables and Constants
# -----------------------------
bank_name = "National Bank of Python"
account_type = "Savings"
MIN_BALANCE = 1000  # Constant

# -----------------------------
# 2 Taking Input from User
# -----------------------------
customer_name = input("Enter your full name: ")
age = int(input("Enter your age: "))
account_number = int(input("Enter your account number: "))
initial_deposit = float(input("Enter your initial deposit amount: "))

# -----------------------------
# 3 Display Data Types
# -----------------------------
print("\n--- Data Types ---")
print("Name:", type(customer_name))
print("Age:", type(age))
print("Account Number:", type(account_number))
print("Initial Deposit:", type(initial_deposit))

# -----------------------------
# 4 String Operations
# -----------------------------
print("\n--- String Operations ---")
print("Name in Uppercase:", customer_name.upper())
print("Number of Characters in Name:", len(customer_name))

# -----------------------------
# 5 Type Casting and Conversion
# -----------------------------
account_number_str = str(account_number)
print("\nAccount Number (as String):", account_number_str)
print("Length of Account Number:", len(account_number_str))

age_float = float(age)
print("Age as Float:", age_float)

# -----------------------------
# 6 Data Structures
# -----------------------------
# Tuple → Available account types
available_accounts = ("Savings", "Current", "Fixed")

# List → Last 3 transactions
transactions = [5000, -2000, 3000]  # + for deposit, - for withdrawal

# Dictionary → Customer details
customer = {
    "name": customer_name,
    "age": age,
    "account_number": account_number,
    "balance": initial_deposit
}

# -----------------------------
# 7 Mathematical Operations
# -----------------------------
# Add deposits and subtract withdrawals
total_balance = customer["balance"] + sum(transactions)

# Interest calculation (5%)
interest = total_balance * 0.05
total_balance += interest

# Modulus check
if total_balance % 2 == 0:
    even_odd = "Even"
else:
    even_odd = "Odd"

print("\n--- Account Summary ---")
print("Bank:", bank_name)
print("Account Type:", account_type)
print("Available Account Types:", available_accounts)
print("Final Balance (with interest):", total_balance)
print("Balance is an", even_odd, "number")

# -----------------------------
# 8 Conditional Structures
# -----------------------------
print("\n--- Account Holder Status ---")
if total_balance >= 100000:
    print("🏅 Premium Account Holder")
elif total_balance >= 50000:
    print("🥇 Gold Account Holder")
elif total_balance >= 20000:
    print("🥈 Silver Account Holder")
else:
    print("🥉 Basic Account Holder")

# -----------------------------
# 9 While Loop (Password Check)
# -----------------------------
print("\n--- Secure Login ---")
correct_password = "python123"
entered_password = ""

while entered_password != correct_password:
    entered_password = input("Enter your bank login password: ")
    if entered_password != correct_password:
        print("Incorrect password! Try again.")

print("✅ Login successful!")

# -----------------------------
# 10 While Loop (Transaction Counter)
# -----------------------------
print("\n--- Transaction Counter ---")
counter = 1
while counter <= 10:
    print("Transaction", counter)
    counter += 1

print("\nThank you for banking with", bank_name)
