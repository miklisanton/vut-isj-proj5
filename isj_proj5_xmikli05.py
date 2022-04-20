#!/usr/bin/env python3


def gen_quiz(qpool, *indexes, altcodes="ABCDEF", quiz=None):
    if quiz is None:
        quiz = []
    for index in indexes:
        try:
            answers_with_altcodes = zip(altcodes, qpool[index][1])  #creates pairs altcode + answer
            answers_with_altcodes = list(map(": ".join, answers_with_altcodes))   #makes strings from pairs
            quiz_element = (qpool[index][0], answers_with_altcodes) #creates pair question + answers with altcodes
            quiz.append(quiz_element)   #appends pair of question and answers to quiz list
        except IndexError:
            print(f"Ignoring index {index} - list index out of range")
        except ValueError:
            print(f"Ignoring index {index} - wrong element of qpool")
    return quiz