# functions go here
def num_check(question):


    # checks that users enter a number that is greater than zero
    valid = False
    while not valid:

        error = "Please enter a number more than zero eg: 1-9"

        try:
        
            # ask user to enter a number
            response = float(input(question))

            # checks number is more than zero
            if response > 0:
                return response

            #outputs error if input is invalid
            else:
                print("Please enter a number more than zero eg: 1-9")
                print()

        except ValueError:
            print(error)

# main routine goes here
keep_going = ""
while keep_going == "":


    width = num_check("Width: ")
    height = num_check("height: ")

    area = width * height

    perimeter = 2 * (width + height)

    print("Perimeter: {} units".format(perimeter))
    print("Area: {} square units".format(area))

    keep_going = input("press <enter> to keep going or any key to quit")

print()
print("thanks for using my area / perimeter calculer")


































