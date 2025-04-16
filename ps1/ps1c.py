## 6.100A PSet 1: Part C
## Name:
## Time Spent:
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Enter the initial deposit: "))


#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
cost_of_house = 800000
portion_down_payment = 0.25
months = 36


##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################
if initial_deposit >= cost_of_house * portion_down_payment - 100:
    r = 0.0
    steps = 1
elif initial_deposit * (1 + 1/12) ** months <= cost_of_house * portion_down_payment - 100:
    r = None
    steps = 0
else:
    low = 0
    high = 1
    r = (low + high) / 2.0
    amount_saved = initial_deposit * (1 + r/12) ** months
    steps = 1
    while abs(amount_saved - cost_of_house * portion_down_payment) >= 100:
        if amount_saved - cost_of_house * portion_down_payment >= 100:
            high = r
        else :
            low = r
        r = (low + high) / 2.0
        amount_saved = initial_deposit * (1 + r/12) ** months
        steps += 1
print(f"Best savings rate: {r} [or very close to this number]")
print(f"Step in bisection: {steps}")

