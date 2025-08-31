# Savings project script
settings: dict = {}
current_setting : str = ""
TAB = "   "

def process_input(s: float):
    global settings
    global current_setting
    results : dict = {}

    cur_set_data : dict= settings[current_setting]

    #calculates value based on settings
    for key in cur_set_data.keys(): #pair = {key: val}
        results[key] = cur_set_data[key] * s

    print("\nResults:")
    total: float = 0.0
    for key in results.keys():
        #Rounds each value
        results[key] = round(results[key], 2)
        total += results[key]
    #Round total because chance computer calculates extra decimal
    total = round(total, 2)

    for key in results.keys():
        print(key + ": " + str(results[key]))
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

def print_setting(key : str = ""):
    global current_setting
    global settings
    global TAB
    if key:
        print(key)
    else:
        print(current_setting)
        cur_set_data : dict = settings[current_setting] #{}
        for key in cur_set_data.keys():
            print(TAB + key + ": " + str(cur_set_data[key]))

#Handles settings to adjusting how much to distribute between needs, wants, and savings
def prompt_settings():
    global current_setting
    global settings

    print("This is your current setting: ")
    print_setting()

    if prompt_user("Do you wish to change your setting? (y/n): "):
        print("Okay, which setting would you like to use?")
        print("Here are the options: " + str(list(settings.keys())))
        while True:
            new_setting = input("Your option: ")
            if new_setting not in settings.keys():
                print("Invalid setting. Try again!")
            else:
                current_setting = new_setting
                print("Excellent!")
                print("This is your current setting: "  + str(current_setting))
                break
    else:
        print("I understand.")
        print("Let us continue!")

#Parses individual line
    #Assumes that the "sep" is part of "line"
def parse_line(line : str)-> tuple:
    sep = ": "
    part_list = list(line.partition(sep))
    for i in range(0, part_list.__len__()):
        part_list[i] = part_list[i].replace("\n", "")
    return (part_list[0], float(part_list[2]))

#Parses data from script
def parse_data() -> None:
    global current_setting
    file = open("presets.txt", "r")
    lines : list[str] = file.readlines()
    heading_str : str= "Heading: "
    def_set_str : str= "Default setting: "
    cur_key : str= ""

    for line in lines:
        if line.__contains__(heading_str): #This is the setting key
            cur_key = (line.removeprefix(heading_str)).removesuffix("\n")
            if not current_setting:
                current_setting = cur_key
        elif line.__contains__(def_set_str): #This is the default setting
            print("def")
            def_set = (line.removeprefix(def_set_str)).removesuffix("\n")
            if def_set.__len__() >= 3 and def_set in settings.keys(): #Min req. for a setting name
                print("Def 2")
                current_setting = def_set
        elif line == "\n":
            continue
        else: #This is a specific column for a setting
            value : tuple = parse_line(line)
            key1 : str = value[0]
            val1 : float = value[1]

            if cur_key in settings.keys():
                (settings[cur_key])[key1] = val1
            else:
                settings[cur_key] = {key1: val1}

    file.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #Parses data from script
    parse_data()
    print("Done parsing!", settings)


    #Greet user
    print("Hello, user!")
    print("This is the savings program")
    print("This will allow you to calculate how much to put into needs, wants, and savings.")
    print("So, here's how it works: type in a number, and then results will be outputted.")

    while True:
        #Give user option to adjust settings
        print(current_setting)
        prompt_settings()

        #User inputs salary
        salary : float =  float(input("Type in your salary: "))
        
        #Results are printed
        process_input(salary)
        print()

        #If user does not want to contiunue, end program
        if not prompt_user("Do you wish to input another number? (y/n): "):
            break
    
    print("I understand\nHave a good rest of your day!\nGood-bye!")
