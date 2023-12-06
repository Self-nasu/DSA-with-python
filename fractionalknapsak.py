class Item:
   def __init__(self, weight, value):
       self.weight = weight
       self.value = value
       self.ratio = value / weight

def fractional_knapsack(items, capacity):
   sorted_items = sorted(items, key=lambda x: x.ratio, reverse=True)

   total_value = 0.0
   knapsack = [0] * len(items)

   for item in sorted_items:
       if capacity <= 0:
           break

       if capacity >= item.weight:
           knapsack[items.index(item)] = 1
           total_value += item.value
           capacity -= item.weight
       else:
           fraction = capacity / item.weight
           knapsack[items.index(item)] = fraction
           total_value += fraction * item.value
           capacity = 0

   return total_value, knapsack

items = [
   Item(10, 60),
   Item(20, 100),
   Item(30, 120)
]
knapsack_capacity = 50

max_value, selected_items = fractional_knapsack(items, knapsack_capacity)

print(f"Maximum value in knapsack: {max_value}")
print("Selected items:")
for i, item in enumerate(selected_items):
   if item > 0:
       print(f"Item {i+1}: {item:.2f} fraction")