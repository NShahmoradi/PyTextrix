questions = {
    0:'Hi! welcome to command line interface (📌 if you want to exit at any part of the program please enter "q" and be mindful which enter the full path of your file). Are you sure wanna continue?(y/n)',
    1:'Please enter path of your file:',
    2:'Please enter a number for consecutive words counter(if you don\'t have any idea for consecutive words counter please enter\'n\'):',
    3:'Do you have any ignored words file?(y/n)',
    4:'Please enter path of your ignored words file(Your words in your ignored file should be separated by \'space\'):',
    5:'Please enter a number for the maximum character range of words:',
    6:'Please enter a number for the minimum character range of words:',
    7:'Please enter path of your file which you want to save there:'
}

def error_management_and_processes(counter_sentences=0, counter_words=0, ignored_words_result_txt=[".", ",", "?", "!", ":", ";", "\"", "'", "-", "–", "—", "(", ")", "[", "]", "...", "/", "{", "}", "<", ">", "|", "\\"],
                                   ignored_words_txt='', ignored_dic_result={}, max_answer=0, min_answer=0,consecutive_words_counter=1,
                                   counter_consecutive_words_counter=0, all_words_list=[], sum_len_of_words =0, ava_len_of_words=0,
                                   range_of_length_of_word=[],new_counter_words=0):
    class TheEndAtTheBeginningError(Exception):
        def __init__(self, message='If you don\'t want your case to be processed, what are you doing here?!🙃'):
            super().__init__(message)
    class ResponseRangeError(Exception):
        def __init__(self, message='🛑 You have two ways to respond, y or n!'):
            super().__init__(message) 
    class ExitConditionError(Exception):
        def __init__(self, message='The process of processing your file is finished👋🙂'):
            super().__init__(message)  
    class NotFoundFileError(Exception):
        def __init__(self, message='🛑 Your file name or path may be incorrect or your file may be empty! please check your file.'):
            super().__init__(message)
    class ResponseError(Exception):
        def __init__(self, message='🛑 Your answer must be an integer or n!'):
            super().__init__(message)                      
    k = 0
    try:  
        while k < len(questions):
            answer = input(questions[k])
            
            if answer in 'qQ':
                raise ExitConditionError()
            if k == 0 and answer in 'nN':
                raise TheEndAtTheBeginningError()
            if (k == 0 and answer not in 'YynN') or (k == 3 and answer not in 'YynN'):
                raise ResponseRangeError()
                
            if k in [1, 4, 7]:
                try:
                    if k==1:
                        with open(answer, mode='r') as file:
                            result_txt = file.read()
                        counter_sentences = len(result_txt.split('.'))
                        
                        for i in result_txt:
                            if i in ignored_words_result_txt:
                                result_txt.replace(i,' ')
 
                        all_words_list = result_txt.split(' ')
                        counter_words = len(all_words_list)
                        counter_line = len(result_txt.split('\n'))
        
                        for i in all_words_list:
                            sum_len_of_words += len(i)
                        ava_len_of_words = sum_len_of_words / counter_words  

                    elif k == 3 and answer in 'yY':
                        k=4
                        try:
                            answer = input(questions[4])
                            with open(answer, mode='r') as file:
                                ignored_words_txt = file.read()
                                # if len(str(ignored_words_txt).split(' ')) == 1 or (len(str(ignored_words_txt).split(' ')) > 1):
                                ignored_words_result_txt = ignored_words_txt.split(' ')
                                for i in all_words_list:
                                    if i in ignored_words_result_txt:
                                        all_words_list.remove(i)
                                counter_words = len(all_words_list)                               
                        except FileNotFoundError:
                            raise NotFoundFileError()
                    elif k==7:
                        try:
                            with open(answer, mode='w') as file:
                                final_result = file.write(
                                    
                                    'ignored_words_result_txt -> as list'
                                )   
                        except FileNotFoundError:
                            raise NotFoundFileError()   
                              
                except FileNotFoundError:
                    raise NotFoundFileError()      
                    
            if k == 3 and answer in 'nN':
                k = 5 
                continue

            if k in [2, 5, 6]:
                if k==2 and (answer in 'nN'):  
                    k = 3
                    continue
                try:
                    answer = int(answer)
                    if k==2:
                        pass
        
                    if k == 5:
                        max_answer = answer
                    if k == 6:
                        min_answer = answer  
                             
                    elif min_answer and max_answer not in [0]:
                        all_words_list.clear()
                        range_of_length_of_word=[ _ for _ in range(min_answer, max_answer+1)]
                        
                        for i in all_words_list:
                            if len(i) in range_of_length_of_word:
                                new_counter_words += 1
                                all_words_list.append(i)
                        counter_words = new_counter_words       
                         
                        for i in all_words_list:
                                if i in ignored_words_result_txt:
                                    all_words_list.remove(i)    
                        
                    elif min_answer == max_answer:
                        all_words_list.clear()
                        for i in all_words_list:
                            if len(i) in min_answer:
                                counter_words += 1
                                all_words_list.append(i)
                        for i in all_words_list:
                                if i in ignored_words_result_txt:
                                    all_words_list.remove(i)
                                                  
                except ValueError:
                    raise ResponseError()
                             
            k += 1  

    except (ValueError, TheEndAtTheBeginningError, ResponseRangeError, ExitConditionError, NotFoundFileError,ResponseError) as e:
        print(e)
error_management_and_processes()