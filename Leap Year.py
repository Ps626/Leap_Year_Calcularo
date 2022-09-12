print("Welcomr to the leap year application. ")
year = int(input("Please eanter the year. "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:       
            print("Leap Year.")
        else:
            print("Not Leap Year.")  
    else:  
        print("Leap year")     
else: 
    print("Not a leap year.")           