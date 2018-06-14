####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Sweet n Shake "#complete me!
signature_flavors = ["Vegan chocolate beetroot", "Pumpkin", "carrot cake"]#complete me!
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    # your code goes here!
    print ("Our Menu: ")
    #print (menu)
    for item in menu: 
        #item,price gives us the key and value
        #to print out all the items in the menu
       #print (item)
       print  ("- %s (KD %s)" % (item, menu[item]))

def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    # your code goes here!
    #print (original_flavors)
    for item in original_flavors:
        print (item)
   

def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    # your code goes here!
    for items in signature_flavors:
      print ("- %s" % items)


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!
    #return true if valid order. We need to check
    #search in all different flavors and menu
    for item in menu:
        if (item == order):
            return True 

    for item in original_flavors:
        if (item == order):
            return True

    for item in signature_flavors:
        if (item == order):
            return True

    return False
""" 
 if order in menu:
     return True 

 elif order.....

 else:
    return False

     will only return keys not values
     you have to check manually for values in for loop
"""
     


def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    #user_order = ""
    # your code goes here!
    #recieve input from user and check if valid or not. If yes, then add to the list
    user_order = input ("What is your order?)(Enter the exact spelling of the item you want. Type 'Exit' to end your order.)\n")
    while user_order.lower() != "exit":
        if is_valid_order (user_order):
            order_list.append(user_order)
        else:
            print ("This is an invalid order. Please try again")

        user_order = input()

    return order_list
    #NEVER ENDING LOOP


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if total >= 5:
        return True

    else:
        return False

    #return total >=5


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!

    for item in order_list:
      if item in menu:
        total += menu[item]

      elif item in original_flavors:
       total += orignal_price

      elif item in signature_flavors:
       total += signature_price


    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    # your code goes here!
    for order in order_list:
        print (order)

    print ("\nYour total price is: KD %s" % get_total_price(order_list))

    if accept_credit_card (get_total_price(order_list)):
        print ("You can make the purchase using a credit card:")

    else:
        print ("you cannot make the purchase using a credit card")

    print ("Thank You for shopping at " + cupcake_shop_name) 