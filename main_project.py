from operator import itemgetter
import json
from dependensyOfProject import questions, TheEndAtTheBeginningError, ResponseRangeError1, ResponseRangeError2,ResponseRangeError3,ResponseRangeError4,ExitConditionError, NotFoundFileError, ResponseError
def error_management_and_processes(ignored_words_result_txt=[".", ",", "?", "!", ":", ";", "\"", "'", "-", "—", "(", ")", "[", "]", "...", "/", "{", "}", "<", ">", "|", "\\","\n"],
                                   counter_sentences=0, counter_line=0, counter_words=0, ignored_words_txt='', ignored_dic_result={},result_of_consecutive_words={},
                                   max_range_of_counter_word=None, min_range_of_counter_word=None, consecutive_words_counter=1, longest_lenght_of_word = {},
                                   all_words_list=[], sum_len_of_words=0, ave_len_of_words=0, range_of_length_of_word=[],permission_to_enter_key8 = 'False',
                                   new_counter_words=0, different_pattern_of_words_jump=[], sign_of='', counter_consecutive_words_counter=0,values_to_remove = [],
                                   result_of_sort_consecutive_words_counter={}, result_dict_for_normal_pattern={},sorted_dict_descending={},unused_words=[],final_all_words_list = []):      
         
    k = 0
    try:  
        while k < len(questions):
            answer = input(questions[k])
            
            if answer in 'qQ':
                raise ExitConditionError()
            if k == 0 and answer in 'nN':
                raise TheEndAtTheBeginningError()
            if (k == 0 and answer not in 'YyNn') or (k == 4 and answer not in 'YyNn'):
                raise ResponseRangeError1()
            if k == 3 and answer not in 'aAdD':
                raise ResponseRangeError2()
                
            if k == 1:
                try:
                    with open(answer, mode='r',encoding='utf-8') as file:
                        result_txt = file.read()
                    counter_sentences = len(result_txt.split('.'))
                    
                    for char in ignored_words_result_txt:
                        result_txt = result_txt.replace(char, ' ')
                    
                    all_words_list = result_txt.split()
                    print(all_words_list)
                    counter_words = len(all_words_list)
                    counter_line = len(result_txt.split('\n'))
    
                    sum_len_of_words = sum([len(word) for word in all_words_list])
                    ave_len_of_words = sum_len_of_words / counter_words
                    
                except FileNotFoundError:
                    raise NotFoundFileError()
            
            elif k == 2:
                if answer in 'nN':
                    k = 4
                    continue
                if answer in '0':
                    print('🖍  So you don\'t want consecutive words counter!')
                    k = 4
                    continue
                else:
                    try:
                        consecutive_words_counter = int(answer)
                        if consecutive_words_counter == 1:
                            for k in all_words_list:
                                different_pattern_of_words_jump[k] = all_words_list.count(v)
                            
                        sign_of = True
                    
                        for i in range(len(all_words_list) - (consecutive_words_counter - 1)):
                            different_pattern_of_words_jump.append(' '.join(all_words_list[i:i+consecutive_words_counter]))
                        for pattern in different_pattern_of_words_jump:
                            result_of_sort_consecutive_words_counter[different_pattern_of_words_jump.count(pattern)] = pattern
                    
                    except ValueError:
                        raise ResponseError()

            elif k == 3:
                if answer in 'dD':
                    sorted_dict = dict(sorted(result_of_sort_consecutive_words_counter.items(), key=itemgetter(1)))
                    result_of_consecutive_words= sorted_dict
                elif answer in 'aA':
                    sorted_dict_descending = dict(sorted(result_of_sort_consecutive_words_counter.items(), key=itemgetter(1), reverse=True))
                    result_of_consecutive_words = sorted_dict_descending
                
                if sign_of == False:
                    result_dict_for_normal_pattern = {word: all_words_list.count(word) for word in all_words_list}
                    if answer in 'dD':
                        sorted_dict = dict(sorted(result_dict_for_normal_pattern.items(), key=itemgetter(1)))
                        result_of_consecutive_words = sorted_dict
                    elif answer in 'aA':
                        sorted_dict_descending = dict(sorted(result_dict_for_normal_pattern.items(), key=itemgetter(1), reverse=True))
                        result_of_consecutive_words = sorted_dict_descending

            elif k == 4:
                if answer in 'nN':
                    k = 6
                    continue
                elif answer in 'yY':
                    k = 5
                    try:
                        answer = input(questions[5])
                        if answer in 'qQ':
                            raise ExitConditionError()
                        else:
                            with open(answer, mode='r') as file:
                                ignored_words_txt = file.read()
                                ignored_words_result_txt = ignored_words_txt.split()
                            
                                for word in all_words_list:
                                   if word in ignored_words_result_txt:
                                        all_words_list.append(ignored_words_result_txt.remove(word))
                                counter_words = len(all_words_list)
                                
                    except FileNotFoundError:
                        raise NotFoundFileError()
            
            elif k == 6 or k == 7:
                try:
                    if k == 6:
                       max_range_of_counter_word = int(answer)
                    else:
                        min_range_of_counter_word = int(answer)
                except ValueError:
                    raise ResponseRangeError3()
                
                if max_range_of_counter_word is not None and min_range_of_counter_word is not None:
                    if min_range_of_counter_word <= 0 and max_range_of_counter_word <= 0:
                        print('🖍 So You don\'t have any counter words!')
                        counter_words = 0
                        k = 9
                        
                    elif min_range_of_counter_word > max_range_of_counter_word:
                        print('🛑 Your minimum counter is greater than your maximum counter! This is not possible.')
                        permission_to_enter_key8 = 'True'
                        
                    elif (min_range_of_counter_word == max_range_of_counter_word) and (min_range_of_counter_word == max_range_of_counter_word)!=0:
                        all_words_list=[word  for word in all_words_list if len(word) == min_range_of_counter_word]
                        counter_words = len(all_words_list)
                        k = 9
                        print('print1:', 1)
                        
                    elif max_range_of_counter_word > min_range_of_counter_word:
                        
                        range_of_length_of_word = [ _ for _ in range(min_range_of_counter_word, max_range_of_counter_word+1)]
                        
                        for word in all_words_list:
                            if len(word) not in range_of_length_of_word:
                                values_to_remove.append(word)
                                
                        for word in all_words_list:
                            unused_words = [word for word in all_words_list if word in values_to_remove]
                            final_all_words_list = [word for word in all_words_list if word not in unused_words]
      
                        counter_words = len(final_all_words_list)
                        k = 9
                        print('print2:', 2)
                            
            
            elif permission_to_enter_key8 in 'True':
                try: 
                    answer = input(questions[8])
                    
                    if answer in 'Cc':
                        _ = min_range_of_counter_word
                        min_range_of_counter_word, max_range_of_counter_word = max_range_of_counter_word , _  
                        range_of_length_of_word=[ _ for _ in range(min_range_of_counter_word, max_range_of_counter_word+1)]
                        
                        for word in all_words_list:
                            unused_words = [word for word in all_words_list if word in values_to_remove]
                            final_all_words_list = [word for word in all_words_list if word not in unused_words]
      
                        counter_words = len(final_all_words_list)
                        K += 1
                        
                    if answer in 'Ee':
                        raise ExitConditionError()
                      
                except ResponseRangeError4 as e:
                        print(e)

            if k == 9:
                try:
                    answer = input(questions[9])
                    with open(answer + '.json', mode='w',encoding='utf-8') as file:
                        final_result = {
                            'Counter sentences': counter_sentences,
                            'All of the words in your file': all_words_list,
                            'Counter words': counter_words,
                            'Counter lines': counter_line,
                            'Ignored words list': ignored_words_result_txt,
                            'The average length of words in your text': ave_len_of_words,
                            'Consecutive words' : result_of_consecutive_words,
                            'longest_lenght_of_word' : longest_lenght_of_word
                        }
                        json.dump(final_result, file, indent=4)
                        print('✨ Your file has been processed')
                except FileNotFoundError:
                    raise NotFoundFileError()
                             
            k += 1    
    except (ValueError, TheEndAtTheBeginningError,ResponseRangeError1,ResponseRangeError2,ResponseRangeError3,ResponseRangeError4,ExitConditionError,NotFoundFileError,ResponseError) as e:
        print(e)

error_management_and_processes()
