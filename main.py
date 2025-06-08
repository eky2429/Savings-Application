# Savings project script
standard_setting = [0.5, 0.3, 0.2]
other_setting = [0.5, 0.1, 0.4]

settings = [standard_setting, other_setting]


needs : float = 0.5
wants : float = 0.1
savings : float = 0.4

results : list = []

current_setting : int = 0

def process_input(s: float):
    #calculates value based on settings
    for col in settings[current_setting]:
        results.append(col * s)

    print("\nResults:")
    total: float = 0.0
    for i in range(0, len(results)):
        #Rounds each value
        results[i] = round(results[i], 2)
        total += results[i]
    #Round total because chance computer calculates extra decimal
    total = round(total, 2)

    print("Needs: " + str(results[0]))
    print("Wants: " + str(results[1]))
    print("Savings: " + str(results[2]))
    print("Is accurate: " + str(total == s))

    #Resets data in list
    results.clear()

def prompt_user(question : str) -> bool:
    while True:
        answer = input(question).lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Invalid input. Try again.")

#Handles settings to adjusting how much to distribute between needs, wants, and savings
def settings():
    print("This is your current setting: setting "  + str(current_setting))
    if prompt_user("Do you wish to change your setting? (y/n): "):
        while True:
            num = int(input("Okay, which setting would you like to use? (0 or 1): "))
            if num < 0 or num >= len(settings):
                print("Invalid number. Try again!")
            else:
                print("Excellent!")
                current_setting = num
                print("This is your current setting: setting "  + str(current_setting))
                break
    else:
        print("I understand.")
        print("Let us continue!")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #Greet user
    print("Hello, user!")
    print("This is the savings program")
    print("This will allow you to calculate how much to put into needs, wants, and savings.")
    print("So, here's how it works: type in a number, and then results will be outputted.")

    while True:
        #Give user option to adjust settings
        settings()

        #User inputs salary
        salary : float =  float(input("Input: "))
        
        #Results are printed
        process_input(salary)
        print()

        #If user does not want to contiunue, end program
        if not prompt_user("Do you wish to input another number? (y/n): "):
            break
    
    print("I understand\nHave a good rest of your day!\nGood-bye!")
