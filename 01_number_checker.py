# functions go here
def num_check(question):


    # checks that users enter a number that is greater than zero
    valid = False
    while not valid:

        error = "Please enter a number more than zero eg: 1-9"

        try:
        
            # ask useer to enter a number
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

width = num_check("Width: ")








































