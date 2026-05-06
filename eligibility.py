medical_cause = input("Do you have a medical cause? (y/n) ").lower().strip()

if medical_cause == 'y':
    print("You are eligible for the exam.")
elif medical_cause == 'n':
    attendance = input("Have you attended at least 75% of the classes? (y/n) ").lower().strip()
    if attendance == 'y':
        print("You are eligible for the exam.")
    elif attendance == 'n':
        print("You are not eligible for the exam.")
    else:
        print("Invalid input. Enter 'y' or 'n' please")
else:
    print("Invalid input. Enter 'y' or 'n' please")
