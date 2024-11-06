student={
'name':input("Enter the student's name:"),
'roll no':input("Enter the student's roll no:"),
'reg no':input("Enter the student's reg no:"),
'dept':input("Enter the student's dept:"),
'sem':input("Enter the student's sem:"),
}
print("Entered student details:",student)
total_mark=int(input("Enter the students total mark:"))
student['total_mark']=total_mark
if total_mark>=90:
    grade='A'
elif total_mark>=82:
    grade='B'
elif total_mark>=75:
    grade='C'
elif total_mark>=60:
    grade='D'
elif total_mark>=50:
    grade='P'
else:
    grade='F'
student['grade']=grade
print("\n Updated Student details:",student)
del student['roll no']
print("\nStudent details after deletion:",student)
