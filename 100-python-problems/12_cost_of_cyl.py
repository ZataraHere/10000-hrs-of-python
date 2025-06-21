#	Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk is 40Rs.

def vol_cyl():
     
     r = float(input("Radius of cylinder in cm: "))
     h = float(input("Height of cylinder in cm: "))

     V = 3.14 * (r**2) * h
     # cost = rs 40/L
     cost = 40*V
     return V, cost

V, cost = vol_cyl()
print(f"Volume of cylinder is: {V} cm³ and cost of milk is: Rs {cost:.2f}")