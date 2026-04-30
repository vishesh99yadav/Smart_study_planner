def log(self):
  print("\n    LOG STUDY     ")
  name = input("Subject: ")

  try:
    hours=float(input("Hours(example: 2 or 2.5): "))
  except:
    print("invalid input! Please enter number like 2 or 2.5\n")
    return

for s in self.subjects:
  if s.name.lower() == name.lower():
    s.hours_done =+ hours
    self.history.append({
      "subject":s.name,
      "hours":hours,
      "date": str(datetime.today().date()),
      "time":datetime.now().strftime(%H:%M:%S)})  
    self.save_date()
    print(f"{hours}hours logged Successfully\n")
    return
    print("Subject Not found\n")
    def history_view(self):
      print("\n         HISTORY            ")
      for h in self.history:
        print(f"{h[date]}{h['time']} {h['subject]} ({[hour']} hrs)")
