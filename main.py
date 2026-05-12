import json
from datetime import datetime
import time
import sys

# ================== CLASSES ==================

class Student:
    def __init__(self, name="", course="", university=""):
        self.name = name
        self.course = course
        self.university = university

    def to_dict(self):
        return self.__dict__


class Subject:
    def __init__(self, name, difficulty, exam_date, units, weak=False, hours_done=0):
        self.name = name
        self.difficulty = difficulty
        self.exam_date = exam_date
        self.units = units
        self.weak = weak
        self.hours_done = hours_done

    def to_dict(self):
        return self.__dict__


# ================== MAIN SYSTEM ==================

class StudyPlanner:

    def __init__(self):
        self.student = Student()
        self.subjects = []
        self.history = []
        self.users = {}
        self.file = None
        self.login_system()

    # ================== DATA ==================

    def load_data(self):
        try:
            with open(self.file, "r", encoding="utf-8") as f:
                data = json.load(f)

                self.history = data.get("history", [])

                if data.get("student"):
                    self.student = Student(**data["student"])

                return [Subject(**d) for d in data.get("subjects", [])]
        except:
            return []

    def save_data(self):
        data = {
            "student": self.student.to_dict(),
            "subjects": [s.to_dict() for s in self.subjects],
            "history": self.history
        }

        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    # ================== PROFILE ==================

    def create_profile(self):
        print("\n========== CREATE / UPDATE PROFILE ==========")
        self.student.name = input(" Name: ")
        self.student.course = input(" Course: ")
        self.student.university = input(" University: ")
        self.save_data()
        print(" Profile saved successfully!\n")

    def view_profile(self):
        print("\n========== PROFILE DETAILS ==========")
        print(f" Name       : {self.student.name}")
        print(f" Course     : {self.student.course}")
        print(f" University : {self.student.university}\n")

    # ================== ADD SUBJECT ==================

    def add_subject(self):
        print("\n========== ADD NEW SUBJECT ==========")

        name = input(" Subject Name: ")
        diff = input(" Difficulty (easy/medium/hard): ")
        date = input(" Exam Date (YYYY-MM-DD): ")

        try:
            units = int(input(" Total Units: "))
        except:
            print(" Invalid units!\n")
            return

        weak = input(" Weak subject? (yes/no): ").lower() == "yes"

        self.subjects.append(Subject(name, diff, date, units, weak))
        self.save_data()

        print(f" Subject '{name}' added!\n")


    def search(self):
        name = input("Search: ")
        for s in self.subjects:
            if name in s.name:
                print(s.__dict__)


    def report(self):
        print("\n========== REPORT ==========")

        with open("report.txt", "a", encoding="utf-8") as f:   # append mode
            f.write("\n========== STUDENT REPORT ==========\n")
            f.write(f"Name: {self.student.name}\n\n")

            for h in self.history:
                f.write(f"{h['date']} {h['time']} {h['subject']} {h['hours']}\n")

            f.write("\n" + "-"*40 + "\n")

    print(" Report appended successfully!\n")


    def today_task(self):
        print("\n========== TODAY TASK ==========")
        for s in self.subjects:
            print(f"Study {s.name}")


    def daily_check(self):
        today = str(datetime.today().date())
        print(" Studied today" if any(h["date"]==today for h in self.history) else " No study")


    def pomodoro(self):
        sec = int(input("Seconds: "))
        for i in range(sec,0,-1):
            print(f"{i} sec", end="\r")
            time.sleep(1)
        print("\nDone!\n")


    def menu(self):
        while True:
            print("\n SMART STUDY PLANNER")
            print("-"*40)
            print("1.Profile 2.View 3.Add 4.Plan 5.Log 6.History 7.Graph 8.Reminder")
            print("9.Search 10.Report 11.Pomodoro 12.Progress 13.Today 14.Streak 15.Suggest 16.Check 17.Login 0.Exit")
            print("-"*40)

            cmd = input(" Enter: ").lower()

            if cmd == "1": self.create_profile()
            elif cmd == "2": self.view_profile()
            elif cmd == "3": self.add_subject()
            elif cmd == "4": self.plan()
            elif cmd == "5": self.log()
            elif cmd == "6": self.history_view()
            elif cmd == "7": self.graph()
            elif cmd == "8": self.reminder()
            elif cmd == "9": self.search()
            elif cmd == "10": self.report()
            elif cmd == "11": self.pomodoro()
            elif cmd == "12": self.progress()
            elif cmd == "13": self.today_task()
            elif cmd == "14": self.streak()
            elif cmd == "15": self.smart_suggestion()
            elif cmd == "16": self.daily_check()
            elif cmd == "17": self.switch_user()
            elif cmd == "0":
                print(" Bye!")
                break


if __name__ == "__main__":
    StudyPlanner().menu()
