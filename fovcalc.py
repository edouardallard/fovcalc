from math import atan2, degrees, hypot

CM_PER_INCH = 2.54

inch = float(input("Enter your screen diagonal (in inches): "))
d_cm = float(input("Enter your distance to the screen (in cm): "))
ratio_1 = float(input("Enter your screen ratio (first number, e.g., 16): "))
ratio_2 = float(input("Enter your screen ratio (second number, e.g., 9): "))

diagonal_cm = inch * CM_PER_INCH
width_cm = diagonal_cm * (ratio_1 / hypot(ratio_1, ratio_2))
half_width_cm = width_cm / 2

fov_deg = 2 * degrees(atan2(half_width_cm, d_cm))

print(f"Your FOV is: {fov_deg:.2f}°")
