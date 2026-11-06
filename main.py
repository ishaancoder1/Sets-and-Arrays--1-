basket1 = {"mango", "banana", "apple", "grape"}
basket2 = {"strawberry", "apple", "orange", "kiwi"}

print("Basket 1: ", basket1)
print("Basket 2: ", basket2)

basket1.add("watermelon")
print("Basket 1 after adding watermelon: ", basket1)

cmnfrts = basket1.intersection(basket2)
print(cmnfrts)

import array as arr
fruit_counts = arr.array('i', [3, 5, 2, 4])
print("Fruit counts arrray: ", fruit_counts)

fruit_counts.insert(0,1)
fruit_counts.append(5)
print("Fruit counts arrray: ", fruit_counts)

count_of_4 = fruit_counts.count(4)
print("Number of times 4 appears: ", count_of_4)

fruit_counts.reverse()
print("Reversed fruit counts array:", fruit_counts)

print("")
print("==== CLASS FRUIT BASKET ORGANIZER =====")
print("Basket 1:", basket1)
print("Basket 2:", basket2)
print("Shared Fruits", cmnfrts)
print("Fruits Reversed:", fruit_counts)