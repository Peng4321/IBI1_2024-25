#write a code to calculate the dosage of a drug based on the patient's weight and the recommended dosage per kg.
#the code contains several checks to ensure the security
def calculate_dosage(weight, dosage_per_kg): 
    # check if the weight is valid numbers
    if weight >= 10 and weight <=100 :
        # check if the dosage is valid numbers
        if dosage_per_kg == '120 mg/5ml'or dosage_per_kg == '120mg/5ml':
            dosage = weight * 15/120*5
            return dosage
        elif dosage_per_kg == '250 mg/5ml'or dosage_per_kg == '250mg/5ml':
            dosage = weight * 15/250*5
            return dosage
        else:
            print("Invalid dosage. Please enter '120 mg/5ml' or '250 mg/5ml'.")
            return None
    else:
        print("Invalid weight. Please enter a weight between 10 and 100 kg.")
        return None


weight = float(input("Enter the patient's weight in kg: "))
dosage_per_kg = input("Enter the dosage per kg (120 mg/5ml or 250 mg/5ml): ")
if calculate_dosage(weight, dosage_per_kg) is not None:
    print(f"The dosage of the drug is: {calculate_dosage(weight, dosage_per_kg)}ml")
else:
    print("Dosage calculation failed due to invalid input.")


