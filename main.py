# Savings project script
needs : float = 0.5
wants : float = 0.3
savings : float = 0.2

results : list = []

def process_input(s: float):
    results.append(needs * s)
    results.append(wants * s)
    results.append(savings * s)

    print("\nResults:")

    total: float = 0.0
    for i in range(0, len(results)):
        results[i] = round(results[i], 2)
        total += results[i]
    total = round(total, 2)

    print("Needs: " + str(results[0]))
    print("Wants: " + str(results[1]))
    print("Savings: " + str(results[2]))
    print("Is accurate: " + str(total == s))

def debug_process_input(s: float):
    results.append(needs * s)
    results.append(wants * s)
    results.append(savings * s)

    print("\nResults:")
    print("Needs: " + str(results[0]))
    print("Wants: " + str(results[1]))
    print("Savings: " + str(results[2]))

    total: float = 0.0
    for i in range(0, len(results)):
        total += results[i]
        results[i] = round(results[i], 2)
    print("Is accurate: " + str(total == s))

    print("\nRounded results:")
    total = 0.0
    for i in range(0, len(results)):
        total += results[i]
    total = round(total, 2)

    print("Needs: " + str(results[0]))
    print("Wants: " + str(results[1]))
    print("Savings: " + str(results[2]))
    print("Is accurate: " + str(total == s))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Hello, user!")

    print("This is the savings program")
    print("This will allow you to calculate how much to put into needs, wants, and savings.")
    print("So, here's how it works: type in a number, and then results will be outputted.")
    print("Input: ")

    salary : float =  float(input())
    process_input(salary)

    print("\nGood-bye")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
