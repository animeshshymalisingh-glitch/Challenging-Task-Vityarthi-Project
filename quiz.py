questions = [
    ["Which language was used to create fb?", "Python", "French", "JavaScript", "Php", 4],
    ["What is the capital of India?", "Mumbai", "Delhi", "Chennai", "Kolkata", 2],
    ["What is 5 + 5?", "10", "11", "25", "55", 1],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Venus", "Jupiter", 2],
    ["Which language was used to create fb?", "Python", "French", "JavaScript", "Php", 4]
]

score = 0

# Loop through the questions using range
for i in range(0, len(questions)):
    
    q = questions[i]

    print()
    print("Question", i+1)
    print(q[0])
    print("1.", q[1])
    print("2.", q[2])
    print("3.", q[3])
    print("4.", q[4])

    # asking for input
    ans = int(input("Enter choice (1-4) or 0 to quit: "))

    if ans == 0:
        print("Quitting game")
        break
    
    if ans == q[5]:
        print("Correct Answer!")
        score = score + 10
    else:
        print("Wrong Answer!")
        break

print("Final Score:", score)