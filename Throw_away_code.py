import random

def short_answer_questions(list_obj, i, test_file):
    random.shuffle(list_obj)
    for question_num in range(i):
        test_file.write('%s %s' % (list_obj[question_num], '\n'*25))


short_answer = ['what is the meaning of life?', 'how many roads must one man walk',
                'do you want to be happy or have money?','can bear grylls grill bears?']


for test_num in range(3):
    test_file = open('PhySci_%s.txt' % (test_num + 1),'w')
    test_key = open('TestKey_%s.txt' % (test_num +1), 'w')

    test_file.write((' '*20)+'PHYSICAL SCIENCE MID-TERM (TEST %s)' % (test_num+1))
    test_file.write('\n\nShort Answer Section\n')
    test_key.write('PHYSICAL SCIENCE ANSWERS (TEST %s)\n' % (test_num+1))
    test_key.write('-Short Answer Section\n')

    short_answer_questions(short_answer, 2, test_file)



    test_file.close()
    test_key.close()
