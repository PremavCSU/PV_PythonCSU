
#nter the current time, given example hour is 13 hours

Current_time = float(input("Enter your current time in hours"))

#Enter no of wait hours for the alarm, given example is 50 hours 
Alarm_time = float(input("Enter your number of wait hours for the alarm"))

#Time need to be calculate for 24 hours format, example mentioned 13 hours
#example given is set Alarm go off in 50 hours
# From given example alarm will goes off at (13 +50) % 24 = 15 hours 
Alarm_off_time = ( Current_time + Alarm_time ) % 24 

#Print the output for alarm off time in hours
print("Alarm will go off at", Alarm_off_time, "hours")


