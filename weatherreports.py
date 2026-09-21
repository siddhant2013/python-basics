# Part 1 - user input
city = input("Enter your city name: ")
temp = float(input("Enter todays' temperature in C:"))

# Part 2 if statement
if temp > 35:
    print("Warning: It is very hot today!")

    # Part 3 - if-else
if temp > 25:
        print("Great day to go outside!")

else:
        print("Grab a jacket before you go out!")
    # Part 4 - if-elif-else
if temp > 35:
        print("Weather:Scorching Hot")
elif temp > 25:
        print("Weather:Warm and Sunny")
elif temp > 15:
        print("Weather: Cool and Breezy")
else:
        print("Weather: Col d- Stay Warm!")

# Part 5 -datetime module
import datetime
import calendar

now = datetime.datetime.now()
print("City:", city)
print("Time now:", now)