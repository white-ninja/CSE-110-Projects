print("Please enter the following information:")
print()

first_name = input("First Name: ")
last_name = input("Last Name: ")
email_address = input("Email Address: ")
phone_number = input("Phone Number: ")
job_title = input("Job Title: ")
id_number = input("ID Number: ")

print("\nThe ID Badge is:\n")
print("-----------------------------------------")
print(f"{last_name.upper()} {first_name.capitalize()}")
print(f"{job_title.title()}")           
print(f"ID: {id_number}")   
print(f"Email: {email_address.lower()}")
print(f"Phone: {phone_number}")
print("-----------------------------------------")

