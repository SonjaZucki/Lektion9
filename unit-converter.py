print("Hi! Welcome to the unit converter - that converts units!")

while True:
    km = int(input("Please enter the kilometers you want to convert: "))

    miles = km / 1.609344

    print("{0} kilometers are equal to {1} miles!".format(km, miles))

    choice = str(input("Would you like to convert another number (y/n)? "))

    if choice == "n":
        print("Okay, bye!")
        break
