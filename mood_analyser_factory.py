from mood_analyser_exception import MoodAnalyserException
from mood_analyser import MoodAnalyser

class MoodAnalyserFactory:
    #create mood analyser object in factory
    @staticmethod
    def create_mood_analyser_object(file_path,class_name,*message):
        try:
            module_name=__import__(file_path)
            module_name=getattr(module_name,class_name)
            if len(message)==0:
                return module_name()
            else:
                return module_name(message[0])
        except:
            raise MoodAnalyserException("Module not found error","MODULE_NOT_FOUND_ERROR")
    
    #invoke method of mood_analyser class
    @staticmethod
    def invoke_method(mood_object,method_name):
        try:
            method=getattr(mood_object,method_name)
            return method()
        except:
            raise MoodAnalyserException("Method not found error","METHOD_NOT_FOUND_ERROR")

    #set field dynamically
    @staticmethod
    def set_field_dynamically(mood_object,field_name,message):
        try:
            getattr(mood_object,field_name)
            setattr(mood_object,field_name,message)
            return mood_object
        except:
            raise MoodAnalyserException("Field not found error","FIELD_NOT_FOUND_ERROR")



            

