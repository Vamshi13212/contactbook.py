import re
num = int(input("Enter No of Contacts: "))
names = []
phone_numbers = []
emails = []


for i in range(num):
    print(' ')
    name = input("Enter Name: ")
    
    while True:
      phone_number = input("Enter Phone Number: ")
      if not phone_number.isdigit(): 
          print ("Enter only numbers\n")
          continue
      elif len(phone_number) != 10:
          print ("Enter 10 digits\n")
          continue
      else: 
          break
    
#   pat = "^[a-zA-Z0-9]+@+gmail.com"
    pat = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    while True:
     email=input ("Enter Email: ")
     if re.match(pat,email):
      break
     else:
      continue  

    names.append(name.upper())
    phone_numbers.append(phone_number)
    emails.append(email)

print("\nName\t\t\tPhone Number\t\t\tEmail")
for i in range(num):
    print("{}\t\t\t{}\t\t\t{}".format(names[i], phone_numbers[i],emails[i]))

search_term = input("\nEnter search term: ")
if search_term in names:
    index = names.index(search_term)
    phone_number = phone_numbers[index]
    email = emails[index]
    print("Seach Results for: " + search_term)
    print("\nName\t\t\tPhone Number\t\t\tEmail")
    print("{}\t\t\t{}\t\t\t{}".format(search_term, phone_number, email))
else:
    print("Name Not Found")


delete_term = input("\nEnter delete name: ")
if delete_term in names:
    index = names.index(delete_term)
    names.pop(index)
    phone_numbers.pop(index)
    emails.pop(index)
    print("Deleted Successfully : " + delete_term)
else:
    print("Unable to delete, Name Not Found")

print("\nName\t\t\tPhone Number\t\t\tEmail")
for i in range(num-1):
    print("{}\t\t\t{}\t\t\t{}".format(names[i], phone_numbers[i],emails[i]))
