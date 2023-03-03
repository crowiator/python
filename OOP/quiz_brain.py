
class QuizBrain:

    def __init__(self, q_list) -> None:
        self.score= 0
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        user_answer= input(f"Otazka c. {self.question_number} je {current_question.question_text} (True/False): ")
        self.check_answer(user_answer,current_question.question_answer)

    def check_answer(self,user_answer, correctt_answer):
        if user_answer.lower() == correctt_answer.lower():
            print("Uhadli ste!!")
            self.score +=1
        else:
            print("Spatna odpoved")  
        print(f"Spravne odpoved je {correctt_answer}")
        print(f"Vase skore je {self.score}/ {self.question_number}")      



    def has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

          