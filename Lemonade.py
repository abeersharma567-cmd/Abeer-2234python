def greet_customer():
    print("Welcome to the Lemonade Stand!")
    print("Fresh lemonade, made just for you.")

greet_customer()

price_per_cup = float(input("Enter the price per cup in dollars: "))
cups_sold = int(input("Enter the number of cups sold: "))

def calculate_total(price, cups):
    total = price * cups
    return total

total_cost = calculate_total(price_per_cup, cups_sold)

rounded_total = round(total_cost, 2)
print("Total Cost:", rounded_total)

amount_paid = float(input("Enter the amount paid by the customer: "))

def calculate_change(paid, total):
    change = paid - total
    return change

change_due = calculate_change(amount_paid, rounded_total)
print("Change Due:", round(change_due, 2))
print("Thank you for your business! Have a wonderful day!")
