SERVICE_TAX = 0.1

coffee = float(input("What is the price of the coffee? "))
pastry = float(input("What is the price of the pastry? "))
juice = float(input("What is the price of the juice? "))

price_all = coffee + pastry + juice

service_multi = price_all * SERVICE_TAX

totalbill = price_all + service_multi

print("Your total is: $", totalbill)