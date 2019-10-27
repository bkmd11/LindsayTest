#this function makes multiple choice questions

import random

#handles multiple choice questions from a dictionary
# I need to modify this for my new format
def multiple_choice_questions(question_dic, list_obj, i, test_file, answer_file):
    random.shuffle(list_obj)
    for question_num in range(i):
        correct_answer = question_dic[list_obj[question_num]]
        wrong_answer = list(question_dic.values())
        del wrong_answer[wrong_answer.index(correct_answer)]
        wrong_answer = random.sample(wrong_answer, 3)
        answer_options = wrong_answer + [correct_answer]
        random.shuffle(answer_options)

        test_file.write(' %s) %s\n' %(question_num+1, list_obj[question_num]))
        for x in range(4):
            test_file.write('%s. %s\n' % ('ABCD'[x], answer_options[x]))
        test_file.write('\n')
        answer_file.write('%s. %s\n' %(question_num+1,
                                       'ABCD'[answer_options.index(correct_answer)]))

#handles matched based questions from a dictionary
def match_option_questions(question_dic, list_obj, i, test_file, answer_file):
    random.shuffle(list_obj)
    for question_num in range(i):
        correct_answer = question_dic[list_obj[question_num]]

        test_file.write('%s %s\n' % (list_obj[question_num], '_'*30))
        answer_file.write('%s\n' % (correct_answer))

#handles short answer and critical thinking questions from a list
def open_ended_questions(list_obj, i, test_file):
    random.shuffle(list_obj)
    for question_num in range(i):
        test_file.write('%s %s' % (list_obj[question_num], '\n'*20))
        
        

        
""" I need to figure out another fucntion for true/false questions
    and one that can handle my short answer and critical thinking questions
    """

 
