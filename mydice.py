email = input("Enter your full email : " ).strip()
#seperating the front name or user name
user_name = email[:email.index("@")]
#seperating the last name or domain name
domain_name = email[email.index("@")+1 :]
#printing directly
print("Your username is ' {} ' and service provider is ' {} ' .".format(user_name , domain_name))

