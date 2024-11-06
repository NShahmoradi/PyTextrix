from operator import itemgetter
import re
import json
from dependensyOfProject import questions, TheEndAtTheBeginningError, ResponseRangeError1, ResponseRangeError2, ExitConditionError, NotFoundFileError, ResponseError

def error_management_and_processes(ignored_words_result_txt=[".", ",", "?", "!", ":", ";", "\"", "'", "-", "—", "(", ")", "[", "]", "...", "/", "{", "}", "<", ">", "|", "\\","\n"],
                                   counter_sentences=0, counter_line=0, counter_words=0, ignored_words_txt='', ignored_dic_result={},
                                   max_answer=0, min_answer=0, consecutive_words_counter=1, counter_consecutive_words_counter=0,
                                   all_words_list=[], sum_len_of_words=0, ave_len_of_words=0, range_of_length_of_word=[],
                                   new_counter_words=0, word_jump=0, different_pattern_of_words_jump=[], sign_of='',
                                   result_of_sort_consecutive_words_counter={}, result_dict_for_normal_pattern={},sorted_dict_descending={}):      
    
         
    k = 0
    try:  
        while k < len(questions):
            answer = input(questions[k])
            
            if answer in 'qQ':
                raise ExitConditionError()
            if k == 0 and answer in 'nN':
                raise TheEndAtTheBeginningError()
            if (k == 0 and answer not in 'YyNn') or (k == 3 and answer not in 'aAdD'):
                raise ResponseRangeError1()
                
            
            if k == 1:
                try:
                    with open(answer, mode='r') as file:
                        result_txt = file.read()
                    counter_sentences = len(result_txt.split('.'))
                    
                    for char in ignored_words_result_txt:
                        result_txt = result_txt.replace(char, ' ')
                    
                    all_words_list = result_txt.split()
                    counter_words = len(all_words_list)
                    counter_line = len(result_txt.split('\n'))
    
                    sum_len_of_words = sum(len(word) for word in all_words_list)
                    ave_len_of_words = sum_len_of_words / counter_words
                    
                except FileNotFoundError:
                    raise NotFoundFileError()
            
            elif k == 2:
                if answer in 'nN':
                    k = 4
                    continue
                else:
                    try:
                        word_jump = int(answer)
                        sign_of = True # edit the name sign_of....
                    
                        for i in range(len(all_words_list) - (word_jump - 1)):
                            different_pattern_of_words_jump.append(' '.join(all_words_list[i:i+word_jump]))
                        for pattern in different_pattern_of_words_jump:
                            result_of_sort_consecutive_words_counter[different_pattern_of_words_jump.count(pattern)] = pattern
                    
                    except ValueError:
                        raise ResponseError()

            elif k == 3:
                if answer not in 'aAdD':
                    raise ResponseRangeError2()
                
                
                if answer in 'dD':
                    sorted_dict = dict(sorted(result_of_sort_consecutive_words_counter.items(), key=itemgetter(1)))
                elif answer in 'aA':
                    sorted_dict_descending = dict(sorted(result_of_sort_consecutive_words_counter.items(), key=itemgetter(1), reverse=True))
                
                
                if sign_of != 'True':
                    result_dict_for_normal_pattern = {word: all_words_list.count(word) for word in all_words_list}
                    if answer in 'dD':
                        sorted_dict = dict(sorted(result_dict_for_normal_pattern.items(), key=itemgetter(1)))
                    elif answer in 'aA':
                        sorted_dict_descending = dict(sorted(result_dict_for_normal_pattern.items(), key=itemgetter(1), reverse=True))

            elif k == 4:
                if answer in 'yY':
                    k = 5
                    try:
                        answer = input(questions[5])
                        with open(answer, mode='r') as file:
                            ignored_words_txt = file.read()
                            ignored_words_result_txt = ignored_words_txt.split()
                            
                            for word in all_words_list:
                                if word in ignored_words_result_txt:
                                    result_txt = re.sub(re.escape(word), ' ', result_txt)
                            counter_words = len(all_words_list)
                            
                    except FileNotFoundError:
                        raise NotFoundFileError()
                elif answer in 'nN':
                    k = 6
                    continue

            elif k == 6:
                pass
            
            elif k == 7:
                pass
            
            elif k == 8:
                try:
                    print('✔ Your file has been processed')
                    with open(answer, mode='w') as file:
                        final_result = {
                            '🟢 Counter sentences': counter_sentences,
                            '🟢 All of the words in your file': all_words_list,
                            '🟢 Counter words': counter_words,
                            '🟢 Counter lines': counter_line,
                            '🟢 Ignored words list': ignored_words_result_txt,
                            '🟢 The average length of words in your text': ave_len_of_words
                        }
                        json.dump(final_result, file)
                except FileNotFoundError:
                    raise NotFoundFileError()
                             
            k += 1  

        print('🟢 Counter sentences:', counter_sentences, '\n',
              '🟢 All of the words in your file:', all_words_list, '\n',
              '🟢 Counter words:', counter_words, '\n',
              '🟢 Counter lines:', counter_line, '\n',
              '🟢 Ignored words list:', ignored_words_result_txt, '\n',
              '🟢 The average length of words in your text:', ave_len_of_words)
        
    except (ValueError, TheEndAtTheBeginningError,ResponseRangeError1,ResponseRangeError2,ExitConditionError,NotFoundFileError,ResponseError) as e:
        print(e)

error_management_and_processes()
