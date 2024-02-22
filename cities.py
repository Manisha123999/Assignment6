cities = []
for i in range(5):
    city = input("Enter the name of city {}: ".format(i + 1))
    cities.append(city)
print("Cities entered:")
for city in cities:
    print(city)