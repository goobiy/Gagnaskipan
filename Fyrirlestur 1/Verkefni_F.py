

number_of_pizzas = int(input())


pizzas = []
total_price = 0

for i in range(number_of_pizzas):
    pizza_and_price = input()
    split = pizza_and_price.split()

    pizzas.append(int(split[1]))


if len(pizzas) % 2 != 0:
    pizzas.pop(min(i))

else:
    pizzas.sort()
    pizzas.reverse()
    total_price += max(pizzas)


# óklárað

