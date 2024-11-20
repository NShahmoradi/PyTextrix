from operator import itemgetter
import json
import re
import os
  
from dependensyOfProject import (questions,
                                 TheEndAtTheBeginningError, 
                                 ResponseRangeError1, 
                                 ResponseRangeError2, 
                                 ResponseRangeError3,
                                 ResponseRangeError4,
                                 ResponseRangeError5,
                                 ExitConditionError,
                                 NotFoundFileError,
                                 ResponseError)

def error_management_and_processes(
        ignored_words_result_txt=[".", ",", "’", "?", "!", ":", ";", "\"", "'", "-", "—", "(", ")", "[", "]", "...", "/", "{", "}", "<", ">", "|", "\\", "\n"],
        counter_sentences=0, counter_line=0, counter_words=0, ignored_words_txt='', result_of_consecutive_words={},max_len_word=0,same_max_length=[],
        max_range_of_counter_word=None, min_range_of_counter_word=None, consecutive_words_counter=1, longest_lenght_of_word={},max_length='',
        all_words_list=[], sum_len_of_words=0, ave_len_of_words=0, range_of_length_of_word=[], final_all_words_list=[],find_max_len_word=[],
        consecutive_value1=False,result_of_sort_consecutive_words_counter={}, result_dict_for_normal_pattern={}):
    
    k = 0
    try:
        while k < len(questions):
            answer = input(questions[k])
             
            # management of entries for the questions 1 & 3 & 4
            if answer in 'qQ':
                raise ExitConditionError()
            if k == 0 and answer in 'nN':
                raise TheEndAtTheBeginningError()
            if (k == 0 and answer not in 'YyNn') or (k == 4 and answer not in 'YyNn'):
                raise ResponseRangeError1()
            if k == 3 and answer not in 'aAdD':
                raise ResponseRangeError2()
            
            # read input the text file
            if k == 1:
                try:
                    with open(answer, mode='r', encoding='utf-8') as file:
                        result_txt = file.read()
                    counter_sentences = len([s for s in re.split(r'(?<=[.!?])\s+(?=[A-Z])', result_txt) if s.strip()])
                    counter_line = len(result_txt.splitlines())
                    
                    # remove the ignored words from the input file
                    for char in ignored_words_result_txt:
                        result_txt = result_txt.replace(char, ' ')

                    all_words_list = result_txt.split()
                    counter_words = len(all_words_list)
                    
                    sum_len_of_words = sum([len(word) for word in all_words_list])
                    
                    # the average number of characters in words in the entire file is the maximum and minimum counters
                    ave_len_of_words = sum_len_of_words / counter_words

                except FileNotFoundError:
                    raise NotFoundFileError()
                
            # process of key2 : check to have any consecutive word counter
            elif k == 2:
                try:
                    if answer in 'nN':
                        k = 4
                        continue
                    if answer == '0':
                        print('🖍  So you don\'t want consecutive words counter!')
                        k = 4
                        continue
                    if int(answer) < 0:
                        raise ResponseRangeError5()
                    
                except ValueError:    
                        raise ResponseError()  
                      
                else:
                    try:
                        consecutive_words_counter = int(answer)
                        # if the consecutive word counter is 1, all words are counted one by one:
                        if consecutive_words_counter == 1:
                            consecutive_value1 = True 
                         
                        # implennting the consecutive word (if is bigger than 1!): 
                        elif consecutive_words_counter > 1:    
                            for i in range(len(all_words_list) - (consecutive_words_counter - 1)):
                               pattern = ' '.join(all_words_list[i:i+consecutive_words_counter])
                               result_of_sort_consecutive_words_counter[pattern] = (pattern).count(pattern) 
                             
                    except ValueError:
                        raise ResponseError()
                    
            # process of key2 :implementing the pattern of consecutive words and sorting them
            elif k == 3:
                if not consecutive_value1:
                    if answer in 'dD':
                        result_of_consecutive_words = dict(sorted(result_of_sort_consecutive_words_counter.items(), key=itemgetter(1)))
                    elif answer in 'aA':
                         result_of_consecutive_words = dict(sorted(result_of_sort_consecutive_words_counter.items(), key=itemgetter(1), reverse=True))
                else:
                    result_dict_for_normal_pattern = {word: all_words_list.count(word) for word in all_words_list}
                    if answer in 'dD':
                        result_of_consecutive_words = dict(sorted(result_dict_for_normal_pattern.items(), key=itemgetter(1)))
                    elif answer in 'aA':
                        result_of_consecutive_words= dict(sorted(result_dict_for_normal_pattern.items(), key=itemgetter(1), reverse=True))
             
            # process of key 4: read ignored word file
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

                                all_words_list = [word for word in all_words_list if word not in ignored_words_result_txt]
                                counter_words = len(all_words_list)

                    except FileNotFoundError:
                        raise NotFoundFileError()
                    
            # processes of key 6 & 7 :  check and give the max & min counter for range of words
            elif k == 6 or k == 7:
                try:
                    if k == 6:
                        max_range_of_counter_word = int(answer)
                    else:
                        min_range_of_counter_word = int(answer)
                except ValueError:
                    raise ResponseRangeError3()
                
                # find the negative counter!!
                if min_range_of_counter_word is not None and min_range_of_counter_word < 0:
                    raise ResponseRangeError5()

                if max_range_of_counter_word is not None and max_range_of_counter_word < 0:
                    raise ResponseRangeError5()

                # manage possible errors to get max & min word count:
                if max_range_of_counter_word is not None and min_range_of_counter_word is not None:
                    if min_range_of_counter_word == 0 and max_range_of_counter_word == 0:
                        print('🖍 So You don\'t have any counter words!')
                        counter_words = 0
                        k = 9
                        
                    elif min_range_of_counter_word > max_range_of_counter_word:
                        print('🛑 Your minimum counter is greater than your maximum counter! This is not possible.')
                        try:
                            answer = input(questions[8])
                            # if the counter word range (max and min counter) is not correct, the counter values ​​will shift when receiving input c.
                            if answer in 'Cc':
                                min_range_of_counter_word, max_range_of_counter_word = max_range_of_counter_word, min_range_of_counter_word
                                range_of_length_of_word = range(min_range_of_counter_word, max_range_of_counter_word + 1)
                                final_all_words_list = [word for word in all_words_list if len(word) in range_of_length_of_word]
                                counter_words = len(final_all_words_list)
                                k = 9

                            if answer in 'Ee':
                                raise ExitConditionError()

                        except ResponseRangeError4 as e:
                            print(e)
                    
                    # if you have same (max and min counter) actually you  you have one counter for filtering
                    elif (min_range_of_counter_word == max_range_of_counter_word) and (min_range_of_counter_word != 0):
                        print('🖍 So you have one limit for sorting your words of file!')
                        all_words_list = [word for word in all_words_list if len(word) == min_range_of_counter_word]
                        counter_words = len(all_words_list)
                        k = 9
                    # if we have a normal counter (max_coun > min_count) we have the basic way to sort all the words
                    elif max_range_of_counter_word > min_range_of_counter_word:
                        range_of_length_of_word = range(min_range_of_counter_word, max_range_of_counter_word + 1)
                        final_all_words_list = [word for word in all_words_list if len(word) in range_of_length_of_word]
                        counter_words = len(final_all_words_list)
                        k = 9
                    
                    # if we have a negative counter, the program will give an error.
                    elif (max_range_of_counter_word < 0) or (min_range_of_counter_word< 0):
                        raise ResponseRangeError5()  
                    
                         
            # find the longest word according to the max and min counters
            for word in final_all_words_list:
                if len(word) > max_len_word:
                    max_length = word
                    max_len_word = len(word)
                else:
                    continue  
             
            # find all words in the file whose length is equal to the length of the longest word in the file    
            same_max_length = [word for word in final_all_words_list if len(word)==max_len_word]  
            
            # process of key 9: get a path to save the result file in json format     
            if k == 9:
                try:
                    answer = input(questions[9])
                    if answer in 'qQ':
                        raise ExitConditionError()
                    
                    # checks if the directory of the specified path exists or not:  
                    if not os.path.isdir(os.path.dirname(answer)):
                        raise NotFoundFileError
                    
                    with open(answer + '.json', mode='w', encoding='utf-8') as file:
                        final_result = {
                            'Counter sentences': counter_sentences,
                            'Total words in the file according to minimum and maximum counters': final_all_words_list,
                            'Counter words': counter_words,
                            'Counter lines': counter_line,
                            'Ignored words list': ignored_words_result_txt,
                            'The average length of words in your text': ave_len_of_words,
                            'Consecutive words': result_of_consecutive_words,
                            'The last word with the longest character length': max_length,
                            'All of the longest length of word': same_max_length
                        }
                        json.dump(final_result, file, indent=3)
                        print('✨ Your file has been processed')
                        
                except FileNotFoundError:
                    raise NotFoundFileError()

            k += 1
    except (ValueError, TheEndAtTheBeginningError, ResponseRangeError1, ResponseRangeError2, ResponseRangeError3, ResponseRangeError4,ResponseRangeError5, ExitConditionError, NotFoundFileError, ResponseError) as e:
        print(e)

error_management_and_processes()