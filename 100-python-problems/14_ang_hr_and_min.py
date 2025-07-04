# Calculate angle between hour and minute hand
def get_angle(h, m):
    # Validate input
    if not (0 <= h <= 12 and 0 <= m < 60):
        print("Please provide valid hour (0–12) and minute (0–59) values.")
        return

    # Adjust 12 to 0 for angle calculation
    if h == 12:
        h = 0

    # Calculate angles
    hour_angle = 30 * h + 0.5 * m   # 360/12 = 30 degrees per hour, 0.5 per minute
    minute_angle = 6 * m           # 360/60 = 6 degrees per minute

    # Find the absolute difference
    angle = abs(hour_angle - minute_angle)

    # Return the smaller angle
    smaller_angle = min(angle, 360 - angle)
    print("Angle between the two hands is:", smaller_angle, "degrees")
