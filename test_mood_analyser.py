import pytest
from  mood_analyser import MoodAnalyser
from  mood_analyser_exception import MoodAnalyserException
from  mood_analyser_factory import MoodAnalyserFactory

class TestMoodAnalyser:

    def test_passed_when_contain_sad(self,mood_analyser_object):
        assert mood_analyser_object.analyse_mood("I am Sad")=="sad"

    def test_passed_when_contain_happy(self,mood_analyser_object):
        assert mood_analyser_object.analyse_mood("I am Happy")=="happy"
