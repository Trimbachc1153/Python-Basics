from this import d


def new_func():
    def num_check(question):


        # checks that users enter a number that is greater than zero
        valid = False
        while not valid:

            error = "Please enter a number more than zero"

            try:
            
                # ask user to enter a number
                response = float(input(question))

                # checks number is more than zero
                if response > 0:
                    return response

                #outputs error if input is invalid
                else:
                    print("Please enter a number more than zero")
                    print()

            except ValueError:
                print(error)



#calculate
    width = num_check("What is the width")
    height = num_check("what is the height")

    area = width * height
    perimeter = 2 *(width + height)

    print("To pay${:.2f}".format(area))
    print("perimeter: {} units".format(perimeter))

return new_func()