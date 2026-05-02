def load_users(self):
  try:
    with open("users.json","r", encoding="utf-8")as f:
      return json.load(f)
  except:
    return{}
def save_users(self):
  with open("users.json","w",encoding="utf-8")as f:
    json.dump(self.users,f,indent=4)
def login_system(self):
  self.users=self.load_users()

  while True:
  print("\n" + "="*60)
  print("USER AUTHENTICATION SYSTEM")
  print("="*60)
  print("1. Register New User")
  print("2. Login Existing user")
  print("3. Exit")

choice = input("\n Enter your choice:")

if choice == "1":
    print("\n REGISTER NEW USER")
    name = input("Enter username:")
    if name in self.users:
      print("User already exists!\n")
      continue
    password=input("Create password:")
    self.users[name]= password
    self.save_users()
    print(f"User'{name}'registered successfully!\n")
elif choice=="2.
print("/n LOGIN USER")
name=input("Username:")
password=input("Password:)

if name in self.user and self.users[name]==password:
   print(f"\n Welcome {name}!Login successful.\n")
   self.gile=f"{name}.json"
   self.student=student9name,"","")

