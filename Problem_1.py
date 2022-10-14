from collections import deque

def pizza_valid(pizza):
    if 0 < pizza <= 10:
        return True
    return False


pizza_orders = deque([int(el) for el in input().split(', ')])
employees_capacity = [int(el) for el in input().split(', ')]

counter_pizzas = 0
while True:
    if len(pizza_orders) <= 0:
        break
    if len(employees_capacity) <= 0:
        break
    current_pizza = pizza_orders[0]
    current_employee = employees_capacity[-1]
    is_valid = pizza_valid(current_pizza)
    if is_valid:
        if current_pizza <= current_employee:
            counter_pizzas += pizza_orders[0]
            pizza_orders.popleft()
            employees_capacity.pop()

        elif current_pizza > current_employee:
            pizza_orders[0] -= employees_capacity[-1]
            counter_pizzas += employees_capacity[-1]
            employees_capacity.pop()

    else:
        pizza_orders.popleft()

if len(pizza_orders) == 0:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {counter_pizzas}')
    print(f'Employees: {", ".join(list(map(str, employees_capacity)))}')
else:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join(list(map(str, pizza_orders)))}')

