from sklearn.metrics import SCORERS
import serialize

def play_trivia(questions):

    score = 0

    total_questions = len(questions)


    for question in questions:

        print(question['question'])

        for i, option in enumerate(question['options']):

            print(f"{i + 1}. {option}")


        answer = input("Enter your answer (1-4): ")

        if answer == str(question['correct_answer']):

            print("Correct!")

            score += 1

        else:

            print("Incorrect!")


    print("\nTrivia Complete!")

    print(f"Your score: {score}/{total_questions}")
    return score


def main():

    # Example trivia questions

    questions = [

        {

            'question': 'What is the capital of France?',

            'options': ['London', 'Paris', 'Berlin', 'Madrid'],

            'correct_answer': 2

        },

        {

            'question': 'Who painted the Mona Lisa?',

            'options': ['Leonardo da Vinci', 'Pablo Picasso', 'Vincent van Gogh', 'Michelangelo'],

            'correct_answer': 1

        },

        {

            'question': 'What is the largest planet in our solar system?',

            'options': ['Mars', 'Venus', 'Jupiter', 'Saturn'],

            'correct_answer': 3

        }

    ]


    # Play trivia game

    file = "last_score.pkl"
    last_score = serialize.load(file)
    if last_score is not None:
        print ("Welcome back, you last score was", last_score)

    last_score = play_trivia(questions)
    serialize.save(last_score, file)

if __name__ == '__main__':

    main() 