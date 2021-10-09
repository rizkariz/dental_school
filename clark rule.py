# clark's rule

dose = int(input("What's the adult dose for the medicine in mg?:"))
weight = input("The weight of the body in lbs?(press ! to convert to kg)")
if weight == "!":
    weight_kg = int(input("Enter the weight in kg:"))
    weight = round((float(weight_kg )* 2.2))
else:
    weight = int(weight)

clark = round((weight/150) * dose)

print(clark , "is the dose for child.")

