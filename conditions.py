# # conditions in python
# # if, else, else if, elif

# # How to accept input from user
# # The return datatype of input function is string
# environment = input("enter you env: ")
# print(environment, type(environment))

# # print(environment + 123) # Output: can only concatenate str (not "int") to str

# num = int(input("enter a number: "))
# print(num + 123)



# If the provided environment PROD, a change ticket is necessary
# For all other non-prod environments, it is not necessary to provide a change ticket
# For staging environment, user need to login with his credentials
# To debug issues on the PROD environment that are reported by the users, an incident ticket is necessary


# Indentation in python is very importenet
#It can be either a tab or 4 spaces

environment = input("Enter your environment: ")

environment = environment.upper()

change_ticket = False
if environment == "PROD":
    change_ticket = input("please enter your change ticket: ")
    if len(change_ticket) > 0:
        change_ticket = True
    if change_ticket:
        print("please proceed with your release activity")
    else:
        print("A change ticket for this release activity is mandatory")
elif environment == "STAGING":
    print("Please login with your credentials and proceed")
else:
    print("You are in non-PROD env")