paint = int(input())  # how much paint do you have in liters
paint_per_badge = int(input())  # how many liters of paint is needed per badge
selling_price = int(input())  # how much money each cap can sell for

# determine the number of badges which can be painted with the paint
num_of_badges = paint // paint_per_badge

# determine how many liters of paint will be left over
leftover_paint = paint % paint_per_badge

# determine how much money can be made from the sale of the leftover paint
leftover_sale = leftover_paint * 1

# calculate the total profit
profit = num_of_badges * selling_price + leftover_sale

print(profit)
