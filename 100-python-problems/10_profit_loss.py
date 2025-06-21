#	Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit

def profit_loss():

    cp =  int(input("Enter cost price in Rs: "))
    sp =  int(input("Enter selling price in Rs: "))

    if sp >= cp:
      print("Profit")

    else:
      print("Loss")

profit_loss()