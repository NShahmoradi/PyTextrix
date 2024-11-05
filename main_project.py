import re
from operator import itemgetter
import json
from dependensyOfProject import questions,TheEndAtTheBeginningError,ResponseRangeError,ExitConditionError,NotFoundFileError,ResponseError

def error_management_and_processes(ignored_words_result_txt=[".", ",", "?", "!", ":", ";", "\"", "'", "-", "—", "(", ")", "[", "]", "...", "/", "{", "}", "<", ">", "|", "\\","\n"],
                                   counter_sentences=0, counter_line=0 ,counter_words=0,ignored_words_txt='', ignored_dic_result={},
                                   max_answer=0, min_answer=0,consecutive_words_counter=1,counter_consecutive_words_counter=0,
                                   all_words_list=[],sum_len_of_words =0, ava_len_of_words=0,range_of_length_of_word=[],
                                   new_counter_words=0,word_jump=0,different_pattern_of_words_jump={},sign_of = ''):               
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
 
                        all_words_list = result_txt.split()
                        counter_words = len(all_words_list)
                        counter_line = len(result_txt.split('\n'))
        
                        for i in all_words_list:
                            sum_len_of_words += len(i)
                        ave_len_of_words = sum_len_of_words / counter_words  

                    elif k == 4 and answer in 'yY':
                        k=5
                        try:
                            answer = input(questions[5])
                            with open(answer, mode='r') as file:
                                ignored_words_txt = file.read()
                                ignored_words_result_txt = ignored_words_txt.split()
                                
                                for i in all_words_list:
                                    if i in ignored_words_result_txt:
                                        result_txt = re.sub(re.escape(i),' ', result_txt)
        
                                counter_words = len(all_words_list)


                        except FileNotFoundError:
                            raise NotFoundFileError()
                    elif k==8:
                        try:
                            print('✔ Your file has been processed')
                            with open(answer, mode='w') as file:
                                final_result =  {
                                        '🟢 Counter sentences:' : counter_sentences,'\n'
                                        '🟢 All of the words in your file:' : all_words_list,'\n'
                                        '🟢 Counter words:' : counter_words,'\n'
                                        '🟢 Counter lines:' : counter_line,'\n'
                                        '🟢 Ignored words list:' : ignored_words_result_txt,'\n'
                                        '🟢 The average length of words in your text:' : ave_len_of_words
                                    }
                                
                                data = json.load(file)  
                                  
                        except FileNotFoundError:
                            raise NotFoundFileError()   
                              
                except FileNotFoundError:
                    raise NotFoundFileError()      
                    
            if k == 4 and answer in 'nN':
                k = 6 
                continue

            if k in [2, 6, 7]:
                if k==2 and (answer in 'nN'):  
                    k = 4
                    continue

                try:
                    if k==2 and answer not in 'nN':
                        sign_of = True
                        answer = int(answer)
                    
                        word_jump = answer
                        different_pattern_of_words_jump = [] 
                        
                        result_of_sort_consecutive_words_counter = {}
                                            
                        for i in range(len(all_words_list)-(word_jump-1)):
                                different_pattern_of_words_jump.append(' '.join(all_words_list[i:i+word_jump])) 
                        for i in different_pattern_of_words_jump:
                            result_of_sort_consecutive_words_counter[different_pattern_of_words_jump.count(i)] =  i
                            
                        if k==3 and answer in 'dD':
                            sorted_dict = dict(sorted(result_of_sort_consecutive_words_counter.items(), key=itemgetter(1)))
                        elif k==3 and answer in 'Aa':
                            sorted_dict_desc = dict(sorted(result_of_sort_consecutive_words_counter.items(), key=itemgetter(1), reverse=True))        
    
                    result_dict_for_normal_pattern = {}
                    result_dict_for_normal_pattern ={i:all_words_list.count(i) for i in all_words_list}
                    
                    if k==3 and sign_of in 'True':
                        if k==3 and answer in 'dD':
                           sorted_dict = dict(sorted(result_of_sort_consecutive_words_counter.items(), key=itemgetter(1)))
                        if k==3 and answer in 'aA':    
                           sorted_dict_desc = dict(sorted(result_of_sort_consecutive_words_counter.items(), key=itemgetter(1), reverse=True))
                           
                    if k==3 and sign_of not in 'True':
                        if k==3 and answer in 'dD':
                           sorted_dict = dict(sorted(result_dict_for_normal_pattern.items(), key=itemgetter(1)))
                        if k==3 and answer in 'aA':    
                           sorted_dict_desc = dict(sorted(result_dict_for_normal_pattern.items(), key=itemgetter(1), reverse=True))
                        

                    if k == 6:
                        max_answer = answer
                    if k == 7:
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

        print('🟢 Counter sentences:' , counter_sentences,'\n',
                                        '🟢 All of the words in your file:', all_words_list,'\n',
                                        '🟢 Counter words:' , counter_words,'\n',
                                        '🟢 Counter lines:' ,counter_line,'\n',
                                        '🟢 Ignored words list:' , ignored_words_result_txt,'\n',
                                        '🟢 The average length of words in your text:' , ave_len_of_words)
        
    except (ValueError, TheEndAtTheBeginningError, ResponseRangeError,ExitConditionError,NotFoundFileError,ResponseError) as e:

        print(e)
error_management_and_processes()