def load_users(self):
  try:
    with open("user.json","r", encoding="utf-8")as f:
      return jsonload(f)
  except:
    return{}
      
      
