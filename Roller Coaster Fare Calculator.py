print("Welcome to the roller coaster ride!")
height = int(input("what is your height in cm?\n"))

if height >=120:
 print("You can take the ride!")
 age = int(input("What is your Age?\n"))
 if age < 12:
   bill = 5
   print("Child Tickets are $5.")
 elif age < 18:
   bill = 7
   print("Youth Tickets are $7.")
# for disaster affected people aged between 45-55, the management decides to offer them ride for free.
 elif age >= 45 and age <= 55:
   bill = 0
   print("Everything will be OK. You can get the ride for free!")   
 else:
   bill = 12
   print("Adult Tickets are $12.")

 Wants_Photo = input("Do you want to click a photo? Y or N\n")
 if Wants_Photo == "Y":
   if bill == 0:
    bill += 0
   else :
    bill += 3

 print(f"Your total amount to be paid is ${bill}")
 print("Enjoy your ride!")

else:
 print("Sorry, You have to grow more taller to take the ride.")