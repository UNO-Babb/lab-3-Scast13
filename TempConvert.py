#TempConvert.py
#Name:
#Date:
#Assignment:



  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature. 
unit = input("Is your temperature in Celcius or Fahrenheit (C/F):")  
temp = float(input("Enter the tempurature: "))

if unit == "C":
  temp = round((9 * temp) / 5 + 32, 1)
  print(f"The temperature in Fahrenheit is: {temp} degress F")
elif unit == "F":
  temp = round((temp - 32) * 5 / 9, 1)
  print(f"The temperature in Celcius is: {temp} degress C")
else:
  print(f"{unit}is an invalid unit of measurement")

