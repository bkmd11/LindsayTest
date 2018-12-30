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

#cant use value to call key!
#need to rewrite so the answer option is the value, and an identifier is the key

dictionary = {}
question = 'spam'
while question != '':
    #question/answer groups
    question = input('Enter the question, or enter nothing to exit: ')
    if question == '':
        break
    else:
        correct_answer = input('What is the correct answer? ')
        wrong_answer1 = input('First wrong answer: ')
        wrong_answer2 = input('Second wrong answer: ')
        wrong_answer3 = input('Final wrong answer: ')
        dictionary.setdefault(question, {'correct_answer': correct_answer, 'wrong_answer1': wrong_answer1,
                                         'wrong_answer2': wrong_answer2, 'wrong_answer3': wrong_answer3})
        

file_name = input('What do you want to name this file? ')
file = open('%s.py' % (file_name), 'w')
file.write(file_name + pprint.pformat(dictionary))
file.close()
print('%s has been saved!' % (file_name))

#there has to be a way to pull from an existing file...
