from QuestionClass import Question

#Questions

question_prompt = [
    "\nHow Many Continents Are There?\n(a) 5\n(b) 7\n(c) 3\n\n",
    "\nHow Much Meals Shoud The Average Person Eat A Day?\n(a) 3 Balanced Meals\n(b) 2 Unhealthy Meals\n(c) No Meals (Who Needs To Eat?)\n\n",
    "\nWhich Country Invented Basketball?\n(a) United States Of America\n(b) Canada\n(c) Brazil\n\n"
]

#Setting up the questions

questions = [
    Question(question_prompt[0], "b"),
    Question(question_prompt[1], "a"),
    Question(question_prompt[2], "b"),
]

#Function that increases score each time you get a question right.

def test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    
    print("You Got ", str(score) + "/" + str(len(questions)) + " Questions Right!")
    
test(questions)