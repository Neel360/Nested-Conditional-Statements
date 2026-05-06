ride = input("Would you like a bike or a motor-vehicle? (bike/motor-vehicle) ").lower().strip()

if ride == 'bike':
    print("Okay, which type of bike do you want? (mountain/road/BMX)")
    bike_type = input().lower().strip()
    if bike_type == 'mountain':
        print("You have chosen a mountain bike.")
    elif bike_type == 'road':
        print("You have chosen a road bike.")
    elif bike_type == 'bmx':
        print("You have chosen a BMX bike.")
    else:
        print("You have entered an invalid bike type. Make sure to enter 'mountain', 'road', or 'BMX'.")
elif ride == 'motor-vehicle':
    print("Okay, which type of motor-vehicle do you want? (car/motorcycle/truck)")
    motor_vehicle_type = input().lower().strip()
    if motor_vehicle_type == 'car':
        print("You have chosen a car.")
    elif motor_vehicle_type == 'motorcycle':
        print("You have chosen a motorcycle.")
    elif motor_vehicle_type == 'truck':
        print("You have chosen a truck.")
    else:
        print("You have entered an invalid motor-vehicle type. Make sure to enter 'car', 'motorcycle', or 'truck'.")
else:
    print("Please choose an option listed above. Make sure to enter 'bike' or 'motor-vehicle'.")
    