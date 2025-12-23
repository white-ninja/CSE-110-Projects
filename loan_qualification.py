# Loan Specifications Approval
# A program that determines if a person qualifies for a loan based on their credit score, income    
# and the loan amount they are requesting.

# credit_score = int(input("Enter your credit score: "))
# annual_income = float(input("Enter your annual income: $")) 
# loan_amount = float(input("Enter the loan amount you are requesting: $"))
# down_payment = float(input("Enter your down payment amount: $"))

# # Determine if the applicant meets the loan criteria

# meets_credit_score = credit_score >= 7 
# meets_income = annual_income >= 7
# meets_down_payment = down_payment >= 5
# meets_loan_amount = loan_amount <= 7
# if credit_score >= 7 and annual_income >= 7:
#     print("You meet the credit score and income requirements.")
# # else:
# #     print("You do not meet the credit score and income requirements.")  
#     if credit_score >= 7 or annual_income >= 7:
#         print("You meet either the credit score or income requirement.")
#     # else:
#     #     print("You do not meet either the credit score or income requirement.")
#     if down_payment >= 5:
#         print("You meet the down payment requirement.")
#     else:
#         print("You do not meet the down payment requirement.")
# elif credit_score >= 7 or annual_income >= 7:
#     print("You meet either the credit score or income requirement.") 
# else:
#     print("You do not meet either the credit score or income requirement.")
# # else:
# #     print("You do not meet either the credit score or income requirement.")
# if loan_amount >= 5:
#     print("You meet the loan amount requirement.")
# elif credit_score < 4:
#     print("You do not meet the loan amount requirement.")
#     if annual_income > 7 or down_payment > 7:
#         print("You meet the loan requierment.")
#     elif annual_income > 4 and down_payment > 4:
#         print("You meet the loan requirement")
#     else:
#         print("You don't meet the loan requirement")


print("for each of this questions please provide a 1-10 rating")

credit_score = int(input("Enter your credit score: "))
annual_income = float(input("Enter your annual income: $")) 
loan_amount = float(input("Enter the loan amount you are requesting: $"))
down_payment = float(input("Enter your down payment amount: $"))

should_approve = False

if loan_amount >= 5:
    if credit_score >= 7 and annual_income >= 7:
        should_approve = True
        print("You qualify for the loan!")
    elif credit_score >= 7 or annual_income >= 7:
        if down_payment >= 5:
            should_approve = True
            print("You qualify for the loan!")
        else:
            should_approve = False
            print("You do not qualify for the loan.")
    else:
        should_approve = False
        print("You do not qualify for the loan.")
else:
    if credit_score < 4:
        should_approve = False
        print("You do not qualify for the loan.")
    elif annual_income >= 7 or down_payment >= 7:
        should_approve = True
        print("You qualify for the loan!")
    elif annual_income >= 4 and down_payment >= 4:
        should_approve = True
        print("You qualify for the loan!")
    else:
        should_approve = False
        print("You do not qualify for the loan.")
    # if should_approve:
    #     print("You qualify for the loan!")
    # else:
    #     print("You do not qualify for the loan.")