print("\n<< Estimate Aldult's Height >>")
gender = input("\nEnter a gender (BOY / GIRL): ").lower()
FatherHeight = int(input("\nEnter father's height(cm): "))
MotherHeight = int(input("Enter mother's height(cm): "))

calculate = (FatherHeight + MotherHeight) / 2

if gender == 'boy':
    print(f"\nThe boy's height is: {calculate + 6.5}cm\n")
    
elif gender == 'girl':
    print(f"\nThe girl's height is: {calculate - 6.5}cm\n")
