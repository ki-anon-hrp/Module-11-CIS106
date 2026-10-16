# Kirill M11P2 10/16/2026

# Define function
def compute(exam_one, exam_two, exam_three):
# Finding sum of all exams in total points and average by dividing total points variable on 3
    total_points = exam_one + exam_two + exam_three    
    average = total_points /  3
    return total_points, average

# Entering last name, exam one, exam two, and exam three
last_name = input("Enter student last name: ")
exam_one = int(input("Enter exam one score: "))
exam_two = int(input("Enter exam two score: "))
exam_three = int(input("Enter exam three score: "))

# Calling for function compute
total_points, average = compute(exam_one, exam_two, exam_three)

# Printing final statement 
print(f"Last name student: {last_name}")
print(f"Total points: {total_points}")
print(f"Average: {average:,.2f}")