'''
Class that represents a database query, either specified from the command line
or entered in interpreter mode.
'''
class Query(object):
  def PrintMatches(self, listRecords, teacherRecords):
    raise NotImplementedError('Query subclass has not implemented PrintMatches')

class StudentQuery(Query):
  def __init__(self, lastname, bus=False):
    self.lastname = lastname
    self.bus = bus

  def PrintMatches(self, listRecords, teacherRecords):
    for listRecord in listRecords:
      if listRecord.studentLast == self.lastname:
        teacher = None
        for teacherRecord in teacherRecords:
          if teacherRecord.classroom == listRecord.classroom:
            teacher = teacherRecord
            break

        if not teacher:
          print 'No teacher found for %s %s in classroom %s.' % (
              listRecord.studentFirst,
              listRecord.studentLast,
              listRecord.classroom)
          return

        if self.bus:
          print '%s %s, Bus: %s' % (listRecord.studentFirst,
                                    listRecord.studentLast,
                                    listRecord.bus)
        else:
          print '%s %s, Grade: %s, Classroom: %s, Teacher: %s %s' % (
              listRecord.studentFirst,
              listRecord.studentLast,
              listRecord.grade,
              listRecord.classroom,
              teacher.teacherFirst,
              teacher.teacherLast)

class TeacherQuery(Query):
  def __init__(self, lastname):
    self.lastname = lastname

  def PrintMatches(self, listRecords, teacherRecords):
    for teacherRecord in teacherRecords:
      if teacherRecord.teacherLast == self.lastname:
        classroom = teacherRecord.classroom
        for listRecord in listRecords:
          if classroom == listRecord.classroom:
            print '%s %s' % (listRecord.studentFirst, listRecord.studentLast)

class GradeQuery(Query):
  def __init__(self, num, teacher=False):
    self.num = num
    self.teacher = teacher

  def PrintMatches(self, listRecords, teacherRecords):
    if self.teacher:
      # Find all classrooms for students of grade |self.num|.
      classrooms = set()
      for record in listRecords:
        if record.grade == self.num:
          classrooms.add(record.classroom)

      # Print all teachers who teach in any such classroom.
      for record in teacherRecords:
        if record.classroom in classrooms:
          print '%s %s' % (record.teacherFirst, record.teacherLast)
    else:
      for record in listRecords:
        if record.grade == self.num:
          print '%s %s' % (record.studentFirst, record.studentLast)

class BusQuery(Query):
  def __init__(self, num):
    self.num = num

  def PrintMatches(self, listRecords, teacherRecords):
    for record in listRecords:
      if record.bus == self.num:
        print '%s %s, Grade: %s, Classroom: %s' % (record.studentFirst,
                                                   record.studentLast,
                                                   record.grade,
                                                   record.classroom)

# TODO(andrew): Fill this shit in yo
class ClassroomQuery(Query):
  pass
