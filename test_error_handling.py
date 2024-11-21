import pytest
from main_project import error_management_and_processes
from dependensyOfProject import ( TheEndAtTheBeginningError,
                                    ResponseRangeError1,
                                    ResponseRangeError2,
                                    ResponseRangeError3,
                                    ResponseRangeError4,
                                    ResponseRangeError5,
                                    ExitConditionError,
                                    NotFoundFileError,
                                    ResponseError)
   
class TestResponseRangeError1:
    def test_default_message(self):
        error = ResponseRangeError1()
        assert str(error) == '🛑 You have two ways to respond, y or n!'

    def test_custom_message(self):
        custom_message = 'this is a custom error'
        error = ResponseRangeError1(custom_message)
        assert str(error) == custom_message

class TestResponseRangeError2:
    def test_default_message(self):
        error = ResponseRangeError2()
        assert str(error) == '🛑 You have two ways to respond, a or d!'

    def test_custom_message(self):
        custom_message = 'this is a custom error'
        error = ResponseRangeError2(custom_message)
        assert str(error) == custom_message

class TestResponseRangeError3:
    def test_default_message(self):
        error = ResponseRangeError3()
        assert str(error) == '🛑 Your answer should be integer!'

    def test_custom_message(self):
        custom_message = 'this is a custom error'
        error = ResponseRangeError3(custom_message)
        assert str(error) == custom_message

class TestResponseRangeError4:
    def test_default_message(self):
        error = ResponseRangeError4()
        assert str(error) == '🛑 You have two ways to respond, c or e!'

    def test_custom_message(self):
        custom_message = 'this is a custom error'
        error = ResponseRangeError4(custom_message)
        assert str(error) == custom_message

class TestResponseRangeError5:
    def test_default_message(self):
        error = ResponseRangeError5()
        assert str(error) == '🛑 Your answer must be a positive integer!'

    def test_custom_message(self):
        custom_message = 'this is a custom error'
        error = ResponseRangeError5(custom_message)
        assert str(error) == custom_message

class TestExitConditionError:
    def test_default_message(self):
        error = ExitConditionError()
        assert str(error) == 'The process of processing your file is finished👋🙂'

    def test_custom_message(self):
        custom_message = 'this is a custom error'
        error = ExitConditionError(custom_message)
        assert str(error) == custom_message

class TestNotFoundFileError:
    def test_default_message(self):
        error = NotFoundFileError()
        assert str(error) == '🛑 File not found!'

    def test_custom_message(self):
        custom_message = 'this is a custom error'
        error = NotFoundFileError(custom_message)
        assert str(error) == custom_message

class ResponseError:
    def test_default_message(self):
        error = ResponseError()
        assert str(error) == '🛑 Your answer must be an integer or n!'
        
    def test_custom_message(self):
        custom_message = 'this is a custom error'
        error = ResponseError(custom_message)
        assert str(error) == custom_message

class TheEndAtTheBeginningError:
    def test_default_message(self):
        error = TheEndAtTheBeginningError()
        assert str(error) == 'If you don\'t want your case to be processed, what are you doing here?!🙃'
        
    def test_custom_message(self):
        custom_message = 'this is a custom error'
        error = TheEndAtTheBeginningError(custom_message)
        assert str(error) == custom_message
            