def log(self):
  print("\n    LOG STUDY     ")
  name = input("Subject: ")

  try:
    hours=float(input("Hours(example: 2 or 2.5): "))
  except:
    print("invalid input! Please enter number like 2 or 2.5\n")
    return

for s in self.subject:
  if s.name.lower() == name.lower():
    s.hours_done =+ hours
    self.history.append()  
