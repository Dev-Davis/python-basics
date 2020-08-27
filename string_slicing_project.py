# input the email of the user
email = input("Enter your email? ")

# slice the name from the email
username = email[:email.index("@"):]
domain = email[email.index("@"):email.index("."):]


# print the info of the user
print("Your name is {} and your email domain is {}".format(username, domain))
