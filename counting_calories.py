burger_choice = int(input())
side_choice = int(input())
drink_choice = int(input())
dessert_choice = int(input())

if burger_choice == 1:
    burger_choice = 461
elif burger_choice == 2:
    burger_choice = 431
elif burger_choice == 3:
    burger_choice = 420
else:
    burger_choice = 0

if side_choice == 1:
    side_choice = 100
elif side_choice == 2:
    side_choice = 57
elif side_choice == 3:
    side_choice = 70
else:
    side_choice = 0

if drink_choice == 1:
    drink_choice = 130
elif drink_choice == 2:
    drink_choice = 160
elif drink_choice == 3:
    drink_choice = 118
else:
    drink_choice = 0

if dessert_choice == 1:
    dessert_choice = 167
elif dessert_choice == 2:
    dessert_choice = 266
elif dessert_choice == 3:
    dessert_choice = 75
else:
    dessert_choice = 0

total_calories = burger_choice + side_choice + drink_choice + dessert_choice

print(f'Your total Calorie count is {total_calories}.')
