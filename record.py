'''
Class that represents one record in the database.
'''
class Record(object):
  def __init__(self, record):
    self.record = record.replace(', ', '#').strip().split('#')

'''
Class that represents one list record in the database.
'''
class ListRecord(Record):
  @property
  def studentLast(self):
    return self.record[0]

  @property
  def studentFirst(self):
    return self.record[1]

  @property
  def grade(self):
    return self.record[2]

  @property
  def classroom(self):
    return self.record[3]

  @property
  def bus(self):
    return self.record[4]

'''
Class that represents one teacher record in the database.
'''
class TeacherRecord(Record):
  @property
  def teacherLast(self):
    return self.record[0]

  @property
  def teacherFirst(self):
    return self.record[1]

  @property
  def classroom(self):
    return self.record[2]

