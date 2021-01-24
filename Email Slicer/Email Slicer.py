email = input("Enter email ID:").strip()
index = email.index('@')

username = email[:index]
print("Username:" , username)

domain = email[index + 1:]
print("Domain:" , domain) 
