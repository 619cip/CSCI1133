amt = float(input("Enter the loan amount in dollars: "))
N = int(input("Enter the loan duration in months: "))
r_percent = float(input("Enter the % monthly interest rate: "))
r = r_percent/100  #Convert from percent to decimal
payment = r*amt / (1 - ((1+r)**(-N)))
print("Your monthly payment is: $" + str(round(payment,2)))