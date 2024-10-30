questions = {
    0:'Hi! welcome to command line interface (📌 if you want to exit at any part of the program please enter "q" and be mindful which enter the full path of your file). Are you sure wanna continue?(y/n)',
    1:'Please enter path of your file:',
    2:'Please enter a number for consecutive words counter:',
    3:'Do you have any ignored words file?(y/n)',
    4:'Please enter path of your ignored words file.(Your words in your ignored file should be separated by \',\')',
    5:'Please enter min range for jump words:',
    6:'Please enter max range for jump words:',
    7:'Please enter path of your file which you want to save there:'
}
result_as_list = []
def error_management(counter_sentences=0, counter_words=0, ignored_words_result_txt=['?', '!', ';'], ignored_words_txt='', ignored_dic_result={}, max_answer=0, min_answer=0,consecutive_words_counter=0,counter_consecutive_words_counter=0, all_words_list=[], sum_len_of_words =0, ava_len_of_words=0):
    class TheEndAtTheBeginningError(Exception):
        def __init__(self, massage='If you don\'t want your case to be processed, what are you doing here?!🙃'):
            super().__init__(massage)
    class ResponseRangeError(Exception):
        def __init__(self, massage='🛑You have two ways to respond, y or n!'):
            super().__init__(massage) 
    class ExitConditionError(Exception):
        def __init__(self, massage='The process of processing your file is finished👋🙂'):
            super().__init__(massage)  
    class NotFoundFileError(Exception):
        def __init__(self, massage='🛑 Your file name or correct path may be incorrect or your file may be empty! please check your file.'):
            super().__init__(massage)         