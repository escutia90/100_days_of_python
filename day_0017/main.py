from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    question_bank.append(Question(i["text"], i["answer"]))

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print(f"Quiz completed!\nYou got {quiz_brain.score} out of {quiz_brain.question_number} right!")