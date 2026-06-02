#create an emailid by taking users first and last as input and print the emailid by using formatted strings
firstname=str(input("enter firt name:"))
lastname=str(input("enter lastname:"))
email=firstname+lastname+"@gmail.com"
print(f"{email} is your email ID") #formatted string
print("this is your email ID:{}".format(email)) #string formatting
print("%s is your email ID"%(email)) #percentage formatting