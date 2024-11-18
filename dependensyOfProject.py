questions = {
    0:'Hi! welcome to command line interface(📍if you want to exit at any part of the program please enter "q" and be mindful which enter the full path of your file). Are you sure wanna continue? [Y/n]:',
    1:'Please enter path of your file:',
    2:'Please enter a number for consecutive words counter(if you don\'t have any idea for consecutive words counter please enter\'n\'):',
    3:'Should the sort be ascending or descending? [a/D]:',
    4:'Do you have any ignored words file? [Y/n]:',
    5:'Please enter path of your ignored words file(Your words in your ignored file should be separated by \'space\'):',
    6:'Please enter a number for the maximum character range of words:',
    7:'Please enter a number for the minimum character range of words:',
    8:'If you want to continue, the max range counter will be replaced with the min range counter otherwise, the program will exit! [C/e]:',
    9:'Please enter path of your file which you want to save there:'
}

class TheEndAtTheBeginningError(Exception):
        def __init__(self, message='If you don\'t want your case to be processed, what are you doing here?!🙃'):
            super().__init__(message)
class ResponseRangeError1(Exception):                
        def __init__(self, message='🛑 You have two ways to respond, y or n!'):
            super().__init__(message) 
class ResponseRangeError2(Exception):                
        def __init__(self, message='🛑 You have two ways to respond, a or d!'):
            super().__init__(message)  
class ResponseRangeError3(Exception):                
        def __init__(self, message='🛑 Your answer should be integer!'):
            super().__init__(message)                           
class ResponseRangeError4(Exception):                
        def __init__(self, message='🛑 You have two ways to respond, c or e!'):
            super().__init__(message)
class ResponseRangeError5(Exception):                
        def __init__(self, message='🛑 Your answer must be a positive integer!'):
            super().__init__(message)             
class ExitConditionError(Exception):
        def __init__(self, message='The process of processing your file is finished👋🙂'):
            super().__init__(message)  
class NotFoundFileError(Exception):
        def __init__(self, message='🛑 File not found!'):
            super().__init__(message)
class ResponseError(Exception):
        def __init__(self, message='🛑 Your answer must be an integer or n!'):
            super().__init__(message)  
              