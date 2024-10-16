class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.total_score = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def quiz_total_score(self):
        q_difficulty = self.question_list[self.question_number]
        if q_difficulty.difficulty == "hard":
            self.total_score += 3
        elif q_difficulty.difficulty == "medium":
            self.total_score += 2
        else:
            self.total_score += 1

        return self.total_score

    def next_question(self):
        current_question = self.question_list[self.question_number]
        q_difficulty = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1}. Difficulty: {q_difficulty.difficulty}\n"
                            f"Question: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer, q_difficulty.difficulty)
        self.question_number += 1

    def check_answer(self, user_answer, correct_answer, question_difficulty):
        if user_answer.lower() == correct_answer.lower():
            if question_difficulty.lower() == "hard":
                self.score += 3
            elif question_difficulty.lower() == "medium":
                self.score += 2
            else:
                self.score += 1
            print("Wow G! You are truly a sigma!")
        else:
            print("Aw, that's not the answer G, big L!")

        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.quiz_total_score()}.")
        print("\n")
