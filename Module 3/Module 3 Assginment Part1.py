#program that calculates the total amount of a meal purchased at a restaurant 

# Enter meal amount  
Meal_Amount = float(input("Enter your meal amount" ))

#Calculate sales Tax amount  
Tax_amount = float(Meal_Amount * .07 )

#calcualte tips 
Tips_amount = Meal_Amount * .18 

#calculate total cost 
Total_cost = Meal_Amount + Tax_amount + Tips_amount 

print("your sales tax amount is: " , format(Tax_amount, '.2f'))
print("Your tips amount is: ",format(Tips_amount,'.2f' ))
print("your total meal cost is:", format(Total_cost,'.2f'))
