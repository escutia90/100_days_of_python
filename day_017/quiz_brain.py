class QuizBrain:

    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (true/false):")
        self.check_answer(answer, self.question_list[self.question_number].answer)
        self.question_number +=1

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score +=1
        else:
            print("That's wrong")
        print(f"Your current score is: {self.score}/{self.question_number + 1}")
        print("\n")
