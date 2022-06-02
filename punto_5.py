# Program to calculate the median from a university student

"""Maximum grade: 20"""
number_1 = int(input("Please, introduce your first grade: "))
percentage_value_1 = int(input("Now, introduce the percentage value of your first grade: "))
number_2 = int(input("Please, introduce your second grade: "))
percentage_value_2 = int(input("Now, introduce the percentage value of your second grade: "))
number_3 = int(input("Please, introduce your third grade: "))
percentage_value_3 = int(input("Now, introduce the percentage value of your third grade: "))

print(f"Final result: {(percentage_value_1 + percentage_value_2 + percentage_value_3) * 20 / 100}")