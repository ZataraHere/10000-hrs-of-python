#1.	User will input (3ages).Find the oldest one
def max_of_3ages():
    person_1_age = int(input("Enter the age of first person: "))
    person_2_age = int(input("Enter the age of second person: "))
    person_3_age = int(input("Enter the age of third person: "))

    max_age = person_1_age

    if person_2_age > max_age:
        max_age = person_2_age
    if person_3_age > max_age:
        max_age = person_3_age

    return max_age

# Call the function
print("The oldest age is:", max_of_3ages())

