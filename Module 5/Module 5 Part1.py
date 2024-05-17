'''        
Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years. 
The program should first ask for the number of years. The outer loop will iterate once for each year. 
The inner loop will iterate twelve times, once for each month. 
Each iteration of the inner loop will ask the user for the inches of rainfall for that month. After all iterations, 
the program should display the number of months, the total inches of rainfall, and the average rainfall per month for the entire period


'''
# get number of year input from users 
Years = int(input("Enter the number of years"))

# set Total month is 12
Number_of_months = 12 

 # set initial raintall is 0
 # set average rainfall is 0
Total_rainfall = 0.0
Average_rainfall = 0.0

# check user give valid year ((less than 0 or greater than 12 ). 
#if it is not valid year print it is not a valid year

if (Years < 1):
    print("Invalid years: 'Enter correct year'")
    
      
    #if user give valid year continue from else
else:
       #check year range
    for year in range(Years):   
        #print years 
        print("For Year:", year + 1, end='')

        #check month range
        for month in range(Number_of_months):

            #rprint number of months one by one
            print("\nEnter the inches rainfall for month:", month + 1)
          
           #get Rainfall in inches from user per month
            Rainfall_inches = float(input("How many inches rainfall in month:"))
          
           #calculate total rainfall
            Total_rainfall = Total_rainfall + Rainfall_inches

            #calculate total month
            Total_month = Number_of_months * Years 

            #calculate average rainfall
            Average_rainfall = Total_rainfall / Total_month 
    

    #print number of  month
    #print the total inches of rainfall
    #print the average rainfall per month for the entire period
    print("\nTotal number of month:", Total_month)
    print("The total inches of rainfall: ", Total_rainfall)
    print("The average rainfall per month for the entire period:", Average_rainfall)
