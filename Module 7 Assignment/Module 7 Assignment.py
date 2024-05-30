#creates a dictionary containing course numbers and the room numbers with key value pair
#Key-Value Pairs: Room Number
#Course Number (key) : Room Number (value)

# create a main funtion()
def main():
    Room_number_dict = { "CSC101":"3004", "CSC102" : "4501" , "CSC103" : "6755", "NET110" : "1244" , "COM241" : "1411" }


#create a dictionary containing course numbers and the names of the instructors that teach each course
#Key-Value Pairs: Instructors
#Course Number (key) : Instructor (value)

    Instructors_dict = { "CSC101":"Haynes", "CSC102" : "Alvarado" , "CSC103" : "Rich", "NET110" : "Burke" , "COM241" : "Lee"}


#create a dictionary containing course numbers and the meeting times of each course
#Key-Value Pairs: Meeting Time
#Course Number (key) : Meeting Time (value)

    Meeting_Time_dict = {"CSC101": "8:00 a.m.", "CSC102" : "9:00 a.m." , "CSC103" : "10:00 a.m.", "NET110" : "11:00 a.m." , "COM241" : "1:00 p.m."}

#Get course number from the user to get the course's room number, instructor, and meeting time.

    Couse_Number = (input("Enter your course number: ")).upper()
    
    # check course number is in the list
    # if it is not in the list, print "Enter correct coruse number" to get the correct course number
    if Couse_Number not in Room_number_dict:
       print("Enter correct coruse number")
    
    # if user enter the correct number print the details
    else:
  
    #print Course's Room Number, instructor and meeting time
     print("course's  Room Number is: ", Room_number_dict[Couse_Number])
     print("course's instructor is: ", Instructors_dict[Couse_Number])
     print("course's meeting time is: ", Meeting_Time_dict[Couse_Number])
     
main()




