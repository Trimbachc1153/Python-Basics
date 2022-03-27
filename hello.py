valid = False
while not valid:

    response = float(input("enter a number"))

    if response > 0:
         valid = True

    else:
        print("Please enter a valid number")
        print()