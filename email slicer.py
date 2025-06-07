email = input("Enter your email: ")
index = email.index("@")
username =email[:index]
domain =email[index:]
print(f"your username is {username} and your domain is {domain}")
