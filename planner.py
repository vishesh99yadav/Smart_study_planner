def plan(self):
        print("\n==========  AI STUDY MENTOR (REALISTIC + BALANCED) ==========")

        if not self.subjects:
            print(" No subjects found!\n")
            return

        total_subjects = len(self.subjects)

        print(f"\n I can see you’re handling {total_subjects} subjects.")
        print(" Don’t worry — we’ll plan this smartly without overloading you.\n")
        total_daily_hours = 6 if total_subjects >= 3 else 5

        print(f"You can study around {total_daily_hours} hours per day effectively.\n")

        weights = []

        for s in self.subjects:
            days = max(1, (datetime.strptime(s.exam_date,"%Y-%m-%d") - datetime.today()).days)
            diff = {"easy":1, "medium":2, "hard":3}.get(s.difficulty.lower(), 2)
            weak = 2 if s.weak else 0
            urgency = 2 if days <= 3 else 1 if days <= 7 else 0
            unit_load = s.units / days

            total = diff + weak + urgency + unit_load
            weights.append(total)

        total_weight = sum(weights)
        for i, s in enumerate(self.subjects):
            days = max(1, (datetime.strptime(s.exam_date,"%Y-%m-%d") - datetime.today()).days)

            weight = weights[i]
            subject_hours = (weight / total_weight) * total_daily_hours
            subject_hours = round(subject_hours, 2)
            print("\n----------------------------------------")
            print(f"Subject: {s.name}")
            print(f"{days} days left for exam")
            print(f"Total Units: {s.units}")

            print("\nWhat I suggest for you:")
             if s.difficulty.lower() == "easy":
                print("This subject is relatively easy for you.")
                print("Just keep it in your routine — don't ignore it completely.")
                elif s.difficulty.lower() == "medium":
                print("This subject needs consistent effort.")
                print("Not too hard, but skipping it can create pressure later.")
            else:
                print("This is a high-focus subject.")
                print("Give proper attention and try to understand concepts deeply.")
            if s.weak:
                print("You mentioned this is your weak subject.")
                print("Try revising it daily in small portions.")

            print(f"\nYou should give around {subject_hours} hours to this subject daily.")
