# fovcalc

A minimalist command-line utility in Python to calculate the mathematically accurate horizontal Field of View (hFOV) in degrees, based on physical screen dimensions and viewing distance. Built exclusively with the Python standard library (`math`) with zero external dependencies.

## Mathematical Formula

The script computes the physical width of the display panel from its diagonal and aspect ratio, then determines the viewing angle using standard trigonometry:

1. **Diagonal conversion:** Converts the screen diagonal from inches to centimeters (1 inch = 2.54 cm).
2. **Physical width:** Computes the true width using the ratio between the horizontal aspect component and the aspect ratio hypotenuse (`hypot(ratio_1, ratio_2)`):
   - `width = diagonal * (ratio_1 / hypot(ratio_1, ratio_2))`
3. **Horizontal FOV:** Calculates the total viewing angle in degrees from the half-width of the screen and the eye-to-screen distance (`atan2`):
   - `hFOV = 2 * degrees(atan2(width / 2, distance))`

## Requirements

* Python 3.x (standard library only)

## Usage

Run the script directly from your terminal:

```sh
python3 calcFOV.py
```

Enter the four physical parameters when prompted:

1. **Screen diagonal** in inches (e.g., `27`)
2. **Viewing distance** from eyes to screen in centimeters (e.g., `60`)
3. **Aspect ratio width** (first number, e.g., `16`)
4. **Aspect ratio height** (second number, e.g., `9`)

### Example

```text
Enter your screen diagonal (in inches): 27
Enter your distance to the screen (in cm): 60
Enter your screen ratio (first number, e.g., 16): 16
Enter your screen ratio (second number, e.g., 9): 9
Your FOV is: 52.96°
```

## License

This project is open-source and available under the [MIT License](LICENSE).
