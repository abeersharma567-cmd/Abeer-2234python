def cube(num):
    return num ** 3

def check_number(num):
    if num % 3 == 0:
        print("Cube:", cube(num))
    else:
        print("Number is not divisible by 3")

check_number(6)
