weight = int(input("enter your weight in pounds: "))
height = int(input("enter your height in inches: "))

BMI = (weight * 703) / (height * height)
print(BMI)

if BMI>0:
    if (BMI<18.5):
          print("you are underwight.")
    elif(BMI<=24.9):
         print("you are normal weight.")
    elif(BMI<29.9):
         print("you are overweight.")
    elif(BMI<=34.9):
         print("you are obese.")
    elif(BMI<39.9):
         print("you are severely obese.")
    else:
         print("you are morbidly obese.")    
else:
    print("Enter valid inputs")
