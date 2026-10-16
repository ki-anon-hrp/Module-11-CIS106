# Kirill M11P4 10/16/2026

# Define function
def compute(score_one, score_two, score_three, handicap):
# Finding sum of all scores, average, and average with handicap
    sum_score = score_one + score_two + score_three
    average_score = sum_score / 3
    average_handicap = average_score + handicap
    return sum_score, average_score, average_handicap

# Entering last name, score one, score two, score three, and handicap
last_name = input("Enter bowler's last name: ")
score_one = int(input("Enter game score one: "))
score_two = int(input("Enter game score two: "))
score_three = int(input("Enter game score three: "))
handicap = int(input("Enter handicap: "))

# Calling for function compute
sum_score, average_score, average_handicap = compute(score_one, score_two, score_three, handicap)

# Printing final statement
print(f"Last name: {last_name}")
print(f"Average score: {average_score:,.2f}")
print(f"Average score with handicap: {average_handicap:,.2f}")