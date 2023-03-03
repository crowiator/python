from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_list = []
for one_question in question_data:
    question_t = one_question["question"]
    question_a = one_question["correct_answer"]
    new_question = Question(question_t,question_a)
    question_list.append(new_question)

quiz = QuizBrain(question_list)
while quiz.has_questions():
    quiz.next_question()
print("Kviz je ukonceny")
print(f"Vase celkove skore je: {quiz.score}/{quiz.question_number}")