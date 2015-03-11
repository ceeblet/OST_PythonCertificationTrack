from datetime import datetime, timedelta
import random
import statistics

def add_two_nums(a, b):
    return int(a) + int(b)

def generate_random_to_ten():
    return random.randint(1, 10)

def calculate_average_time(total_time):
    return statistics.mean(total_time)

def display_results(questions):
    total_time = []
    for key in questions.keys():
        total_time.append(questions[key]["time"])
        print("Question #{0} took {1} second(s) and is {2}!".format(key, questions[key]["time"], questions[key]["grade"]))
    
    print("You took %s seconds to finish the quiz" % sum(total_time)) 
    print("Your average time was %s seconds per question" % calculate_average_time(total_time))   

def main():
    questions = {}
    for question in range(1,6):
        rand_inta = generate_random_to_ten()
        rand_intb = generate_random_to_ten()
        start_time = datetime.now()
        answer = input("What is the sum of {0} and {1}? ".format(rand_inta, rand_intb))
        end_time = datetime.now()
        if (int(answer) == add_two_nums(rand_inta, rand_intb)):
            grade = "right"
        else:
            grade = "wrong"
        print("{0} is {1}!".format(answer, grade))
        delta = end_time - start_time
        questions[question] = {"time": delta.seconds, "grade": grade}

    display_results(questions)

if __name__ == "__main__":
    main()