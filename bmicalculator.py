Height=float(input("Enter your height in centimeter: "))
Weight=float(input("Enter your weight in Kg : "))
Height=Height/100
BMI= Weight/(Height*Height)
print("Your Body Mass Index is : ", BMI)
if(BMI > 0):
  if(BMI <=16):
      print("You are severely underweight")
  elif(BMI <= 18.5):
      print("You are underweight")
  elif(BMI <=25):
      print("You are Healthy")
  elif(BMI<=30):
      print("You are overweight")
  else: print("You are Severely overweight")
else:
  print("Enter valid details ")