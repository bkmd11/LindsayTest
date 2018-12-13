#! python3

import pprint
""" the goal of this file is to format a set of strings into a list
of dictionaries of question/answer groups.

I need to figure out how to extract questions from a word file, and seperate
the multiple choice answers into a seperate dictionary

example format of one key value pair:

Level_one_multi_choice = {'What is a hypothesis?':{'A guess': False,
                    'A prediction about the outcome of an experiment based on prior knowledge': True,
                    'The actual outcome of an experiment': False,
                    'A prediction about the outcome of an experiment without background knowledge': False}}

"""


dictionary = {}
question = 'spam'
while question != '':
    #question/answer groups
    question = input('Enter the question, or enter nothing to exit: ')
    if question == '':
        break
    else:
        answer1 = input('What is the correct answer? ')
        answer2 = input('First wrong answer: ')
        answer3 = input('Second wrong answer: ')
        answer4 = input('Final wrong answer: ')
        # structuring the dictionary
        dictionary.setdefault(question, {answer1: True, answer2:False, answer3:False, answer4:False})

file_name = input('What do you want to name this file? ')
file = open('%s.py' % (file_name), 'w')
file.write(file_name + pprint.pformat(dictionary))
file.close()
print('%s has been saved!' % (file_name))

#there has to be a way to pull from an existing file...
