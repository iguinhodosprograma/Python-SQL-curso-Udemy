class ClassTest:
    def instance_method(self): #Usado quando é necessário usar dados do objeto, ou modificar dados do objeto
        print(f"Called instance_method of {self}")
    
    @classmethod
    def class_method(cls): #
        print(f"Called class_method of {cls}")
    
    @staticmethod
    def static_method(): #Usado quando não é necessários usar o "self" ou "cls", um método dentro da classe
        print("Called static_method.")
        
ClassTest.class_method()

ClassTest.static_method()
