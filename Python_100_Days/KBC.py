# Create a KBC (Kaun Banega Crorepati) game in Python

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Paris", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Mars", "Jupiter", "Saturn", "Uranus"],
        "answer": "Jupiter"
    }
]

print("Welcome to Kaun Banega Crorepati!")
level = [0, 1,2,3,4]
for i in range(0, len(questions)):
    print(f"Question {i + 1}: {questions[i]['question']}")
    for j in range(0, len(questions[i]["options"])):
        print(f"{j + 1}. {questions[i]['options'][j]}")
    answer = input("Enter your answer (1-4): ")
    if questions[i]["options"][int(answer) - 1] == questions[i]["answer"]:
        print("Correct!")
        level[i] = 1
        if level[i]==1:
            print("You have won 1000$")
    else:
        print("Incorrect!")
        level[i] = 0
