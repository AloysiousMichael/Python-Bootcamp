from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for question in question_data:
    question_test=question["question"]
    question_answer=question["correct_answer"]
    new_question=Question(question_test,question_answer)
    question_bank.append((new_question))



quiz=QuizBrain(question_bank)

while quiz.still_questions():
      quiz.next_question()
print("Your have completed the quiz!.")
print(f"Your final score was : {quiz.score} / {quiz.question_number}")