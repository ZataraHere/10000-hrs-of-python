#	Write a program that will convert celsius value to fahrenheit

def cel_to_fahrenheit():
    # 1'C = 33.8 F
    c = int(input("Enter temperature in °C :" ))
    f = (c * 1.8) + 32
    return f
print(f"Temperature is {cel_to_fahrenheit()} °F")