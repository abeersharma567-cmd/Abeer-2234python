# Smart School Day Planner

print("=== Smart School Day Planner ===")
print("Answer 3 quick questions and I will plan your day!\n")

day = input("What day is it? (Monday to Sunday): ").strip().capitalize()
weather = input("What is the weather? (sunny / rainy / cloudy): ").strip().lower()
homework = input("Is your homework done? (yes / no): ").strip().lower()

print()
print(f"=== Your Plan for {day} ===")
print("-" * 35)

# Topic 1 -- if-elif-else: classify the day
if day in ("Saturday", "Sunday"):
    print("Day type   : Weekend - enjoy your free time!")

elif day == "Monday":
    print("Day type   : Start of the week - stay focused!")

elif day == "Tuesday":
    print("Day type   : Regular school day - keep going!")

elif day == "Wednesday":
    print("Day type   : Midweek - you are halfway there!")

elif day == "Thursday":
    print("Day type   : Almost the weekend - stay productive!")

elif day == "Friday":
    print("Day type   : Last school day - finish strong!")

else:
    print("Day type   : Please enter a valid day.")

# Topic 2 -- weather
print()
print("Weather suggestion:")

if weather == "sunny":
    print("It is sunny! You can play outside or go for a walk.")

elif weather == "rainy":
    print("It is rainy! Stay indoors and study or play indoor games.")

elif weather == "cloudy":
    print("It is cloudy! You can enjoy some outdoor activities.")

else:
    print("Weather not recognized.")

# Topic 3 -- homework
print()
print("Homework status:")

if homework == "yes":
    print("Great! Your homework is done. You can relax after school.")

elif homework == "no":
    print("Finish your homework before spending too much time playing.")

else:
    print("Please enter yes or no for homework.")

# Final plan
print()
print("=== Final Daily Plan ===")
print("- Attend your classes and stay focused.")
print("- Complete your schoolwork.")
print("- Take short breaks while studying.")
print("- Spend some time relaxing or playing.")
print("- Prepare your school bag for tomorrow.")

print()
print("Have a productive day! 😊")
