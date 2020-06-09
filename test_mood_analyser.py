import pytest
from  mood_analyser import MoodAnalyser
from  mood_analyser_exception import MoodAnalyserException
from  mood_analyser_factory import MoodAnalyserFactory

class TestMoodAnalyser:

    def test_passed_when_contain_sad(self,mood_analyser_object):
        assert mood_analyser_object.analyse_mood("I am Sad")=="sad"

    def test_passed_when_contain_happy(self,mood_analyser_object):
        assert mood_analyser_object.analyse_mood("I am Happy")=="happy"

    def test_passed_if_none_message_then_throws_exception(self,mood_analyser_object):
        with pytest.raises(MoodAnalyserException) as exception:
            mood_analyser_object.analyse_mood(None)
        assert str(exception.value)=="None mood is invalid"