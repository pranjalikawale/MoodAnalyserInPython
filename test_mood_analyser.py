import pytest
from  mood_analyser import MoodAnalyser
from  mood_analyser_exception import MoodAnalyserException
from  mood_analyser_factory import MoodAnalyserFactory

class TestMoodAnalyser:

    def test_pass_when_contain_sad(self,mood_analyser_object):
        assert mood_analyser_object.analyse_mood("I am Sad")=="sad"

    def test_pass_when_contain_happy(self,mood_analyser_object):
        assert mood_analyser_object.analyse_mood("I am Happy")=="happy"

    def test_pass_when_none_message_then_throws_exception(self,mood_analyser_object):
        with pytest.raises(MoodAnalyserException) as exception:
            mood_analyser_object.analyse_mood(None)
        assert str(exception.value)=="None mood is invalid"

    def test_pass_when_empty_message_then_throws_exception(self,mood_analyser_object):
        with pytest.raises(MoodAnalyserException) as exception:
            mood_analyser_object.analyse_mood()
        assert str(exception.value)=="Empty mood is invalid"
    
    def test_pass_when_contain_sad_by_constructor(self,mood_analyser_object_with_sad):
        assert mood_analyser_object_with_sad.analyse_mood()=="sad"

    def test_passed_when_contain_happy_by_constructor(self,mood_analyser_object_with_happy):
        assert mood_analyser_object_with_happy.analyse_mood()=="happy"

    def test_passed_given_empty_message_to_constuctor_then_throws_exception(self,mood_analyser_object):
        with pytest.raises(MoodAnalyserException) as exception:
            mood_analyser_object.analyse_mood()
        assert str(exception.value)=="Empty mood is invalid"
        
    def test_passed_given_none_message_to_constuctor_then_throws_exception(self):
        with pytest.raises(MoodAnalyserException) as exception:
            analyser_object=MoodAnalyser(None)
            analyser_object.analyse_mood()
        assert str(exception.value)=="None mood is invalid"

    def test_pass_when_given_mood_analyse_class_should_return_object(self,mood_analyser_object):
        assert mood_analyser_object.equals(MoodAnalyserFactory.create_mood_analyser_object
                                          ("mood_analyser","MoodAnalyser"))==True

    def test_pass_when_given_mood_analyse_class_with_message_should_return_object(self, mood_analyser_object_with_happy):
        assert mood_analyser_object_with_happy.equals(MoodAnalyserFactory.create_mood_analyser_object
                                          ("mood_analyser","MoodAnalyser","I am happy"))==True

    def test_pass_when_given_wrong_class_should_throw_module_not_found_exception(self,mood_analyser_object):
        with pytest.raises(MoodAnalyserException) as exception:
            mood_analyser_object.equals(MoodAnalyserFactory.create_mood_analyser_object
                                          ("mood_analyser","MoodAnalyser1"))
        assert str(exception.value)=="Module not found error"
        
    def test_pass_when_given_filepath_should_throw_module_not_found_exception(self, mood_analyser_object):
        with pytest.raises(MoodAnalyserException) as exception:
            mood_analyser_object.equals(MoodAnalyserFactory.create_mood_analyser_object
                                          ("mood_analyser1","MoodAnalyser"))
        assert str(exception.value)=="Module not found error"

    def test_pass_when_given_method_should_return_happy(self):
        assert MoodAnalyserFactory.invoke_method(MoodAnalyserFactory.create_mood_analyser_object
                            ("mood_analyser","MoodAnalyser","I am happy"),"analyse_mood")=="happy"

    def test_pass_when_given_wrong_method_should_throw_method_not_found_exception(self):
        with pytest.raises(MoodAnalyserException) as exception:
            MoodAnalyserFactory.invoke_method(MoodAnalyserFactory.create_mood_analyser_object
                            ("mood_analyser","MoodAnalyser"),"analyse_mood1")
        assert str(exception.value)=="Method not found error"

    def test_pass_when_given_field_when_proper_should_return_happy(self):
        assert MoodAnalyserFactory.invoke_method(MoodAnalyserFactory.set_field_dynamically(MoodAnalyserFactory.create_mood_analyser_object
                            ("mood_analyser","MoodAnalyser","I am sad"),"message","I am happy"),"analyse_mood")=="happy"

    def test_pass_when_given_wrong_field_should_throw_field_not_found_exception(self):
        with pytest.raises(MoodAnalyserException) as exception:
            assert MoodAnalyserFactory.invoke_method(MoodAnalyserFactory.set_field_dynamically(MoodAnalyserFactory.create_mood_analyser_object
                            ("mood_analyser","MoodAnalyser","I am sad"),"message1","I am happy"),"analyse_mood")
        assert str(exception.value)=="Field not found error"