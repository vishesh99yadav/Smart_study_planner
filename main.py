import json
from datetime import datetime
import time
import sy

class student:
  def __init__(self,name="",course="",university=""):
    selt.name = name
    self.course = course
    self.university = university

  def to_dict(self):
    return self.__dict__

class subject:
  def __init__(self,name,difficulty,exam_date,units,weak=False,
hour_done=0):
    self.name = name
    self.difficulty = difficulty
    self.exam_date = exam_date
    self.units = units
    self.weak = weak
    self.hours_done = hours_done

 def to_dict(self):
   return self.__dict__

class studyplanner:
  def __init__(self):
    self.student = students()
    self.subjects = []
    self.history = []
    self.users = {}
    self.file = None
    self.login_system()

  def load_data(self)
    


