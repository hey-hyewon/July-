July = "Julio"
"""This is a code which asks the user to guess what July is in Spanish. 
It checks the user's input and provides feedback based on their answer."""

print("Hello! Guess what July is in Spanish!")
answer = input("I guess it's: ")
user_input = input("Press enter to continue...")
while user_input:
    print("You didn't press enter. Please try again.")
    user_input = input("Press enter to continue...")

    if answer in ["Julio", "julio", "JULIO"]:
        print("Correct! Julio is July in Spanish.")
    else:
        print("Too bad. The correct answer is Julio.")