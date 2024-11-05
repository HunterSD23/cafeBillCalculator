SERVICE_TAX = 0.1

coffee = float(input("What is the price of the coffee? "))
pastry = float(input("What is the price of the pastry? "))
juice = float(input("What is the price of the juice? "))

def calculate_bill():
    price_all = coffee + pastry + juice
    service_multi = price_all * SERVICE_TAX
    totalbill = price_all + service_multi

returnbill = DISPLAY("Your total is: $", totalbill)