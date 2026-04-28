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
             print("\nHow you should study:")
            print("Don't try to complete full units in one go.")
            print("Break units into small topics and cover step by step.")
            print("Study in 2-3 sessions instead of one long sitting.")

            if days <= 3:
                print("\nVery less time left.")
                print("Focus more on revision, PYQs, and important topics.")
            elif days <= 7:
                print("\nTime is limited now.")
                print("Stay consistent daily — avoid skipping.")
            else:
                print("\nYou have enough time.")
                print("Build concepts slowly without rushing.")
                 print("\nReality check:")
            print("You don't need to be perfect in everything.")
            print("Just stay consistent — that's enough.")

            print("----------------------------------------")

        print("\nFinal Advice (Important):")
        print("Don't give all your time to one subject only.")
        print("Even easy subjects need revision.")
        print("Hard subjects need focus — but in limited blocks.")
        print("Smart balance is better than over-studying.\n")


    def reminder(self):
        print("\n========== AI SMART REMINDER ==========\n")
         if not self.subjects:
            print("No subjects found!\n")
            return

        today = datetime.today()

        for s in self.subjects:
            days = max(1, (datetime.strptime(s.exam_date, "%Y-%m-%d") - today).days)

        print(f"{s.name}")
        if days <= 2:
            print("Exam is very close!")
            print("Focus only on revision + important topics now.")
        elif days <= 5:
            print("Time is limited.")
            print("Don't skip this subject today.")
        else:
            print("You still have time.")
            print("Build concepts slowly.")

        # difficulty based
        if s.difficulty.lower() == "hard":
            print("This is a tough subject — give it deep focus.")
        elif s.difficulty.lower() == "easy":
            print("This is easy — just revise to stay confident.")
         if s.weak:
            print("You marked this as weak — revise daily in small parts.")

        # smart suggestion
        print("Suggestion:")
        print("Study in 2 sessions instead of one long sitting.")
        print("Avoid distractions and focus on understanding.\n")

        print("-"*40)

        def smart_suggestion(self):
        print("\n========== SUGGESTION ==========")
        for s in self.subjects:
            if s.weak:
                print(f"Focus {s.name}")
