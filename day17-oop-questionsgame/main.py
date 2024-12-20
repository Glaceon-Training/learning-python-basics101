from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    question_difficulty = question["difficulty"]
    new_question = Question(question_text, question_answer, question_difficulty)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed all the quizzes, G!")
print(f"Your final score was: {quiz.score}/{quiz.total_score}")
