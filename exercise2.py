print ("Welcome to time greeter\n")
print("Please enter the time in 24 hour format\n")
hour = int(input("enter hour: "))
minute = int(input("enter minute: "))

print("you have entered {} hour and {} minute".format(hour,minute) )

if 0 <= hour < 12 and 0 <= minute < 60:
    print("good morning")
elif 12<= hour <18 and 0 <= minute < 60:
    print("good afternoon")
elif 18 <= hour <21 and 0 <= minute < 60:
    print("good evening")
elif 21 <= hour <24 and 0 <= minute < 60:
    print("good night")
else:
    print("invalid time")

#here we had take a perticular input from user and based on that input we are giving output 

#also this is manual way of taking time input from user




