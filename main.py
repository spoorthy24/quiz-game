from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank =[]
for qn in question_data:
    question1 =qn["text"]
    answer1 = qn["answer"]
    n_question = Question(question1, answer1)
    question_bank.append(n_question)
    # print(question_bank)
    # print(question_data[0])

quiz =QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score is {quiz.score}/{len(question_bank)}")