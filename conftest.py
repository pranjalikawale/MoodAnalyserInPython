import pytest
from  mood_analyser import MoodAnalyser
#Fixtures are functions, which will run before each test function to which it is applied.
#Fixtures are used to feed some data to the tests such as database connections, 
#URLs to test and some sort of input data.
@pytest.fixture
def mood_analyser_object_with_sad():
   analyser_object=MoodAnalyser("I am sad")
   return analyser_object

@pytest.fixture
def mood_analyser_object_with_happy():
   analyser_object=MoodAnalyser("I am happy")
   return analyser_object   

@pytest.fixture
def mood_analyser_object():
   analyser_object=MoodAnalyser()
   return analyser_object      