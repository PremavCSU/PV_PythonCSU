''' The CSU Global Bookstore has a book club that awards points to its students based on the number of books purchased each month. The points are awarded as follows:

If a customer purchases 0 books, they earn 0 points.
If a customer purchases 2 books, they earn 5 points.
If a customer purchases 4 books, they earn 15 points.
If a customer purchases 6 books, they earn 30 points.
If a customer purchases 8 or more books, they earn 60 points.
Write a program that asks the user to enter the number of books that they have purchased this month and then display the number of points awarded. '''

# get input from user number of books purchased this month
NumberOfBooks_purchased = int(input("Enter how many books purchased this month: "))

 #If a customer purchased greater than or equal to 0 book and less than or equal to 1 book, 
 #print they earn 0 points.
if(NumberOfBooks_purchased >= 0 and NumberOfBooks_purchased <=1):
    print( "you have purchased", NumberOfBooks_purchased, "  Books this month & you earned 0 points" )

     #If a customer purchased greater than or equal to 2 books and less than or equal to 3 books, 
     #print they earn 5 points.
elif(NumberOfBooks_purchased >= 2 and NumberOfBooks_purchased <=3): 
    print("you have purchased", NumberOfBooks_purchased, " Books this month & you earned 5 points") 

     #If a customer purchased greater than or equal to 4 books and less than or equal to 5 books, 
     #print they earn 15 points.

elif(NumberOfBooks_purchased >= 4 and NumberOfBooks_purchased <=5): 
    print("you have purchased", NumberOfBooks_purchased, "  Books this month & you earned 15 points") 


#If a customer purchased greater than or equal to 6 books and less than or equal to 7 books, 
     #print they earn 30 points.
elif(NumberOfBooks_purchased >= 6 and NumberOfBooks_purchased <=7): 
    print("you have purchased", NumberOfBooks_purchased, "  Books this month & you earned 30 points") 


    #If a customer purchased greater than or equal to  books or more than 8 books
     #print they earn 60 points.
elif(NumberOfBooks_purchased >= 8): 
    print("you have purchased", NumberOfBooks_purchased, "  Books this month & you earned 60 points") 

