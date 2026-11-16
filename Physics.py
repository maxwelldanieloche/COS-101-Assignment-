# PHYSICS OPERATIONS CALCULATOR
# Function 1: Calculate Speed
def calculate_speed():
    distance = float(input("Enter distance (metres): "))
    time = float(input("Enter time (seconds): "))
    if time == 0:
        print("Time cannot be zero.")
    else:
        speed = distance / time
        print("Speed =", speed, "m/s")
# Function 2: Calculate Acceleration
def calculate_acceleration():
    final_velocity = float(input("Enter final velocity (m/s): "))
    initial_velocity = float(input("Enter initial velocity (m/s): "))
    time = float(input("Enter time (seconds): "))
    if time == 0:
        print("Time cannot be zero.")
    else:
        acceleration = (final_velocity - initial_velocity) / time
        print("Acceleration =", acceleration, "m/s²")
# Function 3: Calculate Force
def calculate_force():
    mass = float(input("Enter mass (kg): "))
    acceleration = float(input("Enter acceleration (m/s²): "))
    force = mass * acceleration
    print("Force =", force, "Newtons")
# Function 4: Calculate Work Done
def calculate_work():
    force = float(input("Enter force (Newtons): "))
    distance = float(input("Enter distance (metres): "))
    work = force * distance
    print("Work Done =", work, "Joules")
# Function 5: Calculate Power
def calculate_power():
    work = float(input("Enter work done (Joules): "))
    time = float(input("Enter time (seconds): "))
    if time == 0:
        print("Time cannot be zero.")
