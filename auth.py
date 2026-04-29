def load_users(self):
  try:
    with open("users.json","r", encoding="utf-8")as f:
      return json.load(f)
  except:
    return{}
def save_users(self):
  with open("users.json","w",encoding="utf-8")as f:
    json.dump(self.users,f, indent=4)
