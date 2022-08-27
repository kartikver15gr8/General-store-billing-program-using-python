amount = 0
li = []
while(True):
    cost = input("Enter the cost of the product\n")
    if(cost != "q"):
        amount += int(cost)
        print(f"The total amount till now is Rs{amount}/-")
        li.append(cost)
    elif(cost=="q"):
        print(f"The total bill is of Rs {amount}/-")
        print("Thanks for shopping, Have a great day today!")
        print(f"Your purchase summary is listed here{li}")
        break
