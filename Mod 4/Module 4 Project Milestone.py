# step 1: Build the ItemToPurchase class with the following specifications:
# Online Shopping Cart 

#create ItemToPurchase 
class ItemToPurchase:

    # default constructor 
    #initialize the given item 
    #Initializes item's name = "none", item's price = 0, item's quantity = 0
    def __init__(self, item_name = "none", item_price = 0, item_quantity = 0):
          
        #given attributes 
        self.item_name = item_name 
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
       
        #print item cost method 
         #To calculate the cost, multiply item price and item cost
                      

        # Bottled Water 10 @ $1 = $10
        #Chocolate Chips 1 @ $3 = $3
      
     print('{0} {1} @ ${2} = ${3}' .format(self.item_name, self.item_price, self.item_quantity, (self.item_quantity * self.item_price)))   

      #step 2 
      #In the main section of your code, prompt the user for two items and create two objects of the ItemToPurchase class.
    #item 1 
    #item 1 main section       

if __name__ == "__main__": 
      
    print("This is Item 1")

     #get Name, Price and Quantity input from the user for Item 1. 
    Name1 = input("Enter the item 1 name")    
    Price1 = int(input("Enter the item 1 price"))
    Quantity1 = int(input("Enter the item 1 quantity"))  

     #create a object to ItemToPurchase class 

    obj_Item1 = ItemToPurchase(Name1, Price1, Quantity1)
    

    #
    print("\nThis is Item 2")
     
     #get Name, Price and Quantity input from the user for Item 2
    Name2 = input("Enter the item 2 name")   

    #price I added in integer format, if added float, output format will diffent than given format. 
    Price2 = int(input("Enter the item 2 price"))  
    Quantity2 = int(input("Enter the item 2 quantity"))  

     #create a object to ItemToPurchase class 

    obj_Item2 = ItemToPurchase(Name2, Price2, Quantity2)    

 
   #To calculate the total price, multiply item price and item quantity
    TOTAL_COST = ((obj_Item1.item_price * obj_Item1.item_quantity ) + (obj_Item2.item_price * obj_Item2.item_quantity) )
    

     
    #print()
    
 # Step 3: Add the costs of the two items together and output the total cost.
     #print item1 with given format 
    item1 = obj_Item1.print_item_cost()

    #print item2 with given format
    items2 = obj_Item2.print_item_cost()
    
    #print the item1 with given format
    print(item1)

      #print the item2 with given format
    print(items2)


 #print total cost
    print("Total Cost:", "$",TOTAL_COST)



