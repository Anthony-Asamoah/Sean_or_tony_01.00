# python program to perform the following calculations
# Simple Interest
# Compound Interest
# Cummilative Deposit Compound Interest (susu)


class interest:
    def __init__(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time

    def __str__(self):
        return "cummilative ineterest calculator"

    # Utility Methods
    def percent(profit, net):
        percent = ((profit/net) * 100)
        return percent

    # End Of Utilities


    # Main Methods

    def simple(self):
        profit = (self.principal * self.time) * (self.rate / 100)
        net = profit + self.principal
        percent = interest.percent(profit, net)

        return f"profit = {round(profit, 2)} and NET = {net}\nprofit gained = {round(percent, 2)}%"
 
    def compound(self): 
        first = (1+ (self.rate/100)) **(self.time -1)
        net = self.principal * first
        profit = net - self.principal
        percent = interest.percent(profit, net)

        return f"profit = {round(profit, 2)} and NET = {round(net, 2)}\n profit gained = {round(percent, 2)}%"

    def susu(self):
        net = self.principal
        profit = 0

        for iterations in range(self.time):
            profit = net * (self.rate / 100)
            net += profit + self.principal
            print(f"period {iterations+1}: profit: {profit}, net: {net}")

        percent = interest.percent(profit, net)

        return f"profit = {round(profit,2)} and NET = {round(net,2)}.\n profit gained was {round(percent, 2)}%"

    # End of Main Methods

# Console Start

print('\n\n',' Interest Investigator | Powered by Wine & Python '.center(70, "_"), '\n\n')

while True:
    try:
        type = input("kindly enter letter 's' to calculate simple interest,\nletter 'c' for compound interest,\nand Capital 'C' for Cummilative Deposit Compound interest.\n\nOr 'q'/'Q' to quit\n\n-> ")
        
        if type.lower() == 'q':
                print("\n...Thanks for Using the Interest Investigator.\n\n\n")
                print(" Powered by Wine & Python ".center(70, "_"))
                break
        
        if type in ['c', 'C', 's',]:

            print("\nImportant Notice!!!\nInput must be numbers only.\n") 

            test = interest(
            int(input('Whats the Principal?\n -> ')),
            int(input('What about the Rate?\n -> ')),
            int(input('And the time intervals?\n -> '))
            )

            print("\n")

            if type.lower() == 's':
                print("Using Simple Interest".center(50, "."), "\n")
                print(test.simple())
                print("". ljust(50, "."), "\n\n")
            
            if type == 'c':
                print("Using Compound Interest".center(50, "."))
                print(test.compound())
                print("". ljust(50, "."), "\n\n")

            if type == 'C':
                print("Using Cummilative Deposit Compound Interest ".center(50, "."))
                print(test.susu())
                print("". ljust(50, "."), "\n\n")

            continue
            
        else: 
            print("\n\n*** Error: Invalid Input. Please read the instructions carefully***\n")
            continue

    except Exception as e:
        print("\n\nError: Invalid Input. Please read the instructions carefully\n")
        continue