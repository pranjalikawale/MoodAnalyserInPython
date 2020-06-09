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

