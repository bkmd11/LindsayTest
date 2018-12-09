#! python3
"""mid term tests for lindsays physical science class makes 3 different tests.
Before the program gets run, variables for i need to be checked and modified,
and headers for different test sections need to be changed.
This may allow bugs to be introduced but as of 12/9/18 I dont know how to avoid that"""

import function

#dictionaries that need to be filled, might pull the dictionaries from other files...
multiple_choice = {}
match = {}

#lists of questions
short_answer = []
critical_thinking = []

#makes the tests and keys
for test_num in range(3):
    test_file = open('PhySci_%s.txt' % (test_num + 1),'w')
    test_key = open('TestKey_%s.txt' % (test_num +1), 'w')

    test_file.write((' '*20)+'PHYSICAL SCIENCE MID-TERM (TEST %s)' % (test_num+1))
    test_file.write('\n\n')
    test_key.write('PHYSICAL SCIENCE ANSWERS (TEST %s)\n' % (test_num+1))

    #converting the dictionaries into list_obj for the functions
    multi = list(multiple_choice.keys())
    matchy_match = list(match.keys())

    #testfile.write('Some kind of header for the question catagory')
    function.multiple_choice_questions(multiple_choice, multi, 5, test_file, test_key)
    #test_file.write('Some kind of header for the question catagory')
    function.match_option_questions(match, matchy_match, 3, test_file, test_key)
    #test_file.write('Some kind of header for short answers')
    function.open_ended_questions(short_answer, 3, test_file)
    #test_file.write('Something about critical thinking')
    function.open_ended_questions(critical_thinking, 2, test_file

    test_file.close()
    test_key.close()


"""Lindsay would like random wrong answers instead of ones that come from
    the question dictonary.
    I will need to carefully go through and add question headers for any changes that
    are ever made to the tests... could be a pain with time. I personally believe that
    this whole project would be better for a smaller test first
    """
