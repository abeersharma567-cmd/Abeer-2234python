def total_calc(bill, tip_perc):
    tip = bill * tip_perc / 100
    total = bill + tip
    print("Total amount to pay:", total)

total_calc(100, 10)
