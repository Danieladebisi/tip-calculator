billAmount = int(input('What is your total bill? $'))
billPayers = int(input('How many people are paying? '))
tipPercentage = float(input('What is the tip percentage? '))

totalTipcal = tipPercentage + billAmount / 100
totalTip = totalTipcal / billPayers
tip = f'Each of you will pay ${totalTip} as tip'
print(tip)
