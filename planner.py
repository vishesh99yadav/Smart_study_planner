def plan(self):
        print("\n==========  AI STUDY MENTOR (REALISTIC + BALANCED) ==========")

        if not self.subjects:
            print(" No subjects found!\n")
            return

        total_subjects = len(self.subjects)

        print(f"\n I can see you’re handling {total_subjects} subjects.")
        print(" Don’t worry — we’ll plan this smartly without overloading you.\n")
