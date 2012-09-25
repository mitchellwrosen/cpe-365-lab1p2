import query
import record

import sys
import time

'''
Handles a database query of one of the following forms, printing the matching
records to sys.stdout:

  S[tudent]: <lastname> [B[us]]
  T[eacher]: <lastname>
  G[rade]: <number> [T[eacher]]
  B[us]: <number>
  C[lassroom]: <number> [T[eacher]]

args: Arguments to the query
listRecords: Records parsed from list.txt
teacherRecords: Records parsed from teachers.txt
'''
def HandleQuery(args, listRecords, teacherRecords):
  if not len(args):
    print 'Missing query arguments'
    return

  # Student query.
  if args[0] == 'S:' or args[0] == 'Student:':
    if len(args) == 2:
      q = query.StudentQuery(args[1])
    elif len(args) == 3 and (args[2] == 'B' or args[2] == 'Bus'):
      q = query.StudentQuery(args[1], bus=True)
    else:
      print SyntaxString('student')
      return

  # Teacher query.
  elif args[0] == 'T:' or args[0] == 'Teacher:':
    if len(args) == 2:
      q = query.TeacherQuery(args[1])
    else:
      print SyntaxString('teacher')
      return

  # Grade query.
  elif args[0] == 'G:' or args[0] == 'Grade:':
    if len(args) == 2:
      q = query.GradeQuery(args[1])
    elif len(args) == 3 and (args[2] == 'T' or args[2] == 'Teacher'):
      q = query.GradeQuery(args[1], teacher=True)
    else:
      print '%s' % SyntaxString('grade')
      return

  # Bus query.
  elif args[0] == 'B:' or args[0] == 'Bus:':
    if len(args) == 2:
      q = query.BusQuery(args[1])
    else:
      print SyntaxString('bus')
      return

  # Classroom query.
  elif args[0] == 'C:' or args[0] == 'Classroom:':
    if len(args) == 2:
      q = query.ClassroomQuery(args[1])
    elif len(args) == 3 and (args[2] == 'T' or args[2] == 'Teacher'):
      q = query.ClassroomQuery(args[1], teacher=True)
    else:
      print SyntaxString('classroom')
      return

  else:
    print 'Unknown query type "%s"' % args[0]
    PrintHelp()
    return

  q.PrintMatches(listRecords, teacherRecords)

'''
Returns the syntax of a |typeStr| Query.

typeStr: The Query's type.
'''
def SyntaxString(typeStr):
  try:
    return {
      'student': 'Syntax: S[tudent]: <lastname> [B[us]]',
      'teacher': 'Syntax: T[eacher]: <lastname>',
      'grade': 'Syntax: G[rade]: <number> [T[eacher]]',
      'bus': 'Syntax: B[us]: <number>',
      'classroom': 'Syntax: C[lassroom]: <number> [T[eacher]]',
    }[typeStr]
  except KeyError:
    raise NotImplementedError('Type %s missing syntax definition' % typeStr)

def PrintHelp():
  print 'Valid queries:'
  print '  S[tudent]: <lastname> [B[us]]'
  print '  T[eacher]: <lastname>'
  print '  G[rade]: <number> [T[eacher]]'
  print '  B[us]: <number>'
  print '  C[lassroom]: <number> [T[eacher]]'
  print 'Enter Q[uit] to quit.'

def main():
  listRecords = []
  teacherRecords = []

  # Populate list
  for rec in open('list.txt'):
    listRecords.append(record.ListRecord(rec))

  # Populate teachers
  for rec in open('teachers.txt'):
    teacherRecords.append(record.TeacherRecord(rec))

  # Batch mode.
  if len(sys.argv) > 1:
    HandleQuery(sys.argv[1:], listRecords, teacherRecords)
    return

  # Interactive mode.
  PrintHelp()
  line = sys.stdin.readline().strip()
  while line != 'Q' and line != 'Quit':
    HandleQuery(line.split(), listRecords, teacherRecords)
    line = sys.stdin.readline().strip()

if __name__ == '__main__':
  main()
