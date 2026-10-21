#List

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print("your list is:" + str(basket))

x = input("Enter a fruit to remove_1: ")
basket.remove(x)

y = input("Enter a fruit to remove_2: ")
basket.remove(y)

print("your list is after remove " + x + " and " + y + ":" + str(basket))

j = input("Enter a fruit to add: ")
basket.append(j)

m = input("Enter a fruit to add at the beginning: ")
basket.insert(0, m)

print("your list is after add " + j + " and " + m + ":" + str(basket))

g= input("Enter a fruit to count: ")
print("number is " + str(basket.count(g)))

s = input("you want to clear the list? (yes/no): ")
if s == "yes":
    basket.clear()
else:
    s == "no"
    basket
print(basket)
