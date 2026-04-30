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
  printf("\n" + "="*60)
  print("USER AUTHENTICATION SYSTEM")
  print("="*60)
  print("1. Register New User")
  print("2. Login Existing user")
  print("3. Exit")
