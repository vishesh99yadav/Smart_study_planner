def log(self):
  print("\n    LOG STUDY     ")
  name = input("Subject: ")

  try:
    hours=float(input("Hour(example: 2 or 2.5): "))
  except:
    print("invalid input! Please enter number like 2 or 2.5\n")
    return
