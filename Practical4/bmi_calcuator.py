#To calculate the BMI value of a person and output the BMI value and the grade of the person
#First we need to collect the weight and height of the person
#Then we calculate the BMI value using the formula weight/(height^2)
#Then we check the BMI value and assign a grade to the person
#Finally we output the BMI value and the grade of the person
weight=float(input('kg:'))
height=float(input('m:'))
bmi =  weight/(height**2)
if bmi<18.5:
    grade='Underweight'
elif bmi<25 and bmi>=18.5:
    grade='Normal weight'
else:
    grade='Overweight'
bmi=round(bmi,2) #round the BMI value to 2 decimal places
print(f'Your BMI is {bmi} and you are {grade}') #output the BMI value