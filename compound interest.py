principle = 0
rate = 0
time = 0
while principle <= 0:
   principle = float(input("enter the principle amount"))
   if  principle <= 0:
        print("principle amount cannot be less than or equal to zero")
while rate <= 0:
  rate = float(input("enter the interest rate"))
  if  rate <= 0:
        print("interest rate cannot be less than or equal to zero")
while time <= 0:
  time = int(input("enter the time in years"))
  if  time <= 0:
        print("time cannot be less than or equal to zero")

total = principle * (1 + rate / 100) ** time
print(f"balance amount after {time} year/s: {total:.2f}")
