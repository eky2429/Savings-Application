from decimal import Decimal

#This is the main file for my budget program
amount = float(input("How much did you make? "))
needs = amount * 0.5
wants = amount * 0.3
savings = amount * 0.2

print("Needs: " + str(needs))
print("Wants: " + str(wants))
print("Savings: " + str(savings))

elements_to_round = {"needs": 0, "wants": 0, "savings": 0}

if needs % 0.01 != 0:
    elements_to_round["needs"] = round(needs % 0.01, 3)

if wants % 0.01 != 0:
    elements_to_round["wants"] = round(wants % 0.01, 3)

if savings % 0.01 != 0:
    elements_to_round["savings"] = round(savings % 0.01, 3)

print("Stuff to round: " + str(elements_to_round) )

print("\nHave a good day! :)")