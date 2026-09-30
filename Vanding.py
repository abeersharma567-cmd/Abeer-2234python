def calculate_change(paid, price):
    change = paid - price
    return change

snack_price = 25
print("===== SNACK VENDING MACHINE =====")
print(f"This snack costs {snack_price} units.")
print("Accepted coins: 1, 5, 10, 25\n")

total_inserted = 0
coins_inserted = 0

while True:
    coin = int(input("Insert a coin (1, 5, 10, or 25): "))
    if coin not in [1, 5, 10, 25]:
        print("Invalid coin. Please insert 1, 5, 10, or 25.")
        continue
    total_inserted += coin
    coins_inserted += 1
    print(f"Total inserted: {total_inserted}")
    if total_inserted >= snack_price:
        break

change = calculate_change(total_inserted, snack_price)
print(f"\nYou inserted {coins_inserted} coin(s).")
print(f"Total paid: {total_inserted}")
print(f"Change owed: {change}")
if change > 0:
    print("Please take your change.")
print("Enjoy your snack!")
