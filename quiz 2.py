from blueprint import Blueprint
from blueprint import question_data
class Quiz:
    def __init__(self):
        self.questionbank = []
        for q in question_data:
            text = q["text"]
            answer = q["answer"]
            question = Blueprint(text, answer)
            self.questionbank.append(question)
        
        self.score = 0
        self.current_question_index = 0
        self.consecutive_correct_answers = 0
        self.consecutive_wrong_answers = 0
        self.hint_used = 0
        self.phone_a_friend_used = 0

    def next_question(self):
        if self.current_question_index < len(self.questionbank):
            return self.questionbank[self.current_question_index]
        else:
            return "No Question available--end of Quiz"

    def checker(self, user_answer):
        current_question = self.questionbank[self.current_question_index ]
        return user_answer.lower() == current_question.answer.lower()

    def calc_score(self):
        return self.score

    def is_any_question_left(self):
        return self.current_question_index < len(self.questionbank)

    def skip_question_lifeline(self):
        if self.current_question_index < len(self.questionbank):
            self.current_question_index += 1
            self.consecutive_correct_answers = 0
            self.consecutive_wrong_answers = 0
            print("Question skipped. Moving to the next question.")
            print("No change in score.")
        else:
            print("No more questions to skip.")

    def hint(self):
        if self.hint_used < 2:
            print("Hint: ...........")  # sorry I have not added the hint 
            self.hint_used += 1
        else:
            print("Sorry, you've used all your hints.")

    def phone_a_friend(self):
        if self.phone_a_friend_used < 2:
            print("Enter the name of your friend you want to call:")
            friend_name = input()
            print(f"Calling {friend_name}...")
            self.score += 2  # Assuming the friend always gives the right answer (just like KBC :))
            self.consecutive_correct_answers += 1
            self.consecutive_wrong_answers = 0
            
        else:
            print("This lifeline has reached its limit.")

    def start_quiz(self):
        print("Welcome to the Quiz!")
        while self.is_any_question_left():
            current_question = self.next_question()
            print(f"Question: {current_question.question}")
            user_input = input("True or False? (Type 'hint' for a hint)(Type 'skip' to skip the question)(Type 'call friend' to use the phone-a-friend lifeline): ")

            if user_input.lower() == "hint":
                self.hint()
            elif user_input.lower() == "skip":
                self.skip_question_lifeline()
            elif user_input.lower() == "call friend":
                self.phone_a_friend()
            else:
                if self.checker(user_input):
                    self.score += 2
                    print("Bingo! It's correct!👍")
                    self.consecutive_correct_answers += 1
                    self.consecutive_wrong_answers = 0
                    if self.consecutive_correct_answers == 2:
                        print("You're on fire! 🔥")
                    elif self.consecutive_correct_answers >= 3:
                        print("You're unstoppable! 🔥")
                else:
                    self.score -= 1
                    print("Better luck next time!")
                    self.consecutive_correct_answers = 0
                    self.consecutive_wrong_answers += 1
                    if self.consecutive_wrong_answers >= 3:
                        print("Don't give up! 💪")
            self.current_question_index += 1               

        print(f"Quiz complete! Your score is {self.calc_score()}")
quiz_instance = Quiz()
quiz_instance.start_quiz()
