#Favorite Numbers

my_fav_numbers = {1, 3, 5, 7, 9}

x = int(input("Enter a number_fav1: "))
my_fav_numbers.add(x)

y = int(input("Enter a number_fav2: "))
my_fav_numbers.add(y)

z = int(input("Enter a number_remove: "))
my_fav_numbers.remove(z)

h= int(input("Enter a number_friend_1: "))
k= int(input("Enter a number_friend_2: "))
l= int(input("Enter a number_friend_3: "))
friend_fav_numbers = {h, k, l}

our_fav_numbers = my_fav_numbers | friend_fav_numbers

print("My favorite numbers:", my_fav_numbers)
print("Friend's favorite numbers:", friend_fav_numbers)
print("Our favorite numbers:", our_fav_numbers)