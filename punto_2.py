# This program asks for personal data to 3 users: full name, occupation, age, city, telephone number, and e-mail

""" 
Info from user_1 is gotten from the input function and 
stored in a tuple. The variable ends in '_1' 
to indicate that the data belong to user_1
"""
print("User 1")
full_name_1 = input("What is your name? ")
occupation_1 = input("What is your occupation? ")
age_1 = input("How old are you? ")
city_1 = input("Where do you live? ")
telephone_number_1 = input("What is your telephone number? ")
email_1 = input("What is your e-mail? ")
user_1 = (full_name_1, occupation_1, age_1, city_1, telephone_number_1, email_1)
print("-----------------------------\n")


""" 
Info from user_2 is gotten from the input function and 
stored in a tuple. The variable ends in '_2' 
to indicate that the data belong to user_2
"""
print("User 2")
full_name_2 = input("What is your name? ")
occupation_2 = input("What is your occupation? ")
age_2 = input("How old are you? ")
city_2 = input("Where do you live? ")
telephone_number_2 = input("What is your telephone number? ")
email_2 = input("What is your e-mail? ")
user_2 = (full_name_2, occupation_2, age_2, city_2, telephone_number_2, email_2)
print("-----------------------------\n")


""" 
Info from user_3 is gotten from the input function and 
stored in a tuple. The variable ends in '_3' 
to indicate that the data belong to user_3
"""
print("User 3")
full_name_3 = input("What is your name? ")
occupation_3 = input("What is your occupation? ")
age_3 = input("How old are you? ")
city_3 = input("Where do you live? ")
telephone_number_3 = input("What is your telephone number? ")
email_3 = input("What is your e-mail? ")
user_3 = (full_name_3, occupation_3, age_3, city_3, telephone_number_3, email_3)
print("-----------------------------\n")

""" Data is printed and parsed into lists"""
print("Personal Data User 1")
print(f"Info from user 1: {list(user_1)}")
print("#################################\n")
print("Personal Data User 2")
print(f"Info from user 2: {list(user_2)}")
print("#################################\n")
print("Personal Data User 3")
print(f"Info from user 1: {list(user_3)}")

