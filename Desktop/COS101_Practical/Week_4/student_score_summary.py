
student_number = int(input("Number of students: "))
while student_number <= 0:
    print("The number of students must be greater than 0.")
    student_number = input("Number of students: ")
    
    
total_score = 0
pass_count = 0
fail_count = 0


for student_number in range(1, student_number + 1):
    student_score = float(input(f"Enter score for student {student_number}: "))
    while student_score < 0 or student_score > 100:
        print("The score must be between 0 and 100. Enter a valid score.")
        student_score = float(input(f"Enter score for student {student_number}: "))
    total_score += student_score

    if student_score >= 50:
        pass_count += 1
    else:
        fail_count += 1

        



average_score = total_score/student_number

print("Class result summary")
print(f"Number of students: {student_number}")
print(f"Total score: {total_score}")
print(f"Average score: {average_score}")
print(f"Number of passes: {pass_count}")
print(f"Number of failures: {fail_count}")
        
                          
    
