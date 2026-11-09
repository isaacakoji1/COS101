student_name = input("Student Name: ")
course_work_score = int(input("Coursework Score: "))
if course_work_score < 0 or course_work_score > 30:
    print("The coursework score must be between 0 and 30.")
    course_work_score = int(input("Coursework Score: "))

exam_score = int(input("Examination Score: "))
if exam_score < 0 or exam_score > 70:
    print("The examination score must be between 0 and 70.")
    exam_score = int(input("Examination Score: "))

total_score = course_work_score + exam_score
if total_score >= 70:
    grade = "A"
elif total_score >= 60:
    grade = "B"
elif total_score >= 50:
    grade = "C"
elif total_score >= 45:
    grade = "D"
elif total_score >= 40:
    grade = "E"
else:
    grade = "F"

if total_score >= 50:
    decision = "Pass."
else:
    decision = "Resit required."
print("Student Results")
print(f"Student Name: {student_name}.")
print(f"Coursework: {course_work_score}/30.")
print(f"Examination: {exam_score}/70.")
print(f"Total: {total_score}/100.")
print(f"Grade: {grade}")
print(f"Decision: {decision}")



    
    
                        
