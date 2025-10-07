attempts = int(input("How many free throw attempts did you make?: "))
shots = 1
current_score = 0
for count in range(attempts):
    score = str(input(f"Shot {shots} (y/n)"))
    shots += 1
    if score == "y":
        current_score += 1
    else:
        current_score += 0
    print(f"current score is: {current_score}")
print(f"Final score: {current_score} out of {attempts}")