
#create a ShoppingCart class
class ShoppingCart:

    #initialize the given customer_name, current_date and cart_items attributes
    customer_name = None
    current_date = None
    cart_items = []

    def __init__(self, name, date):
        self.customer_name = name
        self.current_date = date


  # create a add_item() to add items to the cart
  #It is has parameter ItemToPurchase. Does not return anything.

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

        
      # create a remove_item()  to the item from cart list
      #it has a item's name parameter and does not return anything 
    def remove_item(self, name):
       
       #check cart item range to remove item
       for i in range(self.cart_items):
        t = self.cart_items[i].split(":")
        if t[0]==name:

            #To remove the item use remove() method
            self.cart_items.remove(self.cart_items[i])
            break

        #if nothing in this cart, print Item not found in cart. Nothing removed.
        else:
            print("Item not found in cart. Nothing removed.")

        #create a modify_item()  to Modifies an item's description, price, and/or quantity
        #it had a  ItemToPurchase parameter and does not return anything
    def modify_item(self,ItemToPurchase):

       #check lengh of the cart items
        for j in range(len(self.cart_items)):
            t = self.cart_items[j].split(":")
            n = ItemToPurchase[0]   
            q = ItemToPurchase[1]     
            if t[0] == n:
                d = t[1]   
                p = t[2]  

                
              # keep price, quantity and descritions in the temperatoy files
                temp = n +":" + d + ":" + str(p) + ":" + str(q)
                self.cart_items.remove(self.cart_items[j])
                break
            # If item cannot be found (by name) in cart, output this message: "Item not found in cart. Nothing modified.""
            else:
               print("tem not found in cart. Nothing modified.")


   # create a get_num_items_in_cart() method to count quantity
   # It return the qunatity (c) and has no parameter

    def get_num_items_in_cart(self):
        c = 0 
        for k in range (len(self.cart_items)):
           t = self.cart_items[k].split(":")
           c += int(t[-1])
           return c


   # create get_cost_of_cart() method to calculate the total item cost
   #it will returns the total cost of items in cart. Has no parameters

    def get_cost_of_cart(self):
        totalCost = 0
        for i in range(len(self.cart_items)):
            n = self.cart_items[i].split(":")
            cost = int(n[-2]) * int(n[-1])
            totalCost += cost
        return totalCost

    # create a print_total() method to calculate total item in the cart

    def print_total(self):

        # If items is empty, print SHOPPING CART IS EMPTY message
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")

            #if there is a items, then print shopping cart output
        else:
            print("OUTPUT SHOPPING CART")
            print(self.customer_name + "'s shopping Cart - " + self.current_date)
            print("Number of items: ", end="")
            items = []

            #check the items length then use append() method to add item to the cart 
            for i in range(len(self.cart_items)):
                n = self.cart_items[i].split(":")
                items.append(int(n[-1]))
            print(sum(items))
            print()

            #calculate the cost and total cost 
            for i in range(len(self.cart_items)):
                n = self.cart_items[i].split(":")
                print(n[0] + " " + n[-1] + " @ $" + n[-2] + " = ", end="$")
                cost = int(n[-2]) * int(n[-1])
                print(cost)
            print()
            print("Total: $", end="")
            print(self.get_cost_of_cart())


   #create print_descriptions() to get each item's description

    def print_descriptions(self):
        print("OUTPUT ITEMS' DESCRIPTIONS")
        print(self.customer_name + "'s shopping Cart - " + self.current_date)
        print()
        print("Item Descriptions")

        for i in range(len(self.cart_items)):
            n = self.cart_items[i].split(":")
            print(n[0] + ": " + n[1])


# create a print_menu() function and add given list 
#And used "s" parameter to the items
def print_menu(s):
    while 1:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit\n")
        #Choose_an_option = input("Choose an option: ")
        no_of_items = []
        Choose_an_option = input("Choose an option:")
           
           #if user choose option a, them add items to the cart 
           #then ask item name, description, price and quantity
           #Then store these in temperaty files
        if Choose_an_option == "a":
                 print("Add item to cart")
                 print("")

                 #Get item name from users
                 name = input("Enter the item name: ")
                 print()

                 #Get item's description from user
                 description = input("Enter the item description: ")
                 print()

                 #get price details from user
                 price = int(input("Enter item price: "))
                 print()

                 #Get quantity from user
                 q = int(input("Enter the item quantity: "))

                 #store these in the temperaty files and add items to the "s"
                 temp = name + ":" + description + ":" +str(price) + ":" + str(q)
                 s.add_item(temp)


        #if user enter "r", print Remove item from cart
        #Get the name of item from user to remove from the cart and keep to "s"
        elif Choose_an_option == "r":
                 print("Remove item from cart")
                 print()
                 name = input("Enter the name to remove the item from cart")
                 s.modify_item(name)

       # if user enter "c", print Change item quantity
       #Get input from user to which item needs to be change 
       #get input from user the item qunatity 
        elif Choose_an_option == "c": 
                 print("Change item quantity: ")
                 print()
                 n = input("Enter item name to change: ")
                 q = int(input("Enter the itmem qunantity: "))
                 ItemToPurchase = [n,q]
                 s.modify_item(ItemToPurchase)
       
       #keep print_descriptions() to new cart "s"
        elif Choose_an_option == "i":
                s.print_descriptions()


       #keep print_total() to new cart "s"
        elif Choose_an_option == "o":
                 s.print_total()
                 break
        
        #if user entering other than the given list, print Invalid option

        else:
             print("Invalid option")
        

#This is the main section 
#get input from user the customer name and date 
#Call print_menu() in the main() function. 
#Continue to execute the menu until the user enters q to Quit.
def main():
    name = input("Enter the customer's name: ")
    date = input("Enter today's date: ")
    s = ShoppingCart(name, date)
    print_menu(s)


main()

