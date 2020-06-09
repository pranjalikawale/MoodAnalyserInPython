from  mood_analyser_exception import MoodAnalyserException

class MoodAnalyser:
    #initialize object
    def __init__(self,*message):
        if(len(message)>0):
            self.message=message[0]

    #method for mood analyses
    def analyse_mood(self,*message):
        if(len(message)>0):
            self.message=message[0]
        self.check_for_null()
        self.check_for_empty()

        if "sad" in self.message.casefold():
            self.message="sad"
        elif "happy" in self.message.casefold():
            self.message="happy"
        else:
            self.message="Plz enter valid string msg."
        return self.message

    #check for none message
    def check_for_null(self):    
        if self.message==None:
            raise MoodAnalyserException("None mood is invalid","NONE_ERROR")

    #check for empty message
    def check_for_empty(self):
        if self.message=="":
            raise MoodAnalyserException("Empty mood is invalid","EMPTY_ERROR")
    
    #check for equality
    def equals(self,mood_object):
        if mood_object !=None and isinstance(mood_object,MoodAnalyser) and mood_object.message==self.message:
            return True
        return False    



  